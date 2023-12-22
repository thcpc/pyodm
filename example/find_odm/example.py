from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory

from src.pyodm.utils.finder import Finder

if __name__ == '__main__':
    odm = CdiscXMLXsdFactory(data_file=PathSource("odmData.xml")).odm()

    """
    按层级查找，一层一层的查询自己期望的 ODM 对象
    """
    subject_finder = Finder().element(name="SubjectData").attribute(SubjectKey="D001001").Lambda()
    study_event_finder = Finder().element(name="StudyEventData").attribute(StudyEventOID="Screening").Lambda()
    study_event = odm.as_stream().find(_lambda=subject_finder).find(_lambda=study_event_finder).get()

    """
    直接查找自己期望的对象
    """
    item_finder = Finder().element(name="ItemData").attribute(ItemOID="SVDAT").Lambda()
    item = odm.as_stream().find(_lambda=item_finder).get()

    """
    自定义查询的lambda
    """
    item = odm.as_stream().find(
        _lambda=lambda x: x.get_name() == 'SubjectData' and x.SubjectKey.get_value() == 'D001001').get()
