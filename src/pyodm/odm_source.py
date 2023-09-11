import abc
from abc import ABC


class ODMSource(ABC):

    @abc.abstractmethod
    def data(self) -> list[list[dict]]: ...
