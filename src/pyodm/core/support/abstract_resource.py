import abc


class AbstractResource(abc.ABC):
    @abc.abstractmethod
    def load(self): ...
