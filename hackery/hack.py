__author__ = 'Kiril Savino'

from backend import PrintingBackend

class Hack(object):
    backend = PrintingBackend()

    def shoud_fire(self):
        return True

    def count(self, event):
        self.backend.count(event)

