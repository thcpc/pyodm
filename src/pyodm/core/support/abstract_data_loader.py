import abc


class AbstractDataLoader(abc.ABC):
    @abc.abstractmethod
    def load(self): ...
