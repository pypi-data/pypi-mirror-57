# -*- coding: utf-8 -*-
import json
import redis
import logging

logger = logging.getLogger('pubsub')
fh = logging.StreamHandler()
fh.setFormatter(logging.Formatter(fmt='%(asctime)-22s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class PubSub(object):

    def __init__(self, host='localhost', port=6379, database=0):
        self.connection = None
        self.pubsub = None
        self.host = host
        self.port = port
        self.database = database

    def emit(self, event, message, emit=False):

        # Convert dict to string
        message_str = json.dumps(message)
        logger.debug(" [x] Sent %r:%r" % (event, message_str))

        if not emit:
            return

        self.connection = redis.StrictRedis(host=self.host, port=self.port, db=self.database)
        self.pubsub = self.connection.pubsub()

        self.connection.publish(channel=event, message=message_str)

        self.pubsub.close()

    def receive(self, listeners, restart_connections=None):
        self.connection = redis.StrictRedis(host=self.host, port=self.port, db=self.database)
        self.pubsub = self.connection.pubsub(ignore_subscribe_messages=True)

        def callback(message):
            """
            Receiving messages from the queue.
            It works by subscribing a callback function to a queue.
            """
            # Convert str to dict and call handler event function and get handler for event.
            # print(" [x] %r:%r" % (method.routing_key, body))
            logger.debug(u'[x] %(routing_key)s: %(body)s' % {
                'routing_key': message.get('channel'), 'body': message.get('data')
            })
            function = listeners.get(message.get('channel').decode("utf-8"))
            if function is None:
                print('Listener not found %s' % str(message.get('channel').decode("utf-8")))
                return
            my_body = json.loads(message.get('data'))
            logger.debug(u'[f] %(function)s loaded' % {'function': function})
            if restart_connections is not None:
                restart_connections()

            for item in function:
                item(my_body)

        for key in listeners.keys():
            for loaded_func in listeners.get(key):
                logger.info('Loaded function for key %r: %r' % (key, loaded_func.__name__))

            self.pubsub.subscribe(**{key: callback})

        logger.info(' [*] Waiting for logs. To exit press CTRL+C')

        for item in self.pubsub.listen():
            pass

        self.pubsub.close()
