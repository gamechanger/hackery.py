__author__ = 'Kiril Savino'

from pyvows import Vows, expect

from hackery import Hack
from hackery import Backend

@Vows.batch
class HackTest(Vows.Context):
    def topic(self):
        return None

    def should_be_none(self, topic):
        expect(topic).to_be_null()


"""
- Frequency
- Lifespan
- Conditions: API Client, Time, Etc.
- Expiration Dates
- Alerts: expiration! frequency change!  etc.!
"""

with Hack('fancy_stuff') as hack:
    if hack:
        pass
