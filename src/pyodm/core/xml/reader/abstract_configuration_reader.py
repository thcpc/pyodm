import abc

from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractConfigurationReader(abc.ABC):
    @abc.abstractmethod
    def load_cdisc_definition(self, registry: CdiscRegistry, files: list[str]): ...
