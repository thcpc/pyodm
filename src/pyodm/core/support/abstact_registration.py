import abc


class AbstractRegistration(abc.ABC):
    def __init__(self):
        self._registry = None

    @property
    def registry(self): return self._registry

    @registry.setter
    def registry(self, value): self._registry = value
