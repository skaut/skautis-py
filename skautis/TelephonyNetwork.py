# -*- coding: utf-8 -*-

import zeep

# Skautská telefonní síť (nová)
class TelephonyNetwork(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/TelephonyNetwork.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/TelephonyNetwork.asmx?wsdl')

    # Načíst informace o telefonních číslech v STS
    def PersonNumberInfoAll(self, ID_Login, ID, ID_Person, ID_Unit):
        return self._client.service.PersonNumberInfoAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit})

    # Načíst seznam přihlášek do STS
    def EnrollAll(self, ID_Login, ID, ID_Person):
        return self._client.service.EnrollAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Smazat přihlášku do STS
    def EnrollDelete(self, ID_Login, ID):
        return self._client.service.EnrollDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst přihlášku uživatele
    def EnrollDetailLogin(self, ID_Login, ID_Person):
        return self._client.service.EnrollDetailLogin({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načíst detail přihlášky do STS
    def EnrollDetail(self, ID_Login, ID, ID_Person):
        return self._client.service.EnrollDetail({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Ukončit přihlášku do STS
    def EnrollUpdateCancel(self, ID_Login, ID, ID_Person):
        return self._client.service.EnrollUpdateCancel({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Založit přihlášku do STS pro osobu
    def EnrollInsertPerson(self, ID_Login, ID, ID_Person, ValidFrom, ValidTo, IsValid, Agreement):
        return self._client.service.EnrollInsertPerson({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "IsValid": IsValid, "Agreement": Agreement})

    # Načíst seznam přístupových kódu do STS
    def EntryCodeAll(self, ID_Login, ID):
        return self._client.service.EntryCodeAll({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail platného přístupového kódu do STS
    def EntryCodeDetailValid(self, ID_Login, ID_Person):
        return self._client.service.EntryCodeDetailValid({"ID_Login": ID_Login, "ID_Person": ID_Person})

