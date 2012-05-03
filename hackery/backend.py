__author__ = 'Kiril Savino'

from collections import defaultdict

class Backend(object):
    def __init__(self):
        self.counts = defaultdict(lambda:0)

    def count(self, event):
        event = str(event)
        self.counts[event] += 1

    def _count_of(self, event):
        return self.counts.get(event) or 0

class PrintingBackend(Backend):
    def count(self, event):
        Backend.count(self, event)
        print "{0} happened {1} times so far".format(event, self._count_of(event))

