from pyodm.core.source.path_source import PathSource
from pyodm.factory.cdisc_xml_specification_factory import CdiscXMLSpecificationFactory

if __name__ == '__main__':
    # 数据 XML 文件的路径
    data_file = PathSource("odm_data.xml")
    # data_file 数据文件路径
    # specification_files 定义 Class 的配置
    cdisc = CdiscXMLSpecificationFactory(data_file=data_file)
    # 生成 ODM 对象
    odm = cdisc.odm()
    # Class 的定义文件可查看 README
    # ClinicalData is ManyElements
    # 所以无法直接调用属性，需获取其中一个元素 first 获取第一个元素
    # StudyOID 是 ClinicalData的属性
    print(odm.ClinicalData.first().StudyOID.value)
    # SiteRef is OneElement
    # 因为 SiteRef 是一个OneElement, 所以可以直接取元素属性
    print(odm.ClinicalData.first().SubjectData.first().SiteRef.LocationOID.value)

    # 查询 ItemGroupData 为 IG.HEMATOLOGY 下的 ItemGroupData 为 IG.WBC ItemData 为IT.WBC 的 Value的文本
    study_event_data = odm.ClinicalData.first().SubjectData.first().StudyEventData.first()
    # ItemGroupData 为 IG.HEMATOLOGY
    ig_hematology = study_event_data.ItemGroupData.find(ItemGroupOID="IG.HEMATOLOGY")
    # ItemGroupData 为 IG.WBC
    ig_wbc = ig_hematology.ItemGroupData.find(ItemGroupOID="IG.WBC")
    # ItemData 为IT.WBC
    it_wbc = ig_wbc.ItemData.find(ItemOID="IT.WBC")
    print(it_wbc.Value.first().value)