
from pyodm.core.support.abstract_resource import AbstractResource
from pyodm.utils.forest import Forest


class ForestResource(AbstractResource):

    def __init__(self, data_source: AbstractResource):
        self._data_source = data_source

    def load(self):
        return Forest.transform(self._data_source.load())
