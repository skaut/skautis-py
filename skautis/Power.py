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
    def AdvanceTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.AdvanceTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail způsobu platby záloh
    def AdvanceTypeDetail(self, ID_Login, ID=None):
        return self._client.service.AdvanceTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst soubor z přihlášky energie
    def EnrollEnergyDownload(self, ID_Login, ID, Type=None):
        return self._client.service.EnrollEnergyDownload({"ID_Login": ID_Login, "ID": ID, "Type": Type})

    # Založit žádost energie
    def EnrollEnergyAll(self, ID_Login):
        return self._client.service.EnrollEnergyAll({"ID_Login": ID_Login})

    # Načíst dodavatele energie
    def EnergySupplierAll(self, ID_Login):
        return self._client.service.EnergySupplierAll({"ID_Login": ID_Login})

    # Založit žádost energie
    def EnrollEnergyInsert(self, ID_Login, ID, ID_Person, ID_Unit, ID_TempfileAgreement, ID_TempFileAccount, ID_TempFileOther, OnlyValidate, AdvanceAmount, IdentificationCode=None, Note=None, ID_EnrollEnergyType=None, FirstName=None, LastName=None, UnitName=None, Company=None, IC=None, DIC=None, Agent=None, Function=None, Street=None, City=None, Postcode=None, EnergySupplier1=None, EnergySupplier2=None, Phone=None, Email=None, ID_AdvanceType=None, AdvanceTypeContent=None):
        return self._client.service.EnrollEnergyInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_TempfileAgreement": ID_TempfileAgreement, "ID_TempFileAccount": ID_TempFileAccount, "ID_TempFileOther": ID_TempFileOther, "OnlyValidate": OnlyValidate, "AdvanceAmount": AdvanceAmount, "IdentificationCode": IdentificationCode, "Note": Note, "ID_EnrollEnergyType": ID_EnrollEnergyType, "FirstName": FirstName, "LastName": LastName, "UnitName": UnitName, "Company": Company, "IC": IC, "DIC": DIC, "Agent": Agent, "Function": Function, "Street": Street, "City": City, "Postcode": Postcode, "EnergySupplier1": EnergySupplier1, "EnergySupplier2": EnergySupplier2, "Phone": Phone, "Email": Email, "ID_AdvanceType": ID_AdvanceType, "AdvanceTypeContent": AdvanceTypeContent})

