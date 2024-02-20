# -*- coding: utf-8 -*-

import zeep

# Generovaní tiskových sestav
class Reports(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Reports.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Reports.asmx?wsdl')

    # Tisková sestava: Export jednotek
    def ExportUnit(self, ID_Login, ID, ID_UnitFilter, FileFormat=None):
        return self._client.service.ExportUnit({"ID_Login": ID_Login, "ID": ID, "ID_UnitFilter": ID_UnitFilter, "FileFormat": FileFormat})

    # Tisková sestava: Přehled účastníků tábora
    def ParticipantCampExcel(self, ID_Login, ID_EventCamp):
        return self._client.service.ParticipantCampExcel({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp})

    # Tisková sestava: Přehled žádostí o dotaci pro OJ
    def GrantHeadquartersUniversal(self, ID_Login, Year, Format, ID_GrantState=None):
        return self._client.service.GrantHeadquartersUniversal({"ID_Login": ID_Login, "Year": Year, "Format": Format, "ID_GrantState": ID_GrantState})

    # Tisková sestava: Přehled účastníků vzdělávací akce
    def ParticipantEducationFeeExcel(self, ID_Login, ID_EventEducation, ID_EventEducationCourse, IsActive):
        return self._client.service.ParticipantEducationFeeExcel({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "IsActive": IsActive})

    # Tisková sestava: Registrované osoby
    def UnitRegistrationPersons(self, ID_Login, ID, FileFormat, IncludeChild):
        return self._client.service.UnitRegistrationPersons({"ID_Login": ID_Login, "ID": ID, "FileFormat": FileFormat, "IncludeChild": IncludeChild})

    # Tisková sestava: Ručně generované dekrety
    def EventEducationLetterIssueAllZIP(self, ID_Login, ID_Items=None):
        return self._client.service.EventEducationLetterIssueAllZIP({"ID_Login": ID_Login, "ID_Items": ID_Items})

    # Tisková sestava: Ručně generované dekrety a absolventské listy
    def EventEducationLetterIssueAll(self, ID_Login, ID_Items=None):
        return self._client.service.EventEducationLetterIssueAll({"ID_Login": ID_Login, "ID_Items": ID_Items})

    # Tisková sestava: Přehled plateb záloh žádostí o dotace
    def GrantAdvancePaymentList(self, ID_Login, Year, DaysAhead, ID_GrantType=None, ID_State=None):
        return self._client.service.GrantAdvancePaymentList({"ID_Login": ID_Login, "Year": Year, "DaysAhead": DaysAhead, "ID_GrantType": ID_GrantType, "ID_State": ID_State})

    # Tisková sestava: Přehled žádostí o dotaci pro OJ
    def GrantHeadquartersUnorganizedYouth(self, ID_Login, Year, Format, ID_GrantState=None):
        return self._client.service.GrantHeadquartersUnorganizedYouth({"ID_Login": ID_Login, "Year": Year, "Format": Format, "ID_GrantState": ID_GrantState})

    # Tisková sestava: Přehled žádostí o dotaci pro OJ
    def GrantHeadquartersBuilding(self, ID_Login, Year, Format, ID_GrantState=None):
        return self._client.service.GrantHeadquartersBuilding({"ID_Login": ID_Login, "Year": Year, "Format": Format, "ID_GrantState": ID_GrantState})

    # Tisková sestava: Hospodářský výkaz
    def StatementDetail(self, ID_Login, ID, ShowOverview, FileFormat=None):
        return self._client.service.StatementDetail({"ID_Login": ID_Login, "ID": ID, "ShowOverview": ShowOverview, "FileFormat": FileFormat})

    # Tisková sestava: Dekrety a absolventské listy
    def EventEducationLetterAllWithAttachmenZIP(self, ID_Login, IsParticipantEducation, ID_Items=None):
        return self._client.service.EventEducationLetterAllWithAttachmenZIP({"ID_Login": ID_Login, "IsParticipantEducation": IsParticipantEducation, "ID_Items": ID_Items})

    # Tisková sestava: Příloha k vůdcovskému dekretu
    def EventEducationLetterAllAttachment(self, ID_Login, IsParticipantEducation, ExportAttachments, ID_Items=None):
        return self._client.service.EventEducationLetterAllAttachment({"ID_Login": ID_Login, "IsParticipantEducation": IsParticipantEducation, "ExportAttachments": ExportAttachments, "ID_Items": ID_Items})

    # Tisková sestava: Dekrety a absolventské listy
    def EventEducationLetterAll(self, ID_Login, IsParticipantEducation, ID_Items=None):
        return self._client.service.EventEducationLetterAll({"ID_Login": ID_Login, "IsParticipantEducation": IsParticipantEducation, "ID_Items": ID_Items})

    # Tisková sestava: Šablona souhlasu kandidáta sněmu se zápisem do spolkového rejstříku
    def CandidateFunctionAgreementDetail(self, ID_Login, ID):
        return self._client.service.CandidateFunctionAgreementDetail({"ID_Login": ID_Login, "ID": ID})

    # Tisková sestava: Šablona souhlasu se zápisem do spolkového rejstříku
    def FunctionAgreementDetail(self, ID_Login, ID):
        return self._client.service.FunctionAgreementDetail({"ID_Login": ID_Login, "ID": ID})

    # Tisková sestava: Přehled dotovaných vzdělávacích akcí
    def GrantOverview(self, ID_Login, Year, Person=None):
        return self._client.service.GrantOverview({"ID_Login": ID_Login, "Year": Year, "Person": Person})

    # Tisková sestava: Přehled žádostí o dotaci pro OJ
    def GrantHeadquarters(self, ID_Login, Year, Format, ID_GrantType=None):
        return self._client.service.GrantHeadquarters({"ID_Login": ID_Login, "Year": Year, "Format": Format, "ID_GrantType": ID_GrantType})

    # Přehled nových kvalifikací
    def QualificationAllNewSummary(self, ID_Login, From, To, ID_QualificationTypeList=None):
        return self._client.service.QualificationAllNewSummary({"ID_Login": ID_Login, "From": From, "To": To, "ID_QualificationTypeList": ID_QualificationTypeList})

    # Tisková sestava: Přehled žádostí o dotaci pro OJ
    def GrantUnitSummary(self, ID_Login, ID_Unit, Year, Format):
        return self._client.service.GrantUnitSummary({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "Year": Year, "Format": Format})

    # Tisková sestava: Přehled účastníků vzdělávací akce
    def ParticipantEducationExcel(self, ID_Login, ID_EventEducation, ID_EventEducationCourse, IsActive):
        return self._client.service.ParticipantEducationExcel({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "IsActive": IsActive})

    # Tisková sestava: Vzdělávací akce export
    def EventEducationExportExcel(self, ID_Login, ID, ID_EventEducationType, FileFormat, ID_EventEducationGroup=None, DisplayNameFilter=None):
        return self._client.service.EventEducationExportExcel({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "FileFormat": FileFormat, "ID_EventEducationGroup": ID_EventEducationGroup, "DisplayNameFilter": DisplayNameFilter})

    # Tisková sestava: Vzdělávací akce export
    def EventEducationExport(self, ID_Login, ID, ID_EventEducationType, FileFormat, ID_EventEducationGroup=None, DisplayNameFilter=None):
        return self._client.service.EventEducationExport({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "FileFormat": FileFormat, "ID_EventEducationGroup": ID_EventEducationGroup, "DisplayNameFilter": DisplayNameFilter})

    # Tisková sestava: Členská karty
    def MemberCardDetail(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardDetail({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Tisková sestava: Detail 2F pro uživatele
    def UserDetailTwoFactor(self, ID_Login, ID):
        return self._client.service.UserDetailTwoFactor({"ID_Login": ID_Login, "ID": ID})

    # Tisková sestava: Kód
    def Code(self, ID_Login, ID, BarcodeHeight, ID_Table=None, ID_Column=None, BarcodeType=None, FileName=None, Text=None):
        return self._client.service.Code({"ID_Login": ID_Login, "ID": ID, "BarcodeHeight": BarcodeHeight, "ID_Table": ID_Table, "ID_Column": ID_Column, "BarcodeType": BarcodeType, "FileName": FileName, "Text": Text})

    # Tisková sestava: Likvidační protokol
    def WarehouseItemStockTakingDiscarded(self, ID_Login, ID, ID_Warehouse):
        return self._client.service.WarehouseItemStockTakingDiscarded({"ID_Login": ID_Login, "ID": ID, "ID_Warehouse": ID_Warehouse})

    # Tisková sestava: Inventurní soupis
    def WarehouseItemStockTaking(self, ID_Login, ID, ID_Warehouse):
        return self._client.service.WarehouseItemStockTaking({"ID_Login": ID_Login, "ID": ID, "ID_Warehouse": ID_Warehouse})

    # Tisková sestava: Čárový kód položky skladu
    def WarehouseItemBarcode(self, ID_Login, ID, ID_Items=None, BarcodeType=None):
        return self._client.service.WarehouseItemBarcode({"ID_Login": ID_Login, "ID": ID, "ID_Items": ID_Items, "BarcodeType": BarcodeType})

    # Tisková sestava: Hodnocení kvality
    def WarehouseItem(self, ID_Login, ID_Unit, IncludeChild, EventRent, UnitRent, CommercialRent, IsDelete, InWarehouse, Count, RowMin, Reverse, DisplayName=None, InventoryNumber=None, ID_Items=None, ID_WarehouseArray=None, ID_WarehouseTagArray=None, Sort=None, ID_WarehouseItemCategory=None, Columns=None):
        return self._client.service.WarehouseItem({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IncludeChild": IncludeChild, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "IsDelete": IsDelete, "InWarehouse": InWarehouse, "Count": Count, "RowMin": RowMin, "Reverse": Reverse, "DisplayName": DisplayName, "InventoryNumber": InventoryNumber, "ID_Items": ID_Items, "ID_WarehouseArray": ID_WarehouseArray, "ID_WarehouseTagArray": ID_WarehouseTagArray, "Sort": Sort, "ID_WarehouseItemCategory": ID_WarehouseItemCategory, "Columns": Columns})

    # Tisková sestava: Srovnání výsledků kvality s ostatním
    def EvaluationCompare(self, ID_Login, ID, Culture=None):
        return self._client.service.EvaluationCompare({"ID_Login": ID_Login, "ID": ID, "Culture": Culture})

    # Tisková sestava: Grafický pohled na hodnocení podřízených jednotek
    def EvaluationShiftTable(self, ID_Login, ID, MostImportant, Format=None):
        return self._client.service.EvaluationShiftTable({"ID_Login": ID_Login, "ID": ID, "MostImportant": MostImportant, "Format": Format})

    # Tisková sestava: Přehled hlášenek pro MHMP
    def EventCampCapitalSummary(self, ID_Login, ID_Unit, IsFuture, Started, Year, IsRelation, IsChildDirect, IsChildUnit, ForEvaluation, IsKraj, DisplayName=None, ID_EventCampState=None, RegistrationNumber=None, Location=None):
        return self._client.service.EventCampCapitalSummary({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsFuture": IsFuture, "Started": Started, "Year": Year, "IsRelation": IsRelation, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "ForEvaluation": ForEvaluation, "IsKraj": IsKraj, "DisplayName": DisplayName, "ID_EventCampState": ID_EventCampState, "RegistrationNumber": RegistrationNumber, "Location": Location})

    # Tisková sestava: Grafický pohled na hodnocení podřízených jednotek
    def EvaluationGraphSummary(self, ID_Login, Year, ID_EvaluationSubtype):
        return self._client.service.EvaluationGraphSummary({"ID_Login": ID_Login, "Year": Year, "ID_EvaluationSubtype": ID_EvaluationSubtype})

    # Tisková sestava: Grafický pohled na hodnocení podřízených jednotek
    def EvaluationParticipationSummary(self, ID_Login, Year):
        return self._client.service.EvaluationParticipationSummary({"ID_Login": ID_Login, "Year": Year})

    # Tisková sestava: Náhled členské karty
    def MemberCardThumbnail(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardThumbnail({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Tisková sestava: Výpis z registru OJ
    def RegistryMinistry(self, ID_Login):
        return self._client.service.RegistryMinistry({"ID_Login": ID_Login})

    # Tisková sestava: Hodnocení kvality
    def EvaluationDetail(self, ID_Login, ID, EvaluationPersonCount, FileFormat=None):
        return self._client.service.EvaluationDetail({"ID_Login": ID_Login, "ID": ID, "EvaluationPersonCount": EvaluationPersonCount, "FileFormat": FileFormat})

    # Tisková sestava: Přehled skutečnosti jednotlivých táborů
    def EventCampRealAll(self, ID_Login, Year):
        return self._client.service.EventCampRealAll({"ID_Login": ID_Login, "Year": Year})

    # Tisková sestava: Export osob
    def ExportPerson(self, ID_Login, ID, FileFormat=None, Units=None):
        return self._client.service.ExportPerson({"ID_Login": ID_Login, "ID": ID, "FileFormat": FileFormat, "Units": Units})

    # Tisková sestava: Přehled skutečnosti táborů
    def EventCampReal(self, ID_Login, Year):
        return self._client.service.EventCampReal({"ID_Login": ID_Login, "Year": Year})

    # Tisková sestava: Přehled hlášenek
    def EventCampSummary(self, ID_Login, ID_Unit, IsFuture, Started, Year, IsRelation, IsChildDirect, IsChildUnit, ForEvaluation, IsKraj, DisplayName=None, ID_EventCampState=None, RegistrationNumber=None, Location=None):
        return self._client.service.EventCampSummary({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsFuture": IsFuture, "Started": Started, "Year": Year, "IsRelation": IsRelation, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "ForEvaluation": ForEvaluation, "IsKraj": IsKraj, "DisplayName": DisplayName, "ID_EventCampState": ID_EventCampState, "RegistrationNumber": RegistrationNumber, "Location": Location})

    # Vygenerování tiskové sestavy
    def Report(self, ID_Login, ID, ReportName=None, FileFormat=None, FileName=None):
        return self._client.service.Report({"ID_Login": ID_Login, "ID": ID, "ReportName": ReportName, "FileFormat": FileFormat, "FileName": FileName})

