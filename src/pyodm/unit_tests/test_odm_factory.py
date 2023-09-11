from abc import ABC

from pyodmv2.odm import ODM, odm_factory
from pyodmv2.odm_source import ODMSource


class TestSource(ODMSource):
    def data(self) -> list[list[dict]]:
        return [
            [dict(id=1), dict(id=2), dict(id=5)],
            [dict(id=1), dict(id=3)],
            [dict(id=1), dict(id=4)]
        ]


class TestODM(ODM):
    ...


def test_odm_factory():
    test_data = odm_factory(TestODM, TestSource())
    assert test_data.odm.degree == 3
