# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s pojištěním osoby
class Insurance(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Insurance.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Insurance.asmx?wsdl')

    # Načíst seznam Částek za rok
    def AmountPersonAll(self, ID_Application, ID_Login, ID):
        return self._client.service.AmountPersonAll({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID})

    # Smazat Částku za rok
    def AmountPersonDelete(self, ID_Application, ID_Login, ID):
        return self._client.service.AmountPersonDelete({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID})

    # Načíst detail Částky za rok
    def AmountPersonDetail(self, ID_Application, ID_Login, ID, Year):
        return self._client.service.AmountPersonDetail({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID, "Year": Year})

    # Založit Částku za rok
    def AmountPersonInsert(self, ID_Login, ID, Amount, Year, Note=None):
        return self._client.service.AmountPersonInsert({"ID_Login": ID_Login, "ID": ID, "Amount": Amount, "Year": Year, "Note": Note})

    # Upravit Částku za rok
    def AmountPersonUpdate(self, ID_Login, ID, Amount, Year, Note=None):
        return self._client.service.AmountPersonUpdate({"ID_Login": ID_Login, "ID": ID, "Amount": Amount, "Year": Year, "Note": Note})

    # Načíst seznam osob pro pojištění
    def PersonAllUnit(self, ID_Login, ID_Unit, Year, ShowRegistered):
        return self._client.service.PersonAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "Year": Year, "ShowRegistered": ShowRegistered})

    # Načíst seznam pojištěných osob
    def PersonAllRegistration(self, ID_Login, ID_Registration):
        return self._client.service.PersonAllRegistration({"ID_Login": ID_Login, "ID_Registration": ID_Registration})

    # Načíst seznam pojištění osob
    def PersonAll(self, ID_Login, ID_Unit, ID_Function, Year, Person=None):
        return self._client.service.PersonAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Function": ID_Function, "Year": Year, "Person": Person})

    # Smazat pojištění osoby
    def PersonDelete(self, ID_Login, ID):
        return self._client.service.PersonDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail pojištění osoby
    def PersonDetail(self, ID_Login, ID):
        return self._client.service.PersonDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit pojištění osoby
    def PersonUpdate(self, ID_Login, ID, ID_Person, ID_Unit, ID_Function, ValidFrom, ValidTo, Amount, PersonDisplayName=None, Unit=None, RegistrationNumber=None, Note=None):
        return self._client.service.PersonUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Function": ID_Function, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "Amount": Amount, "PersonDisplayName": PersonDisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Note": Note})

    # Načíst seznam registrací, u kterých selhalo odeslání
    def RegistrationAllPostFailed(self, ID_Login, ShowRegistrationOnly):
        return self._client.service.RegistrationAllPostFailed({"ID_Login": ID_Login, "ShowRegistrationOnly": ShowRegistrationOnly})

    # Načíst detail registrace
    def RegistrationDetail(self, ID_Login, ID):
        return self._client.service.RegistrationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit registraci
    def RegistrationInsert(self, ID_Login, ID_Unit, Year, OnlyValidate, Note=None, Persons=None):
        return self._client.service.RegistrationInsert({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "Year": Year, "OnlyValidate": OnlyValidate, "Note": Note, "Persons": Persons})

    # Upravit registraci
    def RegistrationUpdate(self, ID_Login, ID, ExternalID, ID_Unit, ID_Person, Created, Unit=None, RegistrationNumber=None, Person=None, Note=None):
        return self._client.service.RegistrationUpdate({"ID_Login": ID_Login, "ID": ID, "ExternalID": ExternalID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "Created": Created, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Person": Person, "Note": Note})

