__author__ = 'Kiril Savino'

from backend import PrintingBackend

class Hack(object):
    backend = PrintingBackend()

    def __enter__(self):
        return self if self._should_fire() else False

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _should_fire(self):
        return True

    def count(self, event):
        self.backend.count(event)

