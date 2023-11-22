import abc

from pyodm.core.xml.reader.configuration.cdisc_configuration_xsd_reader import CdiscConfigurationXsdReader
from pyodm.factory.abstract_cdisc_factory import AbstractCdiscFactory


class AbstractAssembleFactory(AbstractCdiscFactory, abc.ABC):
    """
    继承自 抽象 Factory 可修改 ODM 描述方法
    通过 赋值 reader_class
    不同的 reader_class 要对应不同 configuration_files
    """
    def __init__(self, configuration_files: list = None):
        super().__init__()
        self._configuration_files = configuration_files if configuration_files else self.default_description_files()
        self._reader_class = CdiscConfigurationXsdReader

    @property
    def reader_class(self): return self._reader_class

    @reader_class.setter
    def reader_class(self, clazz): self._reader_class = clazz

    def clazz_reader(self):
        self._reader_class().load_cdisc_definition(self, self._configuration_files)