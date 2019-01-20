# -*- coding: utf-8 -*-

import zeep

# Správa externích aplikací přistupujících ke skautISu
class ApplicationManagement(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/ApplicationManagement.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/ApplicationManagement.asmx?wsdl')

    # Načíst seznam oprávnění aplikace
    def ApplicationOperationAll(self, ID_Login, ID_Application, ID_Operation=None, ID_Action=None):
        return self._client.service.ApplicationOperationAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Operation": ID_Operation, "ID_Action": ID_Action})

    # Smazat oprávnění aplikace
    def ApplicationOperationDelete(self, ID_Login, ID):
        return self._client.service.ApplicationOperationDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit oprávnění aplikace
    def ApplicationOperationInsert(self, ID_Login, ID_Application, ID_Operation=None, ID_Action=None):
        return self._client.service.ApplicationOperationInsert({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Operation": ID_Operation, "ID_Action": ID_Action})

    # Načíst seznam akcí balíčku práv
    def PackageActionAll(self, ID_Login, ID_Package, ID, ID_Action=None):
        return self._client.service.PackageActionAll({"ID_Login": ID_Login, "ID_Package": ID_Package, "ID": ID, "ID_Action": ID_Action})

    # Smazat akci balíčku práv
    def PackageActionDelete(self, ID_Login, ID, ID_Package, Package=None, ID_Action=None, Action=None):
        return self._client.service.PackageActionDelete({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "Package": Package, "ID_Action": ID_Action, "Action": Action})

    # Založit akci balíčku práv
    def PackageActionInsert(self, ID_Login, ID, ID_Package, Package=None, ID_Action=None, Action=None):
        return self._client.service.PackageActionInsert({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "Package": Package, "ID_Action": ID_Action, "Action": Action})

    # Načíst seznam balíčků práv
    def PackageAll(self, ID_Login, ID, ID_Application, DisplayName=None):
        return self._client.service.PackageAll({"ID_Login": ID_Login, "ID": ID, "ID_Application": ID_Application, "DisplayName": DisplayName})

    # Načíst seznam balíčků v externí aplikace
    def PackageApplicationAll(self, ID_Login, ID, ID_Package, ID_Application):
        return self._client.service.PackageApplicationAll({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "ID_Application": ID_Application})

    # Smazat balíček v externí aplikace
    def PackageApplicationDelete(self, ID_Login, ID, ID_Package, ID_Application, Package=None, Application=None):
        return self._client.service.PackageApplicationDelete({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "ID_Application": ID_Application, "Package": Package, "Application": Application})

    # Založit balíček v externí aplikace
    def PackageApplicationInsert(self, ID_Login, ID, ID_Package, ID_Application, Package=None, Application=None):
        return self._client.service.PackageApplicationInsert({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "ID_Application": ID_Application, "Package": Package, "Application": Application})

    # Smazat balíček práv
    def PackageDelete(self, ID_Login, ID):
        return self._client.service.PackageDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail balíčku práv
    def PackageDetail(self, ID_Login, ID):
        return self._client.service.PackageDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit balíček práv
    def PackageInsert(self, ID_Login, ID, IsActive, DisplayName=None, Note=None):
        return self._client.service.PackageInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "DisplayName": DisplayName, "Note": Note})

    # Načíst seznam operací balíčku práv
    def PackageOperationAll(self, ID_Login, ID_Package, ID, ID_Operation=None):
        return self._client.service.PackageOperationAll({"ID_Login": ID_Login, "ID_Package": ID_Package, "ID": ID, "ID_Operation": ID_Operation})

    # Smazat operaci balíčku práv
    def PackageOperationDelete(self, ID_Login, ID, ID_Package, Package=None, ID_Operation=None, Operation=None):
        return self._client.service.PackageOperationDelete({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "Package": Package, "ID_Operation": ID_Operation, "Operation": Operation})

    # Založit operaci balíčku práv
    def PackageOperationInsert(self, ID_Login, ID, ID_Package, Package=None, ID_Operation=None, Operation=None):
        return self._client.service.PackageOperationInsert({"ID_Login": ID_Login, "ID": ID, "ID_Package": ID_Package, "Package": Package, "ID_Operation": ID_Operation, "Operation": Operation})

    # Aktualizovat aplikace
    def PackageUpdateSyncPermission(self, ID_Login, ID, IsActive, DisplayName=None, Note=None):
        return self._client.service.PackageUpdateSyncPermission({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "DisplayName": DisplayName, "Note": Note})

    # Upravit balíček práv
    def PackageUpdate(self, ID_Login, ID, IsActive, DisplayName=None, Note=None):
        return self._client.service.PackageUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "DisplayName": DisplayName, "Note": Note})

    # Načtení informací o externí aplikaci
    def RemoteApplicationDelete(self, ID_Login, ID_Application):
        return self._client.service.RemoteApplicationDelete({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Načíst seznam externích aplikací
    def RemoteApplicationAll(self):
        return self._client.service.RemoteApplicationAll(None)

    # Načtení informací o externí aplikaci
    def RemoteApplicationDetail(self, idApplication):
        return self._client.service.RemoteApplicationDetail(idApplication=idApplication)

    # Založení nové externí aplikace
    def RemoteApplicationInsert(self, ID_Login, ID_Application, Enabled, ID_Unit, ID_Person, IsAnonymous, IsAllActions, IsPersistentLogin, ID_Role, ID_GroupLogin, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, UnitName=None, Person=None, IP=None, Url=None, UrlLoginPage=None, UrlLogoutPage=None, UrlInfoPanel=None, ValidReturnUrl=None, Role=None):
        return self._client.service.RemoteApplicationInsert({"ID_Login": ID_Login, "ID_Application": ID_Application, "Enabled": Enabled, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "IsAnonymous": IsAnonymous, "IsAllActions": IsAllActions, "IsPersistentLogin": IsPersistentLogin, "ID_Role": ID_Role, "ID_GroupLogin": ID_GroupLogin, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "UnitName": UnitName, "Person": Person, "IP": IP, "Url": Url, "UrlLoginPage": UrlLoginPage, "UrlLogoutPage": UrlLogoutPage, "UrlInfoPanel": UrlInfoPanel, "ValidReturnUrl": ValidReturnUrl, "Role": Role})

    # Editace externí aplikace
    def RemoteApplicationUpdate(self, ID_Login, ID_Application, Enabled, ID_Unit, ID_Person, IsAnonymous, IsAllActions, IsPersistentLogin, ID_Role, ID_GroupLogin, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, UnitName=None, Person=None, IP=None, Url=None, UrlLoginPage=None, UrlLogoutPage=None, UrlInfoPanel=None, ValidReturnUrl=None, Role=None):
        return self._client.service.RemoteApplicationUpdate({"ID_Login": ID_Login, "ID_Application": ID_Application, "Enabled": Enabled, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "IsAnonymous": IsAnonymous, "IsAllActions": IsAllActions, "IsPersistentLogin": IsPersistentLogin, "ID_Role": ID_Role, "ID_GroupLogin": ID_GroupLogin, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "UnitName": UnitName, "Person": Person, "IP": IP, "Url": Url, "UrlLoginPage": UrlLoginPage, "UrlLogoutPage": UrlLogoutPage, "UrlInfoPanel": UrlInfoPanel, "ValidReturnUrl": ValidReturnUrl, "Role": Role})

