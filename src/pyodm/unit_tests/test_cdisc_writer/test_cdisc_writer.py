import pytest

from pyodm.core.loader.cdisc_clazz import CdiscClazz
from pyodm.core.xml.cdisc_config_reader import CdiscConfigReader
from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.exceptions import XmlWriterException
from pyodm.model.v2.specification import Specification
from pyodm.pyodm import PyODM


def test_case1():
    file_path = "D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\resources\\test_case1.xml"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    cw = CdiscXmlWriter(p.odm)
    cw.write()
    assert_case1("test.xml")


def test_case2():
    file_path = "D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\resources\\test_case2.xml"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    cw = CdiscXmlWriter(p.odm)
    cw.write()
    assert_case2("test.xml")


def test_case3():
    file_path = "D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\resources\\test_case3.xml"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    cw = CdiscXmlWriter(p.odm)
    cw.write()
    assert_case3("test.xml")


def test_case4():
    file_path = "D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\resources\\test_case4.xml"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    cw = CdiscXmlWriter(p.odm)
    cw.write()
    assert_case4("test.xml")


def test_case5():
    with pytest.raises(XmlWriterException):
        file_path = "D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\resources\\test_case4.xml"
        cdisc = PyODM.v2(file_path)
        c = cdisc.ClinicalData.first().SubjectData.first()
        cw = CdiscXmlWriter(c)
        cw.write()


def assert_case1(output_name):
    file_path = f"D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\{output_name}"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    x = p.odm.ClinicalData
    assert x.first().StudyOID.value == '11'
    assert x.index(1).StudyOID.value == "EX001"


def assert_case2(output_name):
    file_path = f"D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\{output_name}"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())
    x = p.odm.ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.first().Value
    assert x.first().value == '2200-10-01'
    query = p.odm.ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.find(
        ItemOID="VISDT").Query.find(OID='A529A2F2-F896-4AF7-AD4D-11B7110727BC')
    assert query.Value.value == 'Value 2200-10-01 is in the future, please correct'
    assert query.AuditRecord.first().DateTimeStamp.value == '2021-03-10T13:36:51.668-00:00'


def assert_case3(output_name):
    cdisc = PyODM.v2(f"D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\{output_name}")
    subject = cdisc.ClinicalData.first().SubjectData.first()
    item_group_data = subject.StudyEventData.first().ItemGroupData.find(ItemGroupOID="IG.HEMATOLOGY")
    item_group_data1 = item_group_data.ItemGroupData.index(0)
    assert item_group_data1.ItemGroupOID.value == "IG.WBC"
    item_data = item_group_data1.ItemData.find(ItemOID="IT.WBC")
    assert item_data.Value.first().value == '5.2'
    item_data = item_group_data1.ItemData.index(1)
    assert item_data.Value.first().value == '10*3/uL'
    item_group_data2 = item_group_data.ItemGroupData.find(ItemGroupOID="IT.RBC")
    assert item_group_data2.ItemGroupOID.value == "IT.RBC"
    item_data = item_group_data2.ItemData.first()
    assert item_data.IsNull.value == "Yes"


def assert_case4(output_name):
    # cdisc = PyODM.v2(f"D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\{output_name}")
    file_path = f"D:\\github\\pyodm\\src\\pyodm\\unit_tests\\test_cdisc_writer\\{output_name}"
    p = CdiscConfigReader(file_path=file_path, cdisc_class=CdiscClazz.v2())

    def clinical_data() -> Specification:
        return p.odm.ClinicalData

    subject = clinical_data().first().SubjectData.first()

    # subject = clinical_data().first().SubjectData.first
    assert subject.SubjectKey.value == '1001'
    # subject.StudyEventData.
    query = subject.StudyEventData.find(StudyEventOID="Visit1").ItemGroupData.first().ItemData.first().Query.array
    assert query[0].Value.value == "Value is in the future, please correct"
    for i in query[0].AuditRecord.array:
        print(i.ReasonForChange.value)
