import pathlib

from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.model import odm_xsd_description

if __name__ == '__main__':
    # 数据 XML 文件的路径
    data_file = PathSource("subjectData.xml")
    # pyodm 内置 ODM V2的XSD 文件
    xsd_files = odm_xsd_description()
    # data_file 数据文件路径
    # xsd_files XSD配置文件路径
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    # 生成 ODM 对象
    odm = cdisc.odm()
    print(odm.ClinicalData.index(0).StudyOID.value)
    print(odm.ClinicalData.index(0).SubjectData.index(0).SubjectKey.value)
