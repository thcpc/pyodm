import pathlib

from cjen import MetaMysql
from pyodm.model.definition.mapper.assemble import CdiscSQL
from pyodm.utils.path_utils import PathUtils


@CdiscSQL(
    sql_path=PathUtils.folder("database", __file__).joinpath("sqls", "subjects.sql"),
    mapper_path=PathUtils.folder("database", __file__).joinpath("mappers", "mapper.xml"))
class SubjectMapper(MetaMysql): ...
