__author__ = 'Doug Woos'

from pyvows import Vows
from mockito import mock, verify, any as mockito_any, when

import os
import sys
sys.path.append(os.path.abspath('{0}/../../'.format(__file__)))

from hackery import Hack
from hackery import RedisBackend

class RedisBackendContext(Vows.Context):
    def topic(self):
        redis = mock()
        # when a pipeline is requested, just return ourselves
        when(redis).pipeline(transaction=mockito_any()).thenReturn(redis)
        backend = RedisBackend(redis)
        self.manipulate_backend(backend)
        return redis

@Vows.batch
class ARedisBackend(Vows.Context):
    class WhenHackDefined(RedisBackendContext):
        def manipulate_backend(self, backend):
            Hack('test_hack', backend)

        def should_call_sadd_once(self, redis):
            verify(redis, times=1).sadd('hacks', 'test_hack')

    class WhenTwoHacksDefined(RedisBackendContext):
        def manipulate_backend(self, backend):
            Hack('test_hack', backend)
            Hack('test_hack2', backend)

        def should_call_sadd_first(self, redis):
            verify(redis, times=1).sadd('hacks', 'test_hack')

        def should_call_sadd_second(self, redis):
            verify(redis, times=1).sadd('hacks', 'test_hack2')

    class WhenHackDefinedTwice(RedisBackendContext):
        def manipulate_backend(self, backend):
            Hack('test_hack', backend)
            Hack('test_hack', backend)

        def should_call_sadd_once(self, redis):
            verify(redis, times=1).sadd('hacks', 'test_hack')

    class WhenHackFired(RedisBackendContext):
        def manipulate_backend(self, backend):
            with Hack('test_hack', backend) as hack:
                pass

        def should_increment_count(self, redis):
            verify(redis).hincrby('hack_events', 'test_hack', 1)

        def should_set_time(self, redis):
            verify(redis).hset('hack_times', 'test_hack', mockito_any())

    class WhenHackEventFired(WhenHackFired):
        def manipulate_backend(self, backend):
            with Hack('test_hack', backend) as hack:
                hack.count('test_event')

        def should_increment_event_count(self, redis):
            verify(redis).hincrby('hack_events', 'test_hack.test_event', 1)

        def should_set_event_time(self, redis):
            verify(redis).hset('hack_times', 'test_hack.test_event', mockito_any())
