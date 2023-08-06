import logging
import redis


class RedisLogHandler(logging.Handler):

    def __init__(self, key, host='localhost'):
        logging.Handler.__init__(self)
        self.key = key
        self.redis_server = redis.Redis(host)

    def emit(self, record):
        try:
            self.redis_server.rpush(self.key, self.format(record))
        except:  # noqa
            pass
