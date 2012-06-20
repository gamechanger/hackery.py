__author__ = 'Kiril Savino'

import time
from collections import defaultdict

class Backend(object):
    def __init__(self):
        self.counts = defaultdict(lambda:0)
        self.times = dict()
        self.hacks = set()

    def call(self, name):
        self.hacks.add(name)

    def count(self, event):
        event = str(event)
        self.counts[event] += 1
        self.times[event] = time.time()


    def _count_of(self, event):
        return self.counts.get(event) or 0

class PrintingBackend(Backend):
    def call(self, name):
        super(PrintingBackend, self).call(name)
        print "{0} called".format(name)

    def count(self, event):
        super(PrintingBackend, self).count(self, event)
        print "{0} happened {1} times so far".format(event, self._count_of(event))
