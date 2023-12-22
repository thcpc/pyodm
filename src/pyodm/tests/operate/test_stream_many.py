from pathlib import Path

import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.utils.finder import Finder


def out_put(data):
    cw = CdiscXmlWriter(data, out_put=Path("test.xml"))
    cw.write()


"""
================Test case 1 =================
针对 Element 的是否还会增加还是更新
"""


@pytest.fixture
def test_case1_data1():
    data_file = PathSource("data", "stream_many", "test_case1_data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_case1_data2():
    data_file = PathSource("data", "stream_many", "test_case1_data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_stream_merge_many(test_case1_data1, test_case1_data2):
    """
    合并 Many
    test_data_many2 中有的 ClinicalData, 判断为相似的属性 会更新 test_data_many1
    test_data_many2 中有的 ClinicalData, 如果 test_data_many1 没有，会添加入 test_data_many1 中的 ClinicalData

    """
    base = test_case1_data1.as_stream().find(_lambda=lambda x: x.get_name() == "ODM")
    base.merge("ODM", test_case1_data2)
    out_put(test_case1_data1)
    assert test_case1_data1.ClinicalData.array[0].StudyOID.get_value() == "11"
    assert test_case1_data1.ClinicalData.array[0].MetaDataVersionOID.get_value() == "11"

    assert test_case1_data1.ClinicalData.array[1].StudyOID.get_value() == "EX001"
    assert test_case1_data1.ClinicalData.array[1].MetaDataVersionOID.get_value() == "1010"

    assert test_case1_data1.ClinicalData.array[2].StudyOID.get_value() == "2222"
    assert test_case1_data1.ClinicalData.array[2].MetaDataVersionOID.get_value() == "1010"

    assert test_case1_data1.ClinicalData.array[3].StudyOID.get_value() == "3333"
    assert test_case1_data1.ClinicalData.array[3].MetaDataVersionOID.get_value() == "9999999"

    assert test_case1_data1.ClinicalData.array[4].StudyOID.get_value() == "4444"
    assert test_case1_data1.ClinicalData.array[4].MetaDataVersionOID.get_value() == "10102"

    assert test_case1_data1.ClinicalData.array[5].StudyOID.get_value() == "4444"
    assert test_case1_data1.ClinicalData.array[5].MetaDataVersionOID.get_value() == "10101"

    assert test_case1_data1.ClinicalData.array[6].StudyOID.get_value() == "5555"
    assert test_case1_data1.ClinicalData.array[6].MetaDataVersionOID.get_value() == "10102"
    assert len(test_case1_data1.ClinicalData.array) == 7


"""
================Test case 2 =================
针对 Attribute 的更新
"""


@pytest.fixture
def test_case2_data1():
    data_file = PathSource("data", "stream_many", "test_case2_data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_case2_data2():
    data_file = PathSource("data", "stream_many", "test_case2_data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_case2(test_case2_data1, test_case2_data2):
    base = test_case2_data1.as_stream().find(_lambda=lambda x: x.get_name() == "ODM")
    base.merge("ClinicalData", test_case2_data2)
    item_data = test_case2_data1.as_stream() \
        .find(_lambda=lambda x: x.get_name() == 'SubjectData' and x.SubjectKey.get_value() == 'D001001') \
        .find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupOID.get_value() == 'HeaderLog' and x.ItemGroupRepeatKey.get_value() == "0") \
        .find(_lambda=lambda x: x.get_name() == "ItemData" and x.ItemOID.get_value() == "SVDAT").get()

    assert item_data.Value.array[0].SeqNum.get_value() == "683"
    assert item_data.Value.array[1].SeqNum.get_value() == "684"

    subject_lambda = lambda x: x.get_name() == 'SubjectData' and x.SubjectKey.get_value() == 'D001002'
    item_lambda = lambda x: x.get_name() == 'ItemData' and x.ItemOID.get_value() == 'SVDAT'

    item_data = test_case2_data1.as_stream().find(subject_lambda).find(item_lambda).get()
    assert item_data.Value.array[0].SeqNum.get_value() == '685'
    assert item_data.Value.array[0].get_value() == '685'

    out_put(test_case2_data1)


"""
====== Test Case 3 =======
针对 Element 中的 Text 更新
"""


@pytest.fixture
def test_case3_data1():
    data_file = PathSource("data", "stream_many", "test_case3_data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_case3_data2():
    data_file = PathSource("data", "stream_many", "test_case3_data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_case3(test_case3_data1, test_case3_data2):
    base = test_case3_data1.as_stream().find(_lambda=lambda x: x.get_name() == "ODM")
    base.merge("ClinicalData", test_case3_data2)
    find_lambda = lambda element: element.get_name() == "Query" and element.OID.get_value() == "111"
    query = test_case3_data1.as_stream().find(_lambda=find_lambda).get()
    assert query.Value.get_value() == "Value 2200-10-01 "
    assert query.AuditRecord.array[0].DateTimeStamp.get_value() == "2021-03-10T"
    out_put(test_case3_data1)


"""
========== Test Case 4 ======
测试有元素嵌套的情况
IT.WBC 的 Value 值应该更新到 test_case4_data1
IT.WBC1 ItemGroupData 应该新增到 test_case4_data2
"""


@pytest.fixture
def test_case4_data1():
    data_file = PathSource("data", "stream_many", "test_case4_data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_case4_data2():
    data_file = PathSource("data", "stream_many", "test_case4_data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_case4(test_case4_data1, test_case4_data2):
    base = test_case4_data1.as_stream().find(_lambda=lambda x: x.get_name() == "ODM")
    base.merge("ItemGroupData", test_case4_data2)
    itemgroup_lamda = Finder().element(name="ItemGroupData").attribute(ItemGroupOID="IG.WBC").Lambda()
    item_lambda = Finder().element(name="ItemData").attribute(ItemOID="IT.WBC").Lambda()
    item_data = test_case4_data1.as_stream().find(_lambda=itemgroup_lamda).find(_lambda=item_lambda).get()
    assert item_data.Value.array[0].get_value() == "5.3"
    item_lambda = Finder().element(name="ItemData").attribute(ItemOID="IT.WBC_UNITS").Lambda()
    item_data = test_case4_data1.as_stream().find(_lambda=itemgroup_lamda).find(_lambda=item_lambda).get()
    assert item_data.Value.array[0].get_value() == "10*4/uL"
    out_put(test_case4_data1)
