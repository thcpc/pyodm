from abc import ABC

from cjen.db_bigtangerine import DBBigTangerine

from pyodm.core.support.abstract_resource import AbstractResource


class DataBaseResource(DBBigTangerine, AbstractResource, ABC):

    def __init__(self, database_info):
        super().__init__(database_info)
