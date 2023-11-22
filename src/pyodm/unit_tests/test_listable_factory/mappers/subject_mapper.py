from cjen import MetaMysql

from pyodm.unit_tests.sql_to_odm.cdisc import CdiscSQL

from pyodm.utils.path_utils import PathUtils

path = PathUtils.folder("pyodm", __file__)


@CdiscSQL(
    sql_path=path.joinpath("unit_tests", "test_listable_factory", "sqls", "subjects.sql"),
    mapper_path=path.joinpath("unit_tests", "test_listable_factory", "mappers", "mapper.xml"))
class SubjectMapper(MetaMysql): ...
