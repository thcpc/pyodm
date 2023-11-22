import pathlib

from cjen.nene.database_info import DataBaseInfo


from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter
from pyodm.factory.cdisc_listable_factory import CdiscListableFactory

from pyodm.unit_tests.test_listable_factory.subject_data_resource import SubjectDataResource
from pyodm.utils.path_utils import PathUtils


def xsd_files():
    base = PathUtils.folder("pyodm", __file__).joinpath("model", "v2", "resources", "schema")
    xsds = ["ODM-admindata.xsd", "ODM-clinicaldata.xsd", "ODM-foundation.xsd",
            "ODM-protocol.xsd", "ODM-referencedata.xsd", "ODM-study.xsd"]
    return [base.joinpath(xsd) for xsd in xsds]


if __name__ == '__main__':
    database_info = DataBaseInfo.factory(
        dict(host="dev-03.cluster-c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn", port=3306,
             user='root', pwd='8YTJWOuA7XRK17wRQnw4',
             database='eclinical_edc_dev_846'))
    data_source = SubjectDataResource(database_info)
    factory = CdiscListableFactory(data_source, xsd_files())

    odm_data = factory.odm()
    cw = CdiscXmlWriter(odm_data, pathlib.Path(f"result.xml"))
    cw.write()
