import pathlib

from pyodm.core.xml.reader.data.xml_data_reader import XMLDataReader
from pyodm.core.xml.reader.configuration.cdisc_configuration_specification_reader import \
    CdiscConfigurationSpecificationReader
from pyodm.factory.abstract_cdisc_xml_factory import AbstractCdiscXMLFactory


class CdiscSpecificationFactory(AbstractCdiscXMLFactory):
    """
    Class 类型的对象定义在Specification 中
    """
    def __init__(self, data_file: pathlib.Path, specification_files: list):
        """

        :param data_file: 数据文件路径
        :type data_file: pathlib.Path
        :param specification_files: 定义 Class 的配置
        :type specification_files: list[pathlib.Path]
        """
        super().__init__(data_file)
        self._specification_files = specification_files

    def clazz_reader(self):
        CdiscConfigurationSpecificationReader().load_cdisc_definition(self, self._specification_files)

    def data_reader(self) -> XMLDataReader:
        return XMLDataReader(self)

