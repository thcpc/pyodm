import pathlib
from abc import ABC

from pyodm.core.support.abstract_resource import AbstractResource


class AbstractPathResource(AbstractResource, ABC):
    def __init__(self, file: pathlib.Path):
        self.file = file
