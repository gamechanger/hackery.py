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
        self.client.hincrby('hack_events', event, 1)
