from pathlib import Path

import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.utils.finder import Finder


def out_put(data):
    cw = CdiscXmlWriter(data, out_put=Path("test.xml"))
    cw.write()


@pytest.fixture
def test_data1():
    data_file = PathSource("data", "add", "data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_data2():
    data_file = PathSource("data", "add", "data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_add(test_data1, test_data2):
    finder = Finder().element("SubjectData").attribute(SubjectKey="D001002").Lambda()
    base = test_data1.as_stream().find(_lambda=finder)
    base.add(test_data2)
    out_put(test_data1)
    assert test_data1.as_stream().find(_lambda=finder).get().SiteRef.LocationOID.get_value() == "D001"
