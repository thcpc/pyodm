from pathlib import Path

import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.model.v2.cdisc.ItemGroupData import ItemGroupData
from pyodm.model.v2.cdisc.Value import Value
from pyodm.utils.stream import Stream


@pytest.fixture
def test_data():
    data_file = PathSource("data", "test_data.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def out_put(data):
    cw = CdiscXmlWriter(data, out_put=Path("test.xml"))
    cw.write()





def test_stream_update(test_data):
    stream = Stream(test_data)
    optional = stream.find(_lambda=lambda x: x.get_name() == 'SubjectData' and x.SubjectKey.get_value() == 'D001001')
    optional.update(SubjectKey="9999999")
    assert test_data.SubjectData.array[0].SubjectKey.get_value() == "9999999"
    out_put(test_data)


def test_stream_update_text(test_data):
    stream = Stream(test_data)
    optional = stream.find(_lambda=lambda x: x.get_name() == 'SubjectData' and x.SubjectKey.get_value() == 'D001001') \
        .find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupOID.get_value() == 'HeaderLog' and x.ItemGroupRepeatKey.get_value() == "0") \
        .find(_lambda=lambda x: x.get_name() == 'Value' and x.SeqNum.get_value() == '683')
    optional.update_text("990099")
    out_put(test_data)


@pytest.fixture()
def new_value1():
    value = Value()
    value.set_name("Value")
    value.SeqNum.set_name("SeqNum")
    value.SeqNum.set_value("888777")
    value.set_value("XXXXX")
    return value


@pytest.fixture()
def new_value_by_xml():
    data_file = PathSource("data", "ItemData.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_stream_append(test_data, new_value1, new_value_by_xml):
    stream = Stream(test_data)
    optional = stream.find(_lambda=lambda x: x.get_name() == 'ItemData' and x.ItemOID.get_value() == "SVDAT")
    optional.append("Value", new_value1)
    out_put(test_data)

    stream = Stream(test_data)
    # stream.find(test_data)
    item_group_data = stream.find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupRepeatKey.get_value() == '0' and x.ItemGroupOID.get_value() == 'Enrollment')
    item_group_data.append("ItemData", new_value_by_xml)
    out_put(test_data)


@pytest.fixture()
def data_of_attribute1():
    value = ItemGroupData()
    value.set_name("ItemGroupData")
    value.TransactionType.set_name("TransactionType")
    value.TransactionType.set_value("EN")
    value.ItemGroupDataSeq.set_name("ItemGroupDataSeq")
    value.ItemGroupDataSeq.set_value("10000000")
    return value


@pytest.fixture()
def data_of_attribute2():
    value = ItemGroupData()
    value.set_name("ItemGroupData")
    value.ItemGroupOID.set_name("ItemGroupOID")
    value.ItemGroupOID.set_value("ItemGroupOID99999")
    value.TransactionType.set_name("TransactionType")
    value.TransactionType.set_value("EN")
    value.ItemGroupDataSeq.set_name("ItemGroupDataSeq")
    value.ItemGroupDataSeq.set_value("10000000")
    return value


def test_stream_merge_attribute1(test_data, data_of_attribute1):
    """
    Merge 属性： 合并时，原有属性不存在的值会被 合并对象更新
    """
    item_group_data = test_data.as_stream().find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupRepeatKey.get_value() == '0' and x.ItemGroupOID.get_value() == 'Enrollment')

    item_group_data.merge(data_of_attribute1)
    x = test_data.as_stream().find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupRepeatKey.get_value() == '0' and x.ItemGroupOID.get_value() == 'Enrollment').get()

    assert x.ItemGroupDataSeq.get_value() == "10000000"
    assert x.TransactionType.get_value() == "EN"

    out_put(test_data)


def test_stream_merge_attribute2(test_data, data_of_attribute2):
    """
    Merge 属性： 合并时，原有已存在的属性值不会被合并对象
    """
    item_group_data = Stream(test_data).find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupRepeatKey.get_value() == '0' and x.ItemGroupOID.get_value() == 'Enrollment')

    item_group_data.merge(data_of_attribute2)
    x = Stream(test_data).find(_lambda=lambda
        x: x.get_name() == 'ItemGroupData' and x.ItemGroupRepeatKey.get_value() == '0' and x.ItemGroupOID.get_value() == 'Enrollment').get()
    assert x.ItemGroupOID.get_value() == "Enrollment"
    assert x.ItemGroupDataSeq.get_value() == "10000000"
    assert x.TransactionType.get_value() == "EN"

    out_put(test_data)



