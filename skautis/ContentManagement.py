# -*- coding: utf-8 -*-

import zeep

# Webová služba pro správu obsahu (redakční systém)
class ContentManagement(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/ContentManagement.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/ContentManagement.asmx?wsdl')

    # Načíst seznam oblíbených stránek
    def FavoriteAll(self, ID_Login, ID_User, ID, ID_Page, Top, DisplayName=None):
        return self._client.service.FavoriteAll({"ID_Login": ID_Login, "ID_User": ID_User, "ID": ID, "ID_Page": ID_Page, "Top": Top, "DisplayName": DisplayName})

    # Smazat oblíbenou stránku
    def FavoriteDelete(self, ID_Login, ID):
        return self._client.service.FavoriteDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail oblíbené stránky
    def FavoriteDetail(self, ID_Login, ID, ID_Page, ID_User):
        return self._client.service.FavoriteDetail({"ID_Login": ID_Login, "ID": ID, "ID_Page": ID_Page, "ID_User": ID_User})

    # Založit oblíbenou stránku
    def FavoriteInsert(self, ID_Login, ID, ID_User, ID_Page, DateCreate, Page=None, DisplayName=None, UrlParameter=None):
        return self._client.service.FavoriteInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Page": ID_Page, "DateCreate": DateCreate, "Page": Page, "DisplayName": DisplayName, "UrlParameter": UrlParameter})

    # Upravit oblíbenou stránku
    def FavoriteUpdate(self, ID_Login, ID, ID_User, ID_Page, DateCreate, Page=None, DisplayName=None, UrlParameter=None):
        return self._client.service.FavoriteUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Page": ID_Page, "DateCreate": DateCreate, "Page": Page, "DisplayName": DisplayName, "UrlParameter": UrlParameter})

    # Vyresetovat pořadí záložek
    def TabUpdateReset(self, ID_Login, MasterPage=None):
        return self._client.service.TabUpdateReset({"ID_Login": ID_Login, "MasterPage": MasterPage})

    # Načte podřízené položky hlavního menu jako HTML
    def MenuAllSubmenuHtml(self, ID_Login, ID, BaseUrl=None):
        return self._client.service.MenuAllSubmenuHtml({"ID_Login": ID_Login, "ID": ID, "BaseUrl": BaseUrl})

    # Načte položky hlavního menu jako HTML
    def MenuAllRootHtml(self, ID_Login, BaseUrl=None):
        return self._client.service.MenuAllRootHtml({"ID_Login": ID_Login, "BaseUrl": BaseUrl})

    # Načíst detail stránky
    def PageDetail(self, ID_Login, ID, CheckPermissions, Url=None, UrlParameter=None):
        return self._client.service.PageDetail({"ID_Login": ID_Login, "ID": ID, "CheckPermissions": CheckPermissions, "Url": Url, "UrlParameter": UrlParameter})

    # Načíst detail pohledu
    def PageStateDetail(self, ID_Login, ID, ID_Page, UrlParameter=None):
        return self._client.service.PageStateDetail({"ID_Login": ID_Login, "ID": ID, "ID_Page": ID_Page, "UrlParameter": UrlParameter})

    # Načíst seznam položek pohledu
    def PageStateItemAll(self, ID_Login, ID, ID_PageState):
        return self._client.service.PageStateItemAll({"ID_Login": ID_Login, "ID": ID, "ID_PageState": ID_PageState})

    # Smazat 
    def PageStateItemDelete(self, ID_Login, ID_Page):
        return self._client.service.PageStateItemDelete({"ID_Login": ID_Login, "ID_Page": ID_Page})

    # Upravit pohled
    def PageStateUpdate(self, ID_Login, ID, ID_User, ID_Known, ID_Page, IsDefault, Page=None, DisplayName=None, Data=None):
        return self._client.service.PageStateUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Known": ID_Known, "ID_Page": ID_Page, "IsDefault": IsDefault, "Page": Page, "DisplayName": DisplayName, "Data": Data})

    # Načíst seznam záložek
    def TabAll(self, ID_Login, ID, IsOrderSet, MasterPage=None):
        return self._client.service.TabAll({"ID_Login": ID_Login, "ID": ID, "IsOrderSet": IsOrderSet, "MasterPage": MasterPage})

    # Načíst validační hlášky
    def ValidateAll(self, ID_Login, ID, ProcedureName=None, ID_Action=None):
        return self._client.service.ValidateAll({"ID_Login": ID_Login, "ID": ID, "ProcedureName": ProcedureName, "ID_Action": ID_Action})

