
import pathlib

from pyodm.core.source.path_source import PathSource

from pyodm.factory.cdisc_xml_specification_factory import CdiscXMLSpecificationFactory


if __name__ == '__main__':
    # 数据 XML 文件的路径
    data_file = PathSource("data.xml")
    # pyodm 内置 ODM V2的 定义 Class 配置
    specification_files = [pathlib.Path("custom.xml")]
    # data_file 数据文件路径
    # specification_files 定义 Class 的配置
    cdisc = CdiscXMLSpecificationFactory(data_file=data_file, specification_files=specification_files)
    # 生成 ODM 对象
    subject_form = cdisc.odm()
    print(subject_form.Name.value)
    for subject_item in subject_form.SubjectItem.array:
        print(subject_item.Id.value)
        print(subject_item.Name.value)
        print(subject_item.value)
