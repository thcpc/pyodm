import pathlib

import pytest

from pyodm.factory.cdsic_xsd_factory import CdiscXsdFactory
from pyodm.unit_tests.test_cdisc_factory.common_assert import assert_case1, assert_case2, \
    assert_case3, assert_case4, assert_case5, assert_case6


def project_path(current):
    path = pathlib.Path(current).parent
    while path.name != "pyodm":
        path = path.parent
    return path


@pytest.fixture
def xsd_files():
    base = project_path(__file__).joinpath("model", "v2", "resources", "schema")
    xsds = ["ODM-admindata.xsd", "ODM-clinicaldata.xsd", "ODM-foundation.xsd",
            "ODM-protocol.xsd", "ODM-referencedata.xsd", "ODM-study.xsd"]
    return [base.joinpath(xsd) for xsd in xsds]


def test_case1(xsd_files):
    xsd_file = [xsd_files[0]]
    data_file = pathlib.Path("resources").joinpath("data", "user.xml")
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_file)
    assert_case1(cdisc)


def test_case2(xsd_files):
    data_file = pathlib.Path("resources").joinpath(pathlib.Path("data"), pathlib.Path("odm_template.xml"))
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_files)
    assert_case2(cdisc)


def test_case3(xsd_files):
    data_file = pathlib.Path("resources").joinpath("data", "test_case2.xml")
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_files)
    assert_case3(cdisc)


def test_case4(xsd_files):
    data_file = pathlib.Path("resources").joinpath("data", "transaction_history.xml")
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_files)
    assert_case4(cdisc)


def test_case5(xsd_files):
    data_file = pathlib.Path("resources").joinpath("data", "transaction_history.xml")
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_files)
    assert_case5(cdisc)


def test_case6(xsd_files):
    data_file = pathlib.Path("resources").joinpath("data", "odm_testcase5.xml")
    cdisc = CdiscXsdFactory(data_file=data_file, xsd_files=xsd_files)
    assert_case6(cdisc)
