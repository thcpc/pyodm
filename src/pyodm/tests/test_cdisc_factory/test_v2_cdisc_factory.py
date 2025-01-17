import pathlib

import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.core.xml.writer.cdisc_v_xml_writer import CdiscVXmlWriter
from pyodm.factory.cdsic_v2_factory import CdiscV2Factory
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.tests.test_cdisc_factory.common_assert import assert_case1, assert_case2, assert_case4, assert_case5, \
    assert_case6
from pyodm.utils.path_utils import PathUtils


@pytest.fixture
def xsd_files():
    base = PathUtils.folder("pyodm", __file__).joinpath("model", "v2", "resources", "schema")
    xsds = ["ODM-admindata.xsd", "ODM-clinicaldata.xsd", "ODM-foundation.xsd",
            "ODM-protocol.xsd", "ODM-referencedata.xsd", "ODM-study.xsd"]
    return [base.joinpath(xsd) for xsd in xsds]


def test_case1(xsd_files):
    xsd_file = [xsd_files[0]]
    data_file = PathSource("resources", "data", "user.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_file)
    assert_case1(cdisc)

def test_case2(xsd_files):
    data_file = PathSource("resources", "data", "odm_template.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_files)
    x = cdisc.odm().ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.first().Value
    assert x.first().get_value() == '2200-10-01'
    query = cdisc.odm().ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.find().Query.find()
    assert query.Value.first().get_value() == 'Value 2200-10-01 is in the future, please correct'
    assert query.AuditRecord.first().DateTimeStamp.get_value() == '2021-03-10T13:36:51.668-00:00'
    cw = CdiscVXmlWriter(cdisc.odm(), out_put=pathlib.Path("vtestcase2.xml"))
    cw.write()



def test_case3(xsd_files):
    data_file = PathSource("resources", "data", "test_case2.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_files)
    x = cdisc.odm().ClinicalData
    assert x.first().StudyOID.get_value() == '11'
    assert x.index(1).StudyOID.get_value() == "EX001"
    cw = CdiscVXmlWriter(cdisc.odm(), out_put=pathlib.Path("vtestcase3.xml"))
    cw.write()


def test_case4(xsd_files):
    data_file = PathSource("resources", "data", "transaction_history.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_files)
    subject = cdisc.odm().ClinicalData.first().SubjectData.first()
    assert subject.SubjectKey.get_value() == '1001'
    query = subject.StudyEventData.find().ItemGroupData.first().ItemData.first().Query._array
    assert query[0].Value.first().get_value() == "Value is in the future, please correct"
    for i in query[0].AuditRecord._array:
        print(i.ReasonForChange.get_value())
    cw = CdiscVXmlWriter(cdisc.odm(), out_put=pathlib.Path("vtestcase4.xml"))
    cw.write()


def test_case5(xsd_files):
    data_file = PathSource("resources", "data", "transaction_history.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_files)
    cdisc.odm().ClinicalData.usage(lambda x: print(x.first().StudyOID.get_value()))


def test_case6(xsd_files):
    data_file = PathSource("resources", "data", "odm_testcase5.xml")
    cdisc = CdiscV2Factory(data_file=data_file, xsd_files=xsd_files)
    subject = cdisc.odm().ClinicalData.first().SubjectData.first()
    item_group_data = subject.StudyEventData.first().ItemGroupData.find(ItemGroupOID="IG.HEMATOLOGY")
    item_group_data1 = item_group_data.ItemGroupData.index(0)
    assert item_group_data1.ItemGroupOID.get_value() == "IG.WBC"
    item_data = item_group_data1.ItemData.find(ItemOID="IT.WBC")
    assert item_data.Value.first().get_value() == '5.2'
    item_data = item_group_data1.ItemData.index(1)
    assert item_data.Value.first().get_value() == '10*3/uL'
    item_group_data2 = item_group_data.ItemGroupData.find(ItemGroupOID="IT.RBC")
    assert item_group_data2.ItemGroupOID.get_value() == "IT.RBC"
    item_data = item_group_data2.ItemData.first()
    assert item_data.IsNull.get_value() == "Yes"
    cw = CdiscVXmlWriter(cdisc.odm(), out_put=pathlib.Path("vtestcase6.xml"))
    cw.write()