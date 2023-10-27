import pathlib

import pytest

from pyodm.factory.cdisc_specification_factory import CdiscSpecificationFactory
from pyodm.unit_tests.test_cdisc_factory.common_assert import assert_case2, assert_case6, assert_case5, assert_case4, \
    assert_case3


@pytest.fixture
def specification_file():
    return "D:\\github\\pyodm\\src\\pyodm\\resources\\SpecificationV2.xml"


def test_case2(specification_file):
    data_file = pathlib.Path("resources").joinpath(pathlib.Path("data"), pathlib.Path("odm_template.xml"))
    cdisc = CdiscSpecificationFactory(data_file=data_file, specification_files=[specification_file])
    assert_case2(cdisc)


def test_case3(specification_file):
    data_file = pathlib.Path("resources").joinpath("data", "test_case2.xml")
    cdisc = CdiscSpecificationFactory(data_file=data_file, specification_files=[specification_file])
    assert_case3(cdisc)


def test_case4(specification_file):
    data_file = pathlib.Path("resources").joinpath("data", "transaction_history.xml")
    cdisc = CdiscSpecificationFactory(data_file=data_file, specification_files=[specification_file])
    assert_case4(cdisc)


def test_case5(specification_file):
    data_file = pathlib.Path("resources").joinpath("data", "transaction_history.xml")
    cdisc = CdiscSpecificationFactory(data_file=data_file, specification_files=[specification_file])
    assert_case5(cdisc)


def test_case6(specification_file):
    data_file = pathlib.Path("resources").joinpath("data", "odm_testcase5.xml")
    cdisc = CdiscSpecificationFactory(data_file=data_file, specification_files=[specification_file])
    assert_case6(cdisc)
