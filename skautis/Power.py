# -*- coding: utf-8 -*-

import zeep

# Skautská energie
class Power(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Power.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Power.asmx?wsdl')

    # Načíst seznam způsobů platby záloh
    def AdvanceTypeAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.AdvanceTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typu ukončení smlouvy u předchozího dodavatele
    def ContractTerminationTypeAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.ContractTerminationTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Založit žádost energie
    def EnrollEnergyAllExport(self, ID_Login):
        return self._client.service.EnrollEnergyAllExport({"ID_Login": ID_Login})

    # Založit kandidáta o vstup do energie
    def EnrollEnergyCandidateInsert(self, ID_Login, ID_Application, Email=None, PersonalText=None):
        return self._client.service.EnrollEnergyCandidateInsert({"ID_Login": ID_Login, "ID_Application": ID_Application, "Email": Email, "PersonalText": PersonalText})

    # Procedura pro aktualizaci dokumentů
    def EnrollEnergyUpdateDocument(self, ID_Login, ID_Application, ID, ID_TempFile, ID_DocumentClass=None):
        return self._client.service.EnrollEnergyUpdateDocument({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_TempFile": ID_TempFile, "ID_DocumentClass": ID_DocumentClass})

    # Založit žádost energie z pozvánky
    def EnrollEnergyInsertAccessKey(self, ID_Login, ID_Application, AccessKey, ID, ID_Person, Birthday, ID_Unit, ID_TempfileAgreement, ID_TempFileAccount, ID_TempFileOther, OnlyValidate, AdvanceAmount, ContractTerminationDate, Note=None, ID_EnrollEnergyType=None, FirstName=None, LastName=None, IdentificationCode=None, UnitName=None, Company=None, IC=None, DIC=None, Agent=None, Function=None, Street=None, City=None, Postcode=None, EnergySupplier1=None, EnergySupplier2=None, Phone=None, Email=None, ID_AdvanceType=None, AdvanceTypeContent=None, ID_ContractTerminationType=None):
        return self._client.service.EnrollEnergyInsertAccessKey({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "ID_Unit": ID_Unit, "ID_TempfileAgreement": ID_TempfileAgreement, "ID_TempFileAccount": ID_TempFileAccount, "ID_TempFileOther": ID_TempFileOther, "OnlyValidate": OnlyValidate, "AdvanceAmount": AdvanceAmount, "ContractTerminationDate": ContractTerminationDate, "Note": Note, "ID_EnrollEnergyType": ID_EnrollEnergyType, "FirstName": FirstName, "LastName": LastName, "IdentificationCode": IdentificationCode, "UnitName": UnitName, "Company": Company, "IC": IC, "DIC": DIC, "Agent": Agent, "Function": Function, "Street": Street, "City": City, "Postcode": Postcode, "EnergySupplier1": EnergySupplier1, "EnergySupplier2": EnergySupplier2, "Phone": Phone, "Email": Email, "ID_AdvanceType": ID_AdvanceType, "AdvanceTypeContent": AdvanceTypeContent, "ID_ContractTerminationType": ID_ContractTerminationType})

    # Načíst detail pozvánka do skautské energie
    def EnrollEnergyInvitationDetailAccessKey(self, ID_Login, ID_Application, AccessKey):
        return self._client.service.EnrollEnergyInvitationDetailAccessKey({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey})

    # Načíst detail způsobu platby záloh
    def AdvanceTypeDetail(self, ID_Login, ID_Application, ID=None):
        return self._client.service.AdvanceTypeDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst soubor z přihlášky energie
    def EnrollEnergyDownload(self, ID_Login, ID, ID_Application, Type=None):
        return self._client.service.EnrollEnergyDownload({"ID_Login": ID_Login, "ID": ID, "ID_Application": ID_Application, "Type": Type})

    # Založit pozvánku do skautské energie
    def EnrollEnergyInvitationInsert(self, ID_Login, ID, ValidTo, AccessKey, ID_Person, LastOpened, IsValid, ID_Unit, Person=None, Email=None, PersonalText=None, Unit=None, RegistrationNumber=None):
        return self._client.service.EnrollEnergyInvitationInsert({"ID_Login": ID_Login, "ID": ID, "ValidTo": ValidTo, "AccessKey": AccessKey, "ID_Person": ID_Person, "LastOpened": LastOpened, "IsValid": IsValid, "ID_Unit": ID_Unit, "Person": Person, "Email": Email, "PersonalText": PersonalText, "Unit": Unit, "RegistrationNumber": RegistrationNumber})

    # Upravit pozvánku do skautské energie
    def EnrollEnergyInvitationUpdateExpired(self, ID_Login, ID, ValidTo, AccessKey, ID_Person, LastOpened, IsValid, ID_Unit, Person=None, Email=None, PersonalText=None, Unit=None, RegistrationNumber=None):
        return self._client.service.EnrollEnergyInvitationUpdateExpired({"ID_Login": ID_Login, "ID": ID, "ValidTo": ValidTo, "AccessKey": AccessKey, "ID_Person": ID_Person, "LastOpened": LastOpened, "IsValid": IsValid, "ID_Unit": ID_Unit, "Person": Person, "Email": Email, "PersonalText": PersonalText, "Unit": Unit, "RegistrationNumber": RegistrationNumber})

    # Založit žádost energie
    def EnrollEnergyAll(self, ID_Login):
        return self._client.service.EnrollEnergyAll({"ID_Login": ID_Login})

    # Načíst dodavatele energie
    def EnergySupplierAll(self, ID_Login, ID_Application):
        return self._client.service.EnergySupplierAll({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Založit žádost energie
    def EnrollEnergyInsert(self, ID_Login, ID_Application, AccessKey, ID, ID_Person, Birthday, ID_Unit, ID_TempfileAgreement, ID_TempFileAccount, ID_TempFileOther, OnlyValidate, AdvanceAmount, ContractTerminationDate, Note=None, ID_EnrollEnergyType=None, FirstName=None, LastName=None, IdentificationCode=None, UnitName=None, Company=None, IC=None, DIC=None, Agent=None, Function=None, Street=None, City=None, Postcode=None, EnergySupplier1=None, EnergySupplier2=None, Phone=None, Email=None, ID_AdvanceType=None, AdvanceTypeContent=None, ID_ContractTerminationType=None):
        return self._client.service.EnrollEnergyInsert({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "ID_Unit": ID_Unit, "ID_TempfileAgreement": ID_TempfileAgreement, "ID_TempFileAccount": ID_TempFileAccount, "ID_TempFileOther": ID_TempFileOther, "OnlyValidate": OnlyValidate, "AdvanceAmount": AdvanceAmount, "ContractTerminationDate": ContractTerminationDate, "Note": Note, "ID_EnrollEnergyType": ID_EnrollEnergyType, "FirstName": FirstName, "LastName": LastName, "IdentificationCode": IdentificationCode, "UnitName": UnitName, "Company": Company, "IC": IC, "DIC": DIC, "Agent": Agent, "Function": Function, "Street": Street, "City": City, "Postcode": Postcode, "EnergySupplier1": EnergySupplier1, "EnergySupplier2": EnergySupplier2, "Phone": Phone, "Email": Email, "ID_AdvanceType": ID_AdvanceType, "AdvanceTypeContent": AdvanceTypeContent, "ID_ContractTerminationType": ID_ContractTerminationType})

