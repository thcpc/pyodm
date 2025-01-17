from pathlib import Path

from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.model.cdisc.classv2.element import StudyEventData, ItemGroupData


def define_study_event():
    """
    定义一个 访视
    访视下面有 Screen 和 Chemistry 两个表单
    Screen 是一个单 IG
    Chemistry 是一个多 IG
    :return:
    :rtype:
    """
    study_event = StudyEventData()
    study_event.StudyEventOID.set_value("999")
    study_event.StudyEventRepeatKey.set_value("False")
    screen = ItemGroupData()
    screen.ItemGroupOID.set_value("Screen")
    chemistry = ItemGroupData()
    chemistry.ItemGroupOID.set_value("Chemistry")
    ig1 = ItemGroupData()
    ig1.ItemGroupDataSeq.set_value("COL1")
    ig2 = ItemGroupData()
    ig2.ItemGroupDataSeq.set_value("COL2")
    ig3 = ItemGroupData()
    ig3.ItemGroupDataSeq.set_value("COL3")
    chemistry.ItemGroupData.array.append(ig1)
    chemistry.ItemGroupData.array.append(ig2)
    chemistry.ItemGroupData.array.append(ig3)
    study_event.ItemGroupData.array.append(screen)
    study_event.ItemGroupData.array.append(chemistry)
    cw = CdiscXmlWriter(study_event, out_put=Path("test11.xml"))
    cw.write()


if __name__ == '__main__':
    define_study_event()