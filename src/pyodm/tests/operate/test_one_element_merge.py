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
def test_case1_data1():
    data_file = PathSource("data", "one_merge", "data1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_case1_data2():
    data_file = PathSource("data", "one_merge", "data2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_case1(test_case1_data1, test_case1_data2):

    base = test_case1_data1.as_stream().find(_lambda=Finder().element("ClinicalData").Lambda())
    base.merge("ClinicalData", test_case1_data2)
    out_put(test_case1_data1)
    site = test_case1_data1.as_stream().find(_lambda=Finder().element("SiteRef").Lambda()).get()
    assert site.LocationOID.get_value() == 'D001'

