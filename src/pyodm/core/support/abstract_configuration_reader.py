import abc
import pathlib

from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractConfigurationReader(abc.ABC):
    """
    读取配置文件的抽象方法定义，load_cdisc_definition()
    """
    @abc.abstractmethod
    def load_cdisc_definition(self, registry: CdiscRegistry, files: list[pathlib.Path]): ...
