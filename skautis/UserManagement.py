# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s uživateli (zakládání, přidělování rolí, přihlašování apod.)
class UserManagement(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/UserManagement.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/UserManagement.asmx?wsdl')

    # Načíst seznam rolí uživatele v jednotce
    def UserRoleAllUserUnit(self, ID_Login, ID_User, ID_Unit):
        return self._client.service.UserRoleAllUserUnit({"ID_Login": ID_Login, "ID_User": ID_User, "ID_Unit": ID_Unit})

    # K danému datu vrátí nejbližší možný pracovní den
    def HolidayDetailNotHoliday(self, ID_Login, Date):
        return self._client.service.HolidayDetailNotHoliday({"ID_Login": ID_Login, "Date": Date})

    # Načíst informace o přihlášení pro 2F
    def LoginDetailTwoFactor(self, ID_Login):
        return self._client.service.LoginDetailTwoFactor({"ID_Login": ID_Login})

    # Načíst informace o přihlášení
    def LoginDetail(self, ID_Login):
        return self._client.service.LoginDetail({"ID_Login": ID_Login})

    # Ověření uživatele přes dvoufázové přihlášení
    def LoginUpdateTwoFactor(self, ID, ID_Application, SaveDevice, Code=None, ID_TwoFactorType=None, DisplayName=None):
        return self._client.service.LoginUpdateTwoFactor({"ID": ID, "ID_Application": ID_Application, "SaveDevice": SaveDevice, "Code": Code, "ID_TwoFactorType": ID_TwoFactorType, "DisplayName": DisplayName})

    # Automaticky nastavit vhodnou roli
    def LoginUpdateRoleAuto(self, ID_Login, ID, ID_Group, ID_Table=None, ID_Action=None, RequiredPermissions=None):
        return self._client.service.LoginUpdateRoleAuto({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_Table": ID_Table, "ID_Action": ID_Action, "RequiredPermissions": RequiredPermissions})

    # Načíst seznam pluginů
    def PluginAll(self, ID_Login, ID=None, DisplayName=None, InstanceKey=None):
        return self._client.service.PluginAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "InstanceKey": InstanceKey})

    # Načíst detail pluginu
    def PluginDetail(self, ID_Login, ID=None):
        return self._client.service.PluginDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit plugin
    def PluginUpdate(self, ID_Login, IsEnabled, ID=None, DisplayName=None, Description=None):
        return self._client.service.PluginUpdate({"ID_Login": ID_Login, "IsEnabled": IsEnabled, "ID": ID, "DisplayName": DisplayName, "Description": Description})

    # Upravit pořadí tabulky
    def TableSetOrder(self, ID_Login, TableSetOrderType, ID, OrderInc, ID_Table=None, ID_ParentTable=None, FilterValues=None):
        return self._client.service.TableSetOrder({"ID_Login": ID_Login, "TableSetOrderType": TableSetOrderType, "ID": ID, "OrderInc": OrderInc, "ID_Table": ID_Table, "ID_ParentTable": ID_ParentTable, "FilterValues": FilterValues})

    # Načíst seznam skupin nastavení
    def SettingsGroupAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.SettingsGroupAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Informace o dočasném souboru
    def TempFileDetail(self, ID_Login, ID, ID_Application):
        return self._client.service.TempFileDetail({"ID_Login": ID_Login, "ID": ID, "ID_Application": ID_Application})

    # Vložení dočasného souboru
    def TempFileInsertDocument(self, Size, ImageWidth, ImageHeigth, ID_Login, ID_Application, ContentType=None, Extension=None, HashMD5=None, Content=None, DisplayName=None, Filename=None):
        return self._client.service.TempFileInsertDocument({"Size": Size, "ImageWidth": ImageWidth, "ImageHeigth": ImageHeigth, "ID_Login": ID_Login, "ID_Application": ID_Application, "ContentType": ContentType, "Extension": Extension, "HashMD5": HashMD5, "Content": Content, "DisplayName": DisplayName, "Filename": Filename})

    # No documentation
    def TempFileMaintrance(self, ID_Login):
        return self._client.service.TempFileMaintrance({"ID_Login": ID_Login})

    # No documentation
    def TableMaintrance(self, ID_Login, Databases=None):
        return self._client.service.TableMaintrance({"ID_Login": ID_Login, "Databases": Databases})

    # No documentation
    def TableRebuild(self, ID_Login, OnlyFast):
        return self._client.service.TableRebuild({"ID_Login": ID_Login, "OnlyFast": OnlyFast})

    # Stáhnout dočasný soubor
    def TempFileDownload(self, ID_Login, ID, ID_Application):
        return self._client.service.TempFileDownload({"ID_Login": ID_Login, "ID": ID, "ID_Application": ID_Application})

    # Vložení dočasného souboru
    def TempFileInsert(self, Size, ID_Login, ID_Application, Extension=None, Content=None, Hash=None, Filename=None):
        return self._client.service.TempFileInsert({"Size": Size, "ID_Login": ID_Login, "ID_Application": ID_Application, "Extension": Extension, "Content": Content, "Hash": Hash, "Filename": Filename})

    # Načíst seznam vhodných rolí podle funkcí
    def RoleAllFunction(self, ID_Login, ID_User):
        return self._client.service.RoleAllFunction({"ID_Login": ID_Login, "ID_User": ID_User})

    # Načíst seznam přihlášení
    def LoginAll(self, ID_ApplicationNotCurrent, ID_Login, Count, NotEqual, ID_Application, Success):
        return self._client.service.LoginAll({"ID_ApplicationNotCurrent": ID_ApplicationNotCurrent, "ID_Login": ID_Login, "Count": Count, "NotEqual": NotEqual, "ID_Application": ID_Application, "Success": Success})

    # Zda se nemá z IP odhlašovat
    def PersistentIPDetailIsPersitent(self, ID_Login, IP=None):
        return self._client.service.PersistentIPDetailIsPersitent({"ID_Login": ID_Login, "IP": IP})

    # Načíst seznam Nastavení
    def SettingsAllPublic(self, ID_Login, ID_Application):
        return self._client.service.SettingsAllPublic({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Přidá/odebere přihlášeného uživatele do skupiny aplikace
    def GroupMemberApplication(self, ID_Login, Grant):
        return self._client.service.GroupMemberApplication({"ID_Login": ID_Login, "Grant": Grant})

    # Načíst detail instance skautISu
    def InstanceDetail(self, ID_Login, ID_Application):
        return self._client.service.InstanceDetail({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Načíst seznam Nastavení
    def SettingsAll(self, ID_Login, ID_SettingsGroup, DisplayName=None):
        return self._client.service.SettingsAll({"ID_Login": ID_Login, "ID_SettingsGroup": ID_SettingsGroup, "DisplayName": DisplayName})

    # Načíst detail Nastavení
    def SettingsDetail(self, ID_Login, ID_Application, ID=None):
        return self._client.service.SettingsDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Upravit 
    def SettingsUpdate(self, ID_Login, ID=None, DisplayName=None, Value=None, Note=None):
        return self._client.service.SettingsUpdate({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "Value": Value, "Note": Note})

    # No documentation
    def TableArchive(self, ID_Login):
        return self._client.service.TableArchive({"ID_Login": ID_Login})

    # Načíst seznam typů dvoufaktorového ověření
    def TwoFactorTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.TwoFactorTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit aktivaci účtu
    def UserActivationInsert(self, ID_Login, ID, Birthday, ValidTo, Activated, ID_Application, Code=None, UserName=None, Password=None, NickName=None, FirstName=None, LastName=None, ID_Sex=None, Email=None, IP=None, FirstNameParent=None, LastNameParent=None, EmailParent=None):
        return self._client.service.UserActivationInsert({"ID_Login": ID_Login, "ID": ID, "Birthday": Birthday, "ValidTo": ValidTo, "Activated": Activated, "ID_Application": ID_Application, "Code": Code, "UserName": UserName, "Password": Password, "NickName": NickName, "FirstName": FirstName, "LastName": LastName, "ID_Sex": ID_Sex, "Email": Email, "IP": IP, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "EmailParent": EmailParent})

    # Znovu odeslat aktivační email
    def UserActivationUpdateResend(self, ID_Login, ID, Birthday, ValidTo, Activated, ID_Application, Code=None, UserName=None, Password=None, NickName=None, FirstName=None, LastName=None, ID_Sex=None, Email=None, IP=None, FirstNameParent=None, LastNameParent=None, EmailParent=None):
        return self._client.service.UserActivationUpdateResend({"ID_Login": ID_Login, "ID": ID, "Birthday": Birthday, "ValidTo": ValidTo, "Activated": Activated, "ID_Application": ID_Application, "Code": Code, "UserName": UserName, "Password": Password, "NickName": NickName, "FirstName": FirstName, "LastName": LastName, "ID_Sex": ID_Sex, "Email": Email, "IP": IP, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "EmailParent": EmailParent})

    # Upravit aktivaci účtu
    def UserActivationUpdate(self, ID_Login, ID, Birthday, ValidTo, Activated, ID_Application, Code=None, UserName=None, Password=None, NickName=None, FirstName=None, LastName=None, ID_Sex=None, Email=None, IP=None, FirstNameParent=None, LastNameParent=None, EmailParent=None):
        return self._client.service.UserActivationUpdate({"ID_Login": ID_Login, "ID": ID, "Birthday": Birthday, "ValidTo": ValidTo, "Activated": Activated, "ID_Application": ID_Application, "Code": Code, "UserName": UserName, "Password": Password, "NickName": NickName, "FirstName": FirstName, "LastName": LastName, "ID_Sex": ID_Sex, "Email": Email, "IP": IP, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "EmailParent": EmailParent})

    # Načíst ověření uživatele
    def UserAuthenticationAll(self, ID_Login, ID_User):
        return self._client.service.UserAuthenticationAll({"ID_Login": ID_Login, "ID_User": ID_User})

    # Načíst detail ověření
    def UserAuthenticationDetail(self, ID_Login, ID):
        return self._client.service.UserAuthenticationDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail ověření
    def UserAuthenticationDetailForm(self, ID_Login, ID_User):
        return self._client.service.UserAuthenticationDetailForm({"ID_Login": ID_Login, "ID_User": ID_User})

    # Založit ověření
    def UserAuthenticationInsert(self, ID_Login, ID_Person, ID_User, Number=None, Code=None, NumberDataBox=None):
        return self._client.service.UserAuthenticationInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_User": ID_User, "Number": Number, "Code": Code, "NumberDataBox": NumberDataBox})

    # No documentation
    def UserAuthenticationStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.UserAuthenticationStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # No documentation
    def UserAuthenticationTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.UserAuthenticationTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit ověření uživatele
    def UserAuthenticationRequest(self, ID_Login, ID_Person, ID_User):
        return self._client.service.UserAuthenticationRequest({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_User": ID_User})

    # Nahrát ověřený formulář
    def UserAuthenticationUpdateForm(self, ID_Login, ID, ID_User, DateCreate, ID_UserAuthenticated, DateAuthenticated, ID_UserAuthenticationType=None, UserAuthenticationType=None, ID_UserAuthenticationState=None, UserAuthenticationState=None, Code=None, Number=None, Content=None, FormExtension=None, FormContent=None):
        return self._client.service.UserAuthenticationUpdateForm({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "DateCreate": DateCreate, "ID_UserAuthenticated": ID_UserAuthenticated, "DateAuthenticated": DateAuthenticated, "ID_UserAuthenticationType": ID_UserAuthenticationType, "UserAuthenticationType": UserAuthenticationType, "ID_UserAuthenticationState": ID_UserAuthenticationState, "UserAuthenticationState": UserAuthenticationState, "Code": Code, "Number": Number, "Content": Content, "FormExtension": FormExtension, "FormContent": FormContent})

    # Načtení externích informací o uživateli
    def UserDetailExternal(self, ID_Login, ID, ID_Person):
        return self._client.service.UserDetailExternal({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Načtení informací o uživateli pro dvoufaktorové přihlášení
    def UserDetailTwoFactor(self, ID_Login, ID):
        return self._client.service.UserDetailTwoFactor({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam záložních kódů uživatele
    def UserLoginCodeAll(self, ID_Login, ID_User, ID):
        return self._client.service.UserLoginCodeAll({"ID_Login": ID_Login, "ID_User": ID_User, "ID": ID})

    # Zkontrolovat platnost tokenu
    def UserLoginCodeOtherVerify(self, ID_Login, ID_User, Token=None, Type=None):
        return self._client.service.UserLoginCodeOtherVerify({"ID_Login": ID_Login, "ID_User": ID_User, "Token": Token, "Type": Type})

    # Vygenerovat kód pro přihlášení přes 2F
    def UserLoginCodeOtherGenerateEmailCode(self, ID_Login, ID, ID_User, Created, Used, IsValid, IsActive, Code=None):
        return self._client.service.UserLoginCodeOtherGenerateEmailCode({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "Created": Created, "Used": Used, "IsValid": IsValid, "IsActive": IsActive, "Code": Code})

    # Vygenerovat záložní kódy pro uživatele
    def UserLoginCodeOtherGenerate(self, ID_Login, ID, ID_User, Created, Used, IsValid, IsActive, Code=None):
        return self._client.service.UserLoginCodeOtherGenerate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "Created": Created, "Used": Used, "IsValid": IsValid, "IsActive": IsActive, "Code": Code})

    # Načíst seznam zařízení použitých přihlášení
    def UserLoginDeviceAll(self, ID_Login, ID, ID_User):
        return self._client.service.UserLoginDeviceAll({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User})

    # Smazat všechna zařízení použité k přihlášení
    def UserLoginDeviceDeleteAll(self, ID_Login, ID_User):
        return self._client.service.UserLoginDeviceDeleteAll({"ID_Login": ID_Login, "ID_User": ID_User})

    # Smazat zařízení použité k přihlášení
    def UserLoginDeviceDelete(self, ID_Login, ID):
        return self._client.service.UserLoginDeviceDelete({"ID_Login": ID_Login, "ID": ID})

    # Upravit zařízení použité k přihlášení
    def UserLoginDeviceUpdate(self, ID_Login, ID, Created, ValidTo, ID_User, IsValid, IsMobile, Token=None, Browser=None, System=None, UserAgent=None, DisplayName=None):
        return self._client.service.UserLoginDeviceUpdate({"ID_Login": ID_Login, "ID": ID, "Created": Created, "ValidTo": ValidTo, "ID_User": ID_User, "IsValid": IsValid, "IsMobile": IsMobile, "Token": Token, "Browser": Browser, "System": System, "UserAgent": UserAgent, "DisplayName": DisplayName})

    # Reset barevného nastavení uživatele
    def UserRoleUpdateColorReset(self, ID_Login, ID, ID_User, ID_Role, ID_Group, Color=None):
        return self._client.service.UserRoleUpdateColorReset({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Role": ID_Role, "ID_Group": ID_Group, "Color": Color})

    # Upravit barvu role uživatele
    def UserRoleUpdateColor(self, ID_Login, ID, ID_User, ID_Role, ID_Group, Color=None):
        return self._client.service.UserRoleUpdateColor({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Role": ID_Role, "ID_Group": ID_Group, "Color": Color})

    # Upravit výchozí řazení rolí uživatele
    def UserRoleUpdateRestoreOrder(self, ID_Login, ID_User):
        return self._client.service.UserRoleUpdateRestoreOrder({"ID_Login": ID_Login, "ID_User": ID_User})

    # Změnit viditelnost role
    def UserRoleUpdateIsActive(self, ID_Login, ID, ID_User, ID_Role, ID_Group, Color=None):
        return self._client.service.UserRoleUpdateIsActive({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Role": ID_Role, "ID_Group": ID_Group, "Color": Color})

    # Upravit nastavení 2F uživatele
    def UserUpdateTwoFactorDate(self, ID_Login, ID):
        return self._client.service.UserUpdateTwoFactorDate({"ID_Login": ID_Login, "ID": ID})

    # Upravit nastavení 2F uživatele
    def UserUpdateTwoFactor(self, ID_Login, ID, IsEnabledTwoFactor, ID_TwoFactorType=None):
        return self._client.service.UserUpdateTwoFactor({"ID_Login": ID_Login, "ID": ID, "IsEnabledTwoFactor": IsEnabledTwoFactor, "ID_TwoFactorType": ID_TwoFactorType})

    # Úprava počtu zobrazovaných oblíbených položek
    def UserUpdateFavoriteLimit(self, ID_Login, FavoriteLimit):
        return self._client.service.UserUpdateFavoriteLimit({"ID_Login": ID_Login, "FavoriteLimit": FavoriteLimit})

    # Změnit heslo administrátorem
    def UserUpdatePasswordAdmin(self, ID_Login, ID, Password=None, Password2=None):
        return self._client.service.UserUpdatePasswordAdmin({"ID_Login": ID_Login, "ID": ID, "Password": Password, "Password2": Password2})

    # Načíst seznam sazeb DPH
    def VatRateAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.VatRateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail sazby DPH podle typu sazby DPH
    def VatRateDetailVatRateType(self, ID_Login, ID_VatRateType=None):
        return self._client.service.VatRateDetailVatRateType({"ID_Login": ID_Login, "ID_VatRateType": ID_VatRateType})

    # Načíst detail sazby DPH
    def VatRateDetailPrice(self, ID_Login, ID, Price):
        return self._client.service.VatRateDetailPrice({"ID_Login": ID_Login, "ID": ID, "Price": Price})

    # Načíst detail sazby DPH
    def VatRateDetail(self, ID_Login, ID):
        return self._client.service.VatRateDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam akcí
    def ActionAll(self, ID_Login, DisplayName=None, ID_Table=None, ID_TableRelated=None, ID_Operation=None):
        return self._client.service.ActionAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_Table": ID_Table, "ID_TableRelated": ID_TableRelated, "ID_Operation": ID_Operation})

    # Načíst seznam chyb
    def ErrorAll(self, ID_Login, ID_User, DateFrom, DateTo, IsProcessed, DisplayName=None, ID_ErrorType=None, IgnoredErrorType=None):
        return self._client.service.ErrorAll({"ID_Login": ID_Login, "ID_User": ID_User, "DateFrom": DateFrom, "DateTo": DateTo, "IsProcessed": IsProcessed, "DisplayName": DisplayName, "ID_ErrorType": ID_ErrorType, "IgnoredErrorType": IgnoredErrorType})

    # Načíst detail chyby
    def ErrorDetail(self, ID_Login, ID):
        return self._client.service.ErrorDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit chybu
    def ErrorInsert(self, ID_Login, ID, ID_User, ID_Person, Date, IsProcessed, DisplayName=None, Person=None, ID_ErrorType=None, ErrorType=None, URL=None, Description=None, Browser=None, IP=None):
        return self._client.service.ErrorInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Person": ID_Person, "Date": Date, "IsProcessed": IsProcessed, "DisplayName": DisplayName, "Person": Person, "ID_ErrorType": ID_ErrorType, "ErrorType": ErrorType, "URL": URL, "Description": Description, "Browser": Browser, "IP": IP})

    # Upravit chybu
    def ErrorUpdate(self, ID_Login, ID, ID_User, ID_Person, Date, IsProcessed, DisplayName=None, Person=None, ID_ErrorType=None, ErrorType=None, URL=None, Description=None, Browser=None, IP=None):
        return self._client.service.ErrorUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Person": ID_Person, "Date": Date, "IsProcessed": IsProcessed, "DisplayName": DisplayName, "Person": Person, "ID_ErrorType": ID_ErrorType, "ErrorType": ErrorType, "URL": URL, "Description": Description, "Browser": Browser, "IP": IP})

    # Načíst seznam typů skupin
    def GroupTypeAll(self, ID_Login, CanLogin, DisplayName=None, ID_Table=None):
        return self._client.service.GroupTypeAll({"ID_Login": ID_Login, "CanLogin": CanLogin, "DisplayName": DisplayName, "ID_Table": ID_Table})

    # Načíst seznam položek logu
    def LogAll(self, ID_Login, DisplayObjectId, ID_User, ID_TableDisplay=None, ID_Operation=None):
        return self._client.service.LogAll({"ID_Login": ID_Login, "DisplayObjectId": DisplayObjectId, "ID_User": ID_User, "ID_TableDisplay": ID_TableDisplay, "ID_Operation": ID_Operation})

    # Načíst detail logu
    def LogDetail(self, ID_Login, ID):
        return self._client.service.LogDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst změněné vlastnosti
    def LogDetailHistory(self, ID_Login, ID):
        return self._client.service.LogDetailHistory({"ID_Login": ID_Login, "ID": ID})

    # Prodloužení platnosti přihlašovacího tokenu o 30 minut
    def LoginUpdateRefresh(self, ID):
        return self._client.service.LoginUpdateRefresh({"ID": ID})

    # Odhlášení uživatele
    def LoginUpdateLogout(self, ID):
        return self._client.service.LoginUpdateLogout({"ID": ID})

    # Načíst seznam skupin
    def GroupAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.GroupAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Přihlášení uživatele na jinou roli
    def LoginUpdate(self, ID, ID_UserRole):
        return self._client.service.LoginUpdate({"ID": ID, "ID_UserRole": ID_UserRole})

    # Načíst seznam operací
    def OperationAll(self, ID_Login, DisplayName=None):
        return self._client.service.OperationAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam oprávnění
    def PermissionAll(self, ID_Login, IsStatic, ID_Role, ID=None, DisplayName=None, ID_GroupType=None):
        return self._client.service.PermissionAll({"ID_Login": ID_Login, "IsStatic": IsStatic, "ID_Role": ID_Role, "ID": ID, "DisplayName": DisplayName, "ID_GroupType": ID_GroupType})

    # Vrátí seznam akcí, které může přihlášený uživatele vyvolat pro zadaný záznam
    def ActionVerify(self, ID_Login, ID, IsRaiseError, ID_Table=None, ID_Action=None):
        return self._client.service.ActionVerify({"ID_Login": ID_Login, "ID": ID, "IsRaiseError": IsRaiseError, "ID_Table": ID_Table, "ID_Action": ID_Action})

    # Vrátí seznam oprávnění přhlášeného uživatele
    def PermissionAllLogin(self, ID_Login, ID=None):
        return self._client.service.PermissionAllLogin({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam rolí
    def RoleAll(self, ID_Login, DisplayName=None, ID_UnitType=None, ID_GroupType=None):
        return self._client.service.RoleAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType, "ID_GroupType": ID_GroupType})

    # Smazat roli
    def RoleDelete(self, ID_Login, ID, IsHidden, IsTwoFactorRequired, DisplayName=None, ID_GroupType=None, GroupType=None, ID_UnitType=None, UnitType=None, Color=None):
        return self._client.service.RoleDelete({"ID_Login": ID_Login, "ID": ID, "IsHidden": IsHidden, "IsTwoFactorRequired": IsTwoFactorRequired, "DisplayName": DisplayName, "ID_GroupType": ID_GroupType, "GroupType": GroupType, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Color": Color})

    # Načíst detail role
    def RoleDetail(self, ID_Login, ID):
        return self._client.service.RoleDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit roli
    def RoleInsert(self, ID_Login, ID, IsHidden, IsTwoFactorRequired, DisplayName=None, ID_GroupType=None, GroupType=None, ID_UnitType=None, UnitType=None, Color=None):
        return self._client.service.RoleInsert({"ID_Login": ID_Login, "ID": ID, "IsHidden": IsHidden, "IsTwoFactorRequired": IsTwoFactorRequired, "DisplayName": DisplayName, "ID_GroupType": ID_GroupType, "GroupType": GroupType, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Color": Color})

    # Načíst seznam práv přiřazených do role
    def RolePermissionAll(self, ID_Login, ID_Role, ID_Permission=None):
        return self._client.service.RolePermissionAll({"ID_Login": ID_Login, "ID_Role": ID_Role, "ID_Permission": ID_Permission})

    # Odebrat právo z role
    def RolePermissionDelete(self, ID_Login, ID, ID_Role, IsHierarchic, ID_Permission=None):
        return self._client.service.RolePermissionDelete({"ID_Login": ID_Login, "ID": ID, "ID_Role": ID_Role, "IsHierarchic": IsHierarchic, "ID_Permission": ID_Permission})

    # Přidat právo do role
    def RolePermissionInsert(self, ID_Login, ID, ID_Role, IsHierarchic, ID_Permission=None):
        return self._client.service.RolePermissionInsert({"ID_Login": ID_Login, "ID": ID, "ID_Role": ID_Role, "IsHierarchic": IsHierarchic, "ID_Permission": ID_Permission})

    # Upravit přiřazení práva do role
    def RolePermissionUpdate(self, ID_Login, ID, ID_Role, IsHierarchic, ID_Permission=None):
        return self._client.service.RolePermissionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Role": ID_Role, "IsHierarchic": IsHierarchic, "ID_Permission": ID_Permission})

    # Upravit roli
    def RoleUpdate(self, ID_Login, ID, IsHidden, IsTwoFactorRequired, DisplayName=None, ID_GroupType=None, GroupType=None, ID_UnitType=None, UnitType=None, Color=None):
        return self._client.service.RoleUpdate({"ID_Login": ID_Login, "ID": ID, "IsHidden": IsHidden, "IsTwoFactorRequired": IsTwoFactorRequired, "DisplayName": DisplayName, "ID_GroupType": ID_GroupType, "GroupType": GroupType, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Color": Color})

    # Načíst seznam uživatelů
    def UserAll(self, ID_Login, ID, ID_Person, ID_Unit, UserName=None, DisplayName=None):
        return self._client.service.UserAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "UserName": UserName, "DisplayName": DisplayName})

    # Načíst seznam rolí přiřazených uživateli
    def UserRoleAll(self, ID_Login, ID_User, ID_Role, IsActive, CanEdit, ID, ID_GroupType=None):
        return self._client.service.UserRoleAll({"ID_Login": ID_Login, "ID_User": ID_User, "ID_Role": ID_Role, "IsActive": IsActive, "CanEdit": CanEdit, "ID": ID, "ID_GroupType": ID_GroupType})

    # Načíst seznam obsazení rolí v jednotce
    def UserRoleALLUnit(self, ID_Login, ID_Unit, ID_Role):
        return self._client.service.UserRoleALLUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Role": ID_Role})

    # Odebrat uživateli roli
    def UserRoleDelete(self, ID_Login, ID):
        return self._client.service.UserRoleDelete({"ID_Login": ID_Login, "ID": ID})

    # Přidat uživateli roli
    def UserRoleInsert(self, ID_Login, ID, ID_User, ID_Role, ID_Group, Color=None):
        return self._client.service.UserRoleInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Role": ID_Role, "ID_Group": ID_Group, "Color": Color})

    # Upravit roli uživatele
    def UserRoleUpdate(self, ID_Login, ID, ID_User, ID_Role, ID_Group, Color=None):
        return self._client.service.UserRoleUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Role": ID_Role, "ID_Group": ID_Group, "Color": Color})

    # Upravit uživatele
    def UserUpdate(self, ID_Login, ID, IsEnabled, Password=None, PasswordActual=None):
        return self._client.service.UserUpdate({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "Password": Password, "PasswordActual": PasswordActual})

    # Načíst seznam dnů v týdnu
    def WeekDayAll(self, ID_Login, DisplayName=None):
        return self._client.service.WeekDayAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Přihlášení uživatele
    def LoginInsert(self, ID_UserRole, ID_Application, IsPersistent, ID_PersistentLogin, IsMobile, UserName=None, Password=None, IP=None, Token=None, UserAgent=None, Place=None):
        return self._client.service.LoginInsert({"ID_UserRole": ID_UserRole, "ID_Application": ID_Application, "IsPersistent": IsPersistent, "ID_PersistentLogin": ID_PersistentLogin, "IsMobile": IsMobile, "UserName": UserName, "Password": Password, "IP": IP, "Token": Token, "UserAgent": UserAgent, "Place": Place})

    # Načtení informací o uživateli
    def UserDetail(self, ID_Login, ID):
        return self._client.service.UserDetail({"ID_Login": ID_Login, "ID": ID})

    # Registrace uživatele
    def UserInsert(self, Birthday, UserName=None, Password=None, FirstName=None, LastName=None, NickName=None, Email=None, ID_Sex=None):
        return self._client.service.UserInsert({"Birthday": Birthday, "UserName": UserName, "Password": Password, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "Email": Email, "ID_Sex": ID_Sex})

    # Žádost o zaslání e-mailu při ztrátě hesla
    def UserPasswordRequest(self, UserName=None, Email=None):
        return self._client.service.UserPasswordRequest({"UserName": UserName, "Email": Email})

    # Změna zapomenutého hesla pomocí jedinečného identifikátoru
    def UserUpdatePassword(self, PasswordRequest, Password=None):
        return self._client.service.UserUpdatePassword({"PasswordRequest": PasswordRequest, "Password": Password})

