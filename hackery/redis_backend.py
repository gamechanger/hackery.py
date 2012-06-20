import time
from backend import Backend

class RedisBackend(Backend):

    def __init__(self, client):
        super(RedisBackend, self).__init__()
        self.client = client

    def call(self, name):
        super(RedisBackend, self).call(name)
        self.client.sadd('hacks', name)


    def count(self, event):
        super(RedisBackend, self).count(event)
        pipe = self.client.pipeline(transaction=False)
        pipe.hincrby('hack_events', event, 1)
        pipe.hset('hack_times', event, time.time())
        pipe.execute()
