import pathlib

from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdisc_xml_specification_factory import CdiscXMLSpecificationFactory
from pyodm.model import odm_specification_description

if __name__ == '__main__':
    # 数据 XML 文件的路径
    data_file = PathSource("subjectData.xml")
    # data_file 数据文件路径
    # specification_files 定义 Class 的配置
    cdisc = CdiscXMLSpecificationFactory(data_file=data_file)
    # 生成 ODM 对象
    odm = cdisc.odm()
    print(odm.ClinicalData.index(0).StudyOID.value)
    print(odm.ClinicalData.index(0).SubjectData.index(0).SubjectKey.value)