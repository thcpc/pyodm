import pathlib

import xmlschema

ODM_SCHEMA_XSD = pathlib.Path().joinpath(
    pathlib.Path(__file__).absolute().parent,
    "resources", "odm", "schema")


def xsd(file: str):
    def __wrapper__(func):
        def __inner__(cls, xml_file):
            xsd_file = pathlib.Path().joinpath(ODM_SCHEMA_XSD, file)
            try:

                schema_xsd = xmlschema.XMLSchema(xsd_file)
                schema_xsd.validate(xml_file)
            except xmlschema.XMLSchemaException as e:
                raise e
            return True
        return __inner__

    return __wrapper__


class ODMValidator:

    @classmethod
    @xsd(file="xml.xsd")
    def xml(cls, xml_file: str): ...

    @classmethod
    @xsd(file="ODM.xsd")
    def odm(cls, xml_file: str): ...

    @classmethod
    @xsd(file="ODM-admindata.xsd")
    def admindata(cls, xml_file: str): ...

    @classmethod
    @xsd(file="ODM-clinicaldata.xsd")
    def clinicaldata(cls, xml_file: str): ...
