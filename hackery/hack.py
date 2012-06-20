__author__ = 'Kiril Savino'

from backend import PrintingBackend

class Hack(object):
    backend = PrintingBackend()
    def __init__(self, name):
        self.name = name
        self.backend.call(self.name)

    def __enter__(self):
        if self._should_fire():
            self.backend.count(self.name)
            return self
        return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _should_fire(self):
        return True

    def count(self, event):
        self.backend.count('{0}.{1}'.format(self.name, event))
