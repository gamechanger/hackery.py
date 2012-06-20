__author__ = 'Doug Woos'

from pyvows import Vows, expect

import os
import sys
sys.path.append(os.path.abspath('{0}/../../'.format(__file__)))

from hackery import Hack
from hackery import VersionHack
from hackery import Backend

@Vows.create_assertions
def to_match_as_set(topic, expected):
    return set(topic) == set(expected)


class TestBackend(Backend):
    pass

@Vows.batch
class HackeryContext(Vows.Context):

    class HackContext(Vows.Context):
        def topic(self):
            return lambda: Hack('test_hack', backend=TestBackend())

        class HackRecordContext(Vows.Context):
            def topic(self, hack_fn):
                return hack_fn()

            def should_record_hack(self, topic):
                expect(topic.backend.hacks).to_match_as_set(set(['test_hack']))

        class HackFireContext(Vows.Context):
            def topic(self, hack_fn):
                with hack_fn() as hack:
                    return hack

            def should_record_hack(self, topic):
                expect(topic.backend.hacks).to_match_as_set(set(['test_hack']))

            def should_fire(self, topic):
                expect(topic.backend.counts).to_be_like({'test_hack': 1})

            def should_time_fire(self, topic):
                expect(topic.backend.last_times).to_include('test_hack')

            def should_only_time_fire(self, topic):
                expect(topic.backend.last_times).to_length(1)

        class HackCountContext(Vows.Context):
            def topic(self, hack_fn):
                with hack_fn() as hack:
                    hack.count('test_event')
                    return hack

            def should_record_hack(self, topic):
                expect(topic.backend.hacks).to_match_as_set(['test_hack'])

            def should_count(self, topic):
                expect(topic.backend.counts).to_be_like({'test_hack': 1, 'test_hack.test_event': 1})

            def should_time_fire(self, topic):
                expect(topic.backend.last_times).to_include('test_hack')

            def should_time_count(self, topic):
                expect(topic.backend.last_times).to_include('test_hack.test_event')

            def should_only_time_fire_and_count(self, topic):
                expect(topic.backend.last_times).to_length(2)

        class HackCountMoreContext(Vows.Context):
            def topic(self, hack_fn):
                with hack_fn() as hack:
                    hack.count('test_event')
                    hack.count('test_event')
                    return hack

            def should_record_hack(self, topic):
                expect(topic.backend.hacks).to_match_as_set(['test_hack'])

            def should_count_twice(self, topic):
                expect(topic.backend.counts).to_be_like({'test_hack': 1, 'test_hack.test_event': 2})

            def should_time_fire(self, topic):
                expect(topic.backend.last_times).to_include('test_hack')

            def should_time_count(self, topic):
                expect(topic.backend.last_times).to_include('test_hack.test_event')

            def should_only_time_fire_and_count(self, topic):
                expect(topic.backend.last_times).to_length(2)

    class VersionHackContext(HackContext):
        def topic(self):
            return lambda: VersionHack('test_hack', 'android==2', {'android': 2}, backend=TestBackend())

        class VersionHackConstrainFailureContext(Vows.Context):
            def topic(self):
                hack = VersionHack('test_hack', 'android==2', {'android': 3}, backend=TestBackend())
                with hack as h:
                    return h


            def should_not_fire(self, topic):
                expect(topic).to_be_false()
