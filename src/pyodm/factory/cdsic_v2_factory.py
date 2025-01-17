import os

from pyodm.core.source.path_source import PathSource

from pyodm.core.xml.reader.data.xml_v2_data_reader import XMLV2DataReader
from pyodm.factory.abstract_cdisc_xml_factory import AbstractCdiscXMLFactory

import pyodm.model.cdisc.classv2.element as Element
from pyodm.model import odm_xsd_description


class CdiscV2Factory(AbstractCdiscXMLFactory):

    def default_description_files(self) -> list:
        return odm_xsd_description()

    def __init__(self, data_file: PathSource, xsd_files: list = None):
        """
        :param data_file:  数据文件路径
        :type data_file: pathlib.Path
        :param xsd_files: XSD配置文件路径, 默认使用内置的 ODM 配置
        :type xsd_files: list[pathlib.Path]
        """
        super().__init__(data_file, xsd_files)
        self._xsd_files = xsd_files if xsd_files else self.default_description_files()

    def data_reader(self) -> XMLV2DataReader:
        """
        指定了解析 ODM XML Data 的数据方式
        :return:
        :rtype:
        """
        return XMLV2DataReader(self)

    def clazz_reader(self):
        """
        没有用动态加载的原因
        主要是为了避免如果以后需要用pyinstall打包的话,引用的第三包里如果动态加载,执行的话无法执行
        格式定义为 Class名:类型名的原因
        因为 Definition Attributes和 Element 都有
        :return:
        :rtype:
        """
        self.registry_cdisc('AbsoluteTimingConstraint:element', Element.AbsoluteTimingConstraint)
        self.registry_cdisc('Address:element', Element.Address)
        self.registry_cdisc('AdminData:element', Element.AdminData)
        self.registry_cdisc('Alias:element', Element.Alias)
        self.registry_cdisc('AnnotatedCRF:element', Element.AnnotatedCRF)
        self.registry_cdisc('Annotation:element', Element.Annotation)
        self.registry_cdisc('Arm:element', Element.Arm)
        self.registry_cdisc('Association:element', Element.Association)
        self.registry_cdisc('AuditRecord:element', Element.AuditRecord)
        self.registry_cdisc('Branching:element', Element.Branching)
        self.registry_cdisc('CDISCNotes:element', Element.CDISCNotes)
        self.registry_cdisc('CheckValue:element', Element.CheckValue)
        self.registry_cdisc('City:element', Element.City)
        self.registry_cdisc('Class:element', Element.Class)
        self.registry_cdisc('ClinicalData:element', Element.ClinicalData)
        self.registry_cdisc('Code:element', Element.Code)
        self.registry_cdisc('CodeList:element', Element.CodeList)
        self.registry_cdisc('CodeListItem:element', Element.CodeListItem)
        self.registry_cdisc('CodeListRef:element', Element.CodeListRef)
        self.registry_cdisc('Coding:element', Element.Coding)
        self.registry_cdisc('Comment:element', Element.Comment)
        self.registry_cdisc('CommentDef:element', Element.CommentDef)
        self.registry_cdisc('ConditionDef:element', Element.ConditionDef)
        self.registry_cdisc('Country:element', Element.Country)
        self.registry_cdisc('CRFCompletionInstructions:element', Element.CRFCompletionInstructions)
        self.registry_cdisc('Criterion:element', Element.Criterion)
        self.registry_cdisc('DateTimeStamp:element', Element.DateTimeStamp)
        self.registry_cdisc('Decode:element', Element.Decode)
        self.registry_cdisc('DefaultTransition:element', Element.DefaultTransition)
        self.registry_cdisc('Definition:element', Element.Definition)
        self.registry_cdisc('Description:element', Element.Description)
        self.registry_cdisc('DocumentRef:element', Element.DocumentRef)
        self.registry_cdisc('DurationTimingConstraint:element', Element.DurationTimingConstraint)
        self.registry_cdisc('Epoch:element', Element.Epoch)
        self.registry_cdisc('ErrorMessage:element', Element.ErrorMessage)
        self.registry_cdisc('ExclusionCriteria:element', Element.ExclusionCriteria)
        self.registry_cdisc('ExternalCodeLib:element', Element.ExternalCodeLib)
        self.registry_cdisc('FamilyName:element', Element.FamilyName)
        self.registry_cdisc('Flag:element', Element.Flag)
        self.registry_cdisc('FlagType:element', Element.FlagType)
        self.registry_cdisc('FlagValue:element', Element.FlagValue)
        self.registry_cdisc('FormalExpression:element', Element.FormalExpression)
        self.registry_cdisc('FullName:element', Element.FullName)
        self.registry_cdisc('GeoPosition:element', Element.GeoPosition)
        self.registry_cdisc('GivenName:element', Element.GivenName)
        self.registry_cdisc('HouseNumber:element', Element.HouseNumber)
        self.registry_cdisc('Image:element', Element.Image)
        self.registry_cdisc('ImplementationNotes:element', Element.ImplementationNotes)
        self.registry_cdisc('Include:element', Element.Include)
        self.registry_cdisc('InclusionCriteria:element', Element.InclusionCriteria)
        self.registry_cdisc('InclusionExclusionCriteria:element', Element.InclusionExclusionCriteria)
        self.registry_cdisc('IntercurrentEvent:element', Element.IntercurrentEvent)
        self.registry_cdisc('InvestigatorRef:element', Element.InvestigatorRef)
        self.registry_cdisc('ItemData:element', Element.ItemData)
        self.registry_cdisc('ItemDef:element', Element.ItemDef)
        self.registry_cdisc('ItemGroupData:element', Element.ItemGroupData)
        self.registry_cdisc('ItemGroupDef:element', Element.ItemGroupDef)
        self.registry_cdisc('ItemGroupRef:element', Element.ItemGroupRef)
        self.registry_cdisc('ItemRef:element', Element.ItemRef)
        self.registry_cdisc('KeySet:element', Element.KeySet)
        self.registry_cdisc('Leaf:element', Element.Leaf)
        self.registry_cdisc('LegalReason:element', Element.LegalReason)
        self.registry_cdisc('Location:element', Element.Location)
        self.registry_cdisc('LocationRef:element', Element.LocationRef)
        self.registry_cdisc('Meaning:element', Element.Meaning)
        self.registry_cdisc('MetaDataVersion:element', Element.MetaDataVersion)
        self.registry_cdisc('MetaDataVersionRef:element', Element.MetaDataVersionRef)
        self.registry_cdisc('MethodDef:element', Element.MethodDef)
        self.registry_cdisc('MethodSignature:element', Element.MethodSignature)
        self.registry_cdisc('ODM:element', Element.ODM)
        self.registry_cdisc('Organization:element', Element.Organization)
        self.registry_cdisc('Origin:element', Element.Origin)
        self.registry_cdisc('OtherText:element', Element.OtherText)
        self.registry_cdisc('Parameter:element', Element.Parameter)
        self.registry_cdisc('ParameterValue:element', Element.ParameterValue)
        self.registry_cdisc('PDFPageRef:element', Element.PDFPageRef)
        self.registry_cdisc('PostalCode:element', Element.PostalCode)
        self.registry_cdisc('Prefix:element', Element.Prefix)
        self.registry_cdisc('Prompt:element', Element.Prompt)
        self.registry_cdisc('Protocol:element', Element.Protocol)
        self.registry_cdisc('Query:element', Element.Query)
        self.registry_cdisc('Question:element', Element.Question)
        self.registry_cdisc('RangeCheck:element', Element.RangeCheck)
        self.registry_cdisc('ReasonForChange:element', Element.ReasonForChange)
        self.registry_cdisc('ReferenceData:element', Element.ReferenceData)
        self.registry_cdisc('RelativeTimingConstraint:element', Element.RelativeTimingConstraint)
        self.registry_cdisc('Resource:element', Element.Resource)
        self.registry_cdisc('ReturnValue:element', Element.ReturnValue)
        self.registry_cdisc('Selection:element', Element.Selection)
        self.registry_cdisc('Signature:element', Element.Signature)
        self.registry_cdisc('SignatureDef:element', Element.SignatureDef)
        self.registry_cdisc('SignatureRef:element', Element.SignatureRef)
        self.registry_cdisc('SiteRef:element', Element.SiteRef)
        self.registry_cdisc('SourceID:element', Element.SourceID)
        self.registry_cdisc('SourceItem:element', Element.SourceItem)
        self.registry_cdisc('SourceItems:element', Element.SourceItems)
        self.registry_cdisc('Standard:element', Element.Standard)
        self.registry_cdisc('Standards:element', Element.Standards)
        self.registry_cdisc('StateProv:element', Element.StateProv)
        self.registry_cdisc('StreetName:element', Element.StreetName)
        self.registry_cdisc('Study:element', Element.Study)
        self.registry_cdisc('StudyEndPoint:element', Element.StudyEndPoint)
        self.registry_cdisc('StudyEndPointRef:element', Element.StudyEndPointRef)
        self.registry_cdisc('StudyEndPoints:element', Element.StudyEndPoints)
        self.registry_cdisc('StudyEstimand:element', Element.StudyEstimand)
        self.registry_cdisc('StudyEstimands:element', Element.StudyEstimands)
        self.registry_cdisc('StudyEventData:element', Element.StudyEventData)
        self.registry_cdisc('StudyEventDef:element', Element.StudyEventDef)
        self.registry_cdisc('StudyEventGroupDef:element', Element.StudyEventGroupDef)
        self.registry_cdisc('StudyEventGroupRef:element', Element.StudyEventGroupRef)
        self.registry_cdisc('StudyEventRef:element', Element.StudyEventRef)
        self.registry_cdisc('StudyIndication:element', Element.StudyIndication)
        self.registry_cdisc('StudyIndications:element', Element.StudyIndications)
        self.registry_cdisc('StudyIntervention:element', Element.StudyIntervention)
        self.registry_cdisc('StudyInterventionRef:element', Element.StudyInterventionRef)
        self.registry_cdisc('StudyInterventions:element', Element.StudyInterventions)
        self.registry_cdisc('StudyObjective:element', Element.StudyObjective)
        self.registry_cdisc('StudyObjectives:element', Element.StudyObjectives)
        self.registry_cdisc('StudyParameter:element', Element.StudyParameter)
        self.registry_cdisc('StudyStructure:element', Element.StudyStructure)
        self.registry_cdisc('StudySummary:element', Element.StudySummary)
        self.registry_cdisc('StudyTargetPopulation:element', Element.StudyTargetPopulation)
        self.registry_cdisc('StudyTargetPopulationRef:element', Element.StudyTargetPopulationRef)
        self.registry_cdisc('StudyTiming:element', Element.StudyTiming)
        self.registry_cdisc('StudyTimings:element', Element.StudyTimings)
        self.registry_cdisc('SubClass:element', Element.SubClass)
        self.registry_cdisc('SubjectData:element', Element.SubjectData)
        self.registry_cdisc('Suffix:element', Element.Suffix)
        self.registry_cdisc('SummaryMeasure:element', Element.SummaryMeasure)
        self.registry_cdisc('SupplementalDoc:element', Element.SupplementalDoc)
        self.registry_cdisc('TargetTransition:element', Element.TargetTransition)
        self.registry_cdisc('Telecom:element', Element.Telecom)
        self.registry_cdisc('Title:element', Element.Title)
        self.registry_cdisc('Transition:element', Element.Transition)
        self.registry_cdisc('TransitionTimingConstraint:element', Element.TransitionTimingConstraint)
        self.registry_cdisc('TranslatedText:element', Element.TranslatedText)
        self.registry_cdisc('TrialPhase:element', Element.TrialPhase)
        self.registry_cdisc('User:element', Element.User)
        self.registry_cdisc('UserName:element', Element.UserName)
        self.registry_cdisc('UserRef:element', Element.UserRef)
        self.registry_cdisc('Value:element', Element.Value)
        self.registry_cdisc('ValueListDef:element', Element.ValueListDef)
        self.registry_cdisc('ValueListRef:element', Element.ValueListRef)
        self.registry_cdisc('WhereClauseDef:element', Element.WhereClauseDef)
        self.registry_cdisc('WhereClauseRef:element', Element.WhereClauseRef)
        self.registry_cdisc('WorkflowDef:element', Element.WorkflowDef)
        self.registry_cdisc('WorkflowEnd:element', Element.WorkflowEnd)
        self.registry_cdisc('WorkflowRef:element', Element.WorkflowRef)
        self.registry_cdisc('WorkflowStart:element', Element.WorkflowStart)


if __name__ == '__main__':

    for f in os.listdir("D:\\github\\pyodm\\src\\pyodm\\model\\cdisc\\classv2\\element"):
        name = f.replace(".py", "")
        print(f"self.registry_cdisc('{name}:element', Element.{name})")
        # print(f"from pyodm.model.cdisc.classv2.element.{name} import {name}")
