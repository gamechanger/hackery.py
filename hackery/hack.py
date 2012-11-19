
from backend import PrintingBackend

default_backend = PrintingBackend()

def set_default_backend(backend):
    global default_backend
    default_backend = backend

class Hack(object):
    def __init__(self, name, backend=None, condition=None):
        self.name = name
        self.backend = backend or default_backend
        self.backend.record_hack(self.name)
        self.condition = condition

    def __enter__(self):
        if self._should_fire():
            self.backend.count(self.name)
            return self
        return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _should_fire(self):
        """
        Have we met the conditions for this hack to be fired?
        """
        if self.condition and callable(self.condition):
            return self.condition()
        return True

    def count(self, event):
        self.backend.count('{0}.{1}'.format(self.name, event))
