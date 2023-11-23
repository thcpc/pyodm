import pathlib

from cjen.nene.database_info import DataBaseInfo


from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.factory.cdisc_listable_factory import CdiscListableFactory

from pyodm.utils.path_utils import PathUtils

from example.database.subject_data_resource import SubjectDataResource

if __name__ == '__main__':
    # 定义数据配置
    database_info = DataBaseInfo.factory(dict(
        host="",# 数据库主机
        port=3306,# 数据库端口号
        user="",# 数据库用户名
        pwd="",# 数据库密码
        database=""# 数据库库名
    ))
    # 定义数据源
    data_source = SubjectDataResource(database_info)
    # 生成 ODM 对象
    factory = CdiscListableFactory(data_source)
    odm_data = factory.odm()
    # 导出成 XML 文件
    cw = CdiscXmlWriter(odm_data, pathlib.Path(f"subject_data.xml"))
    cw.write()
