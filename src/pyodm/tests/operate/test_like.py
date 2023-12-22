import pytest

from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdsic_xml_xsd_factory import CdiscXMLXsdFactory
from pyodm.utils.odm_utils import OdmUtils


@pytest.fixture
def test_data1():
    data_file = PathSource("data", "like", "test_data_like1.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


@pytest.fixture
def test_data2():
    data_file = PathSource("data", "like", "test_data_like2.xml")
    cdisc = CdiscXMLXsdFactory(data_file=data_file)
    return cdisc.odm()


def test_like(test_data1, test_data2):
    clinical_data_list1 = test_data1.ClinicalData.array
    clinical_data_list2 = test_data2.ClinicalData.array

    assert OdmUtils.like(clinical_data_list1[0], clinical_data_list2[0]) is True
    assert OdmUtils.like(clinical_data_list1[1], clinical_data_list2[1]) is True
    assert OdmUtils.like(clinical_data_list1[2], clinical_data_list2[2]) is False
    assert OdmUtils.like(clinical_data_list1[3], clinical_data_list2[3]) is True
