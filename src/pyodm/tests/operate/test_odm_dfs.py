import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.utils.search.odm_dfs import ODMDfs


@pytest.fixture
def test_data():
    data_file = PathSource("data", "test_data.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_data2():
    data_file = PathSource("data", "test_data.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_odm_dfs(test_data):
    dfs = ODMDfs(test_data)
    data = dfs.find(_lambda=lambda x: x.get_name() == 'ItemData' and x.ItemOID.get_value() == "SVDAT")
    print(data.Value.array[0].get_value())
