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
    def RemoteApplicationInsert(self, ID_Application, Enabled, IsAnonymous, IsAllActions, ID_Login, IsPersistentLogin, ID_Role, ID_GroupLogin, DisplayName=None, Description=None, IP=None, Url=None, UrlLoginPage=None, UrlLogoutPage=None, UrlInfoPanel=None, Role=None):
        return self._client.service.RemoteApplicationInsert({"ID_Application": ID_Application, "Enabled": Enabled, "IsAnonymous": IsAnonymous, "IsAllActions": IsAllActions, "ID_Login": ID_Login, "IsPersistentLogin": IsPersistentLogin, "ID_Role": ID_Role, "ID_GroupLogin": ID_GroupLogin, "DisplayName": DisplayName, "Description": Description, "IP": IP, "Url": Url, "UrlLoginPage": UrlLoginPage, "UrlLogoutPage": UrlLogoutPage, "UrlInfoPanel": UrlInfoPanel, "Role": Role})

    # Editace externí aplikace
    def RemoteApplicationUpdate(self, ID_Application, Enabled, IsAnonymous, IsAllActions, ID_Login, IsPersistentLogin, ID_Role, ID_GroupLogin, DisplayName=None, Description=None, IP=None, Url=None, UrlLoginPage=None, UrlLogoutPage=None, UrlInfoPanel=None, Role=None):
        return self._client.service.RemoteApplicationUpdate({"ID_Application": ID_Application, "Enabled": Enabled, "IsAnonymous": IsAnonymous, "IsAllActions": IsAllActions, "ID_Login": ID_Login, "IsPersistentLogin": IsPersistentLogin, "ID_Role": ID_Role, "ID_GroupLogin": ID_GroupLogin, "DisplayName": DisplayName, "Description": Description, "IP": IP, "Url": Url, "UrlLoginPage": UrlLoginPage, "UrlLogoutPage": UrlLogoutPage, "UrlInfoPanel": UrlInfoPanel, "Role": Role})

