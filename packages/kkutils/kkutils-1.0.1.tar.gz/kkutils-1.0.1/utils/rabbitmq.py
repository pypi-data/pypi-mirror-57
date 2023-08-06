#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Email: kai.zhang1@nio.com
Last modified: 2018-09-29 00:59:38
'''
import asyncio
import logging
import os
import pickle
from functools import partial

import aio_pika
import pika

from .decorator import aio_retry
from .decorator import retry
from .log_utils import Logger

logging.getLogger('pika').setLevel(logging.ERROR)


class Pika:

    def __init__(self, queue='test', **kwargs):
        if any([key in kwargs for key in ['host', 'port', 'user', 'pwd', 'vhost']]):
            host = kwargs.pop('host', 'localhost')
            port = kwargs.pop('port', 5672)
            user = kwargs.pop('user', 'guest')
            pwd = kwargs.pop('pwd', 'guest')
            vhost = kwargs.pop('vhost', '/')
            self.uri = f'amqp://{user}:{pwd}@{host}:{port}{vhost}'
        elif 'uri' in kwargs:
            self.uri = kwargs.pop('uri')
        elif 'MQ_URI' in os.environ:
            self.uri = os.environ['MQ_URI']
        else:
            host = os.environ.get('MQ_HOST', 'localhost')
            port = os.environ.get('MQ_PORT', 5672)
            user = os.environ.get('MQ_USER', 'guest')
            pwd = os.environ.get('MQ_PWD', 'guest')
            vhost = os.environ.get('MQ_VHOST', '/')
            self.uri = f'amqp://{user}:{pwd}@{host}:{port}{vhost}'

        self.logger = Logger()
        self.queue = queue
        self._channels = {}
        self._queues = {}
        self.connect()

    def connect(self):
        parameter = pika.URLParameters(self.uri)
        self._connection = pika.BlockingConnection(parameter)
        self.logger.info(self._connection)

    def init(self, queue=None):
        queue = queue or self.queue
        if self._connection.is_closed:
            self.connect()

        if not (queue in self._channels and not self._channels[queue].is_closed):
            channel = self._connection.channel()
            channel.basic_qos(prefetch_count=1)
            q = channel.queue_declare(queue=queue, auto_delete=False, durable=False)
            self._channels[queue] = channel
            self._queues[queue] = q

        return queue

    def size(self, queue=None):
        queue = self.init(queue)
        return self._queues[queue].method.message_count

    def _consume(self, process, ack, channel, method_frame, header_frame, body):
        try:
            if ack:
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
                process(pickle.loads(body))
            else:
                process(pickle.loads(body))
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except Exception as e:
            self.logger.exception(e)

    def consume(self, process, queue=None, ack=False):
        queue = self.init(queue)
        channel = self._channels[queue]
        channel.basic_consume(queue, partial(self._consume, process, ack))
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            self.close()

    def get(self, queue=None, ack=True):
        queue = self.init(queue)
        msg = self._channels[queue].basic_get(queue, auto_ack=ack)
        return pickle.loads(msg[-1])

    @retry
    def publish(self, msg, queue=None):
        queue = self.init(queue)
        self._channels[queue].basic_publish(exchange='',
                                            routing_key=queue,
                                            body=pickle.dumps(msg))

    def close(self):
        for channel in self._channels.values():
            if not channel.is_closed:
                channel.close()
        if not self._connection.is_closed:
            self._connection.close()


class AioPika(Pika):

    def __init__(self, queue='test', workers=1, **kwargs):
        super().__init__(queue, **kwargs)
        self.workers = workers

    async def _connect(self):
        self._connection = await aio_pika.connect_robust(self.uri, loop=self.loop)
        self.logger.info(self._connection)

    def connect(self):
        self.loop = asyncio.get_event_loop()
        if self.loop.is_running():
            self.loop.create_task(self._connect())
        else:
            self.loop.run_until_complete(self._connect())

    async def size(self, queue=None):
        queue = await self.init(queue)
        return self._queues[queue].declaration_result.message_count

    async def init(self, queue):
        queue = queue or self.queue
        if self._connection.is_closed:
            await self._connect()

        if not (queue in self._channels and not self._channels[queue].is_closed):
            channel = await self._connection.channel()
            await channel.set_qos(prefetch_count=1)
            q = await channel.declare_queue(queue, auto_delete=False, durable=False)
            self._channels[queue] = channel
            self._queues[queue] = q

        return queue

    async def _consume(self, process, queue, ack):
        async for msg in queue:
            try:
                if ack:
                    await msg.ack()
                    await process(pickle.loads(msg.body))
                else:
                    await process(pickle.loads(msg.body))
                    await msg.ack()
            except Exception as e:
                self.logger.exception(e)

    async def consume(self, process, queue=None, ack=False):
        queue = await self.init(queue)
        for _ in range(self.workers):
            self.loop.create_task(self._consume(process, self._queues[queue], ack))

    @aio_retry
    async def get(self, queue=None, ack=True):
        queue = await self.init(queue)
        while True:
            msg = await self._queues[queue].get(no_ack=ack, fail=False, timeout=None)
            if msg:
                return pickle.loads(msg.body)
            else:
                await asyncio.sleep(1)

    @aio_retry
    async def publish(self, msg, queue=None):
        queue = await self.init(queue)
        await self._channels[queue].default_exchange.publish(aio_pika.Message(pickle.dumps(msg)),
                                                             routing_key=queue)

    async def close(self):
        for channel in self._channels.values():
            if not channel.is_closed:
                await channel.close()
        if not self._connection.is_closed:
            await self._connection.close()
