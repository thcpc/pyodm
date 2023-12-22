from pathlib import Path

from pyodm.core.source.path_source import PathSource

from pyodm.core.data_loader.json_path_loader import JsonPathLoader
from pyodm.core.json.writer.json_writer import JSONWriter
from pyodm.factory.cdisc_json_factory import CdiscJSONFactory

if __name__ == '__main__':
    jf = CdiscJSONFactory(data_loader=JsonPathLoader(PathSource("submit-data2.json").read()),
                          configuration_files=[Path("eclinical-dataentry.xsd")])
    data = jf.factory(specified="submitData")
    jw = JSONWriter(Path("test.json"), data)
    jw.write()