import zeep

# Webová služba pro práci s GoogleApps (zápis dat do databáze, komunikace s GoogleApps)
class GoogleApps:
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/GoogleApps.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/GoogleApps.asmx?wsdl')

    # Smazat doménu pouze ze skautISu
    def DomainDelete(self, ID_Login, ID):
        return self._client.service.DomainDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam využití sdílených disků jednotky
    def SharedDriveAllUnitUsage(self, ID_Login, ID_Unit):
        return self._client.service.SharedDriveAllUnitUsage({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načíst seznam sdílených disků jednotky
    def SharedDriveAllUnit(self, ID_Login, ID_Unit):
        return self._client.service.SharedDriveAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načíst seznam názvů akcí pro sdílené disky jednotky
    def SharedDriveAllEvents(self, ID_Login, ID_Unit, AddSystemItem, DisplayName=None):
        return self._client.service.SharedDriveAllEvents({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "AddSystemItem": AddSystemItem, "DisplayName": DisplayName})

    # Aktualizovat využití sdíleného disku
    def SharedDriveUpdateUsage(self, ID_Login, ID, ID_Unit, DateCreated, ID_UserCreated, SpaceUsed, ID_PersonAdmin, DateUpdated, CheckConditions, ID_PersonCreated, ShowEventName, ShowAdminLink, DriveId=None, Unit=None, ID_SharedDriveType=None, SharedDriveType=None, DisplayName=None, EventName=None, UserCreated=None, AdminEmail=None, Note=None, OrgUnitPath=None, DateUpdatedClass=None):
        return self._client.service.SharedDriveUpdateUsage({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreated": DateCreated, "ID_UserCreated": ID_UserCreated, "SpaceUsed": SpaceUsed, "ID_PersonAdmin": ID_PersonAdmin, "DateUpdated": DateUpdated, "CheckConditions": CheckConditions, "ID_PersonCreated": ID_PersonCreated, "ShowEventName": ShowEventName, "ShowAdminLink": ShowAdminLink, "DriveId": DriveId, "Unit": Unit, "ID_SharedDriveType": ID_SharedDriveType, "SharedDriveType": SharedDriveType, "DisplayName": DisplayName, "EventName": EventName, "UserCreated": UserCreated, "AdminEmail": AdminEmail, "Note": Note, "OrgUnitPath": OrgUnitPath, "DateUpdatedClass": DateUpdatedClass})

    # Založit fixně nastavenou emailovou adresu v Google skupině dle emailu
    def SyncSettingsEmailInsertEmail(self, ID_Login, ID_GoogleGroup, EmailArray=None):
        return self._client.service.SyncSettingsEmailInsertEmail({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "EmailArray": EmailArray})

    # Založit fixně nastavenou emailovou adresu v Google skupině dle osoby
    def SyncSettingsEmailInsertPerson(self, ID_Login, ID_GoogleGroup, ID_Person):
        return self._client.service.SyncSettingsEmailInsertPerson({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "ID_Person": ID_Person})

    # Smazat fixně nastavenou emailovou adresu v Google skupině
    def SyncSettingsEmailDelete(self, ID_Login, ID, ID_GoogleGroup):
        return self._client.service.SyncSettingsEmailDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup})

    # Načíst seznam fixně nastavených emailových adres v Google skupině
    def SyncSettingsEmailAll(self, ID_Login, ID_GoogleGroup):
        return self._client.service.SyncSettingsEmailAll({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup})

    # Načíst seznam GA účtů k synchronizaci
    def GoogleAccountAllSync(self, ID_Login):
        return self._client.service.GoogleAccountAllSync({"ID_Login": ID_Login})

    # Načíst detail užití úložiště daného účtu v GA
    def GoogleAccountDetailStorage(self, ID_Login, ID):
        return self._client.service.GoogleAccountDetailStorage({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail hlavního účtu jednotky v GA
    def GoogleAccountDetailOrganizationUnit(self, ID_Login, ID):
        return self._client.service.GoogleAccountDetailOrganizationUnit({"ID_Login": ID_Login, "ID": ID})

    # Nastavit organizační jednotku pro google účet
    def GoogleAccountUpdateOrganizationUnit(self, ID_Login, ID, OrganizationUnitId=None):
        return self._client.service.GoogleAccountUpdateOrganizationUnit({"ID_Login": ID_Login, "ID": ID, "OrganizationUnitId": OrganizationUnitId})

    # Načíst seznam organizačních jednotek v GA
    def GoogleUnitAll(self, ID_Login):
        return self._client.service.GoogleUnitAll({"ID_Login": ID_Login})

    # Načíst seznam google skupin pro synchronizaci
    def GoogleGroupAllSync(self, ID_Login):
        return self._client.service.GoogleGroupAllSync({"ID_Login": ID_Login})

    # Načíst seznam požadavků na synchronizaci
    def GoogleGroupSyncRequestAll(self, ID_Login, ID_GoogleGroup, ID):
        return self._client.service.GoogleGroupSyncRequestAll({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "ID": ID})

    # Načíst seznam nastavení synchronizace Google skupiny
    def GoogleGroupSyncSettingsAll(self, ID_Login, ID_GoogleGroup, ID, ID_SyncLevelType=None, ID_SyncType=None):
        return self._client.service.GoogleGroupSyncSettingsAll({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "ID": ID, "ID_SyncLevelType": ID_SyncLevelType, "ID_SyncType": ID_SyncType})

    # Smazat nastavení synchronizace Google skupiny
    def GoogleGroupSyncSettingsDelete(self, ID_Login, ID, ID_GoogleGroup, IsFunction, ID_Unit, GoogleGroup=None, ID_SyncLevelType=None, SyncLevelType=None, Units=None, SyncContactTypes=None, MembershipCategories=None, FunctionsDirect=None, Functions=None, ID_UnitType=None, DisplayName=None):
        return self._client.service.GoogleGroupSyncSettingsDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "IsFunction": IsFunction, "ID_Unit": ID_Unit, "GoogleGroup": GoogleGroup, "ID_SyncLevelType": ID_SyncLevelType, "SyncLevelType": SyncLevelType, "Units": Units, "SyncContactTypes": SyncContactTypes, "MembershipCategories": MembershipCategories, "FunctionsDirect": FunctionsDirect, "Functions": Functions, "ID_UnitType": ID_UnitType, "DisplayName": DisplayName})

    # Založit nastavení synchronizace Google skupiny
    def GoogleGroupSyncSettingsInsert(self, ID_Login, ID, ID_GoogleGroup, IsFunction, ID_Unit, GoogleGroup=None, ID_SyncLevelType=None, SyncLevelType=None, Units=None, SyncContactTypes=None, MembershipCategories=None, FunctionsDirect=None, Functions=None, ID_UnitType=None, DisplayName=None):
        return self._client.service.GoogleGroupSyncSettingsInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "IsFunction": IsFunction, "ID_Unit": ID_Unit, "GoogleGroup": GoogleGroup, "ID_SyncLevelType": ID_SyncLevelType, "SyncLevelType": SyncLevelType, "Units": Units, "SyncContactTypes": SyncContactTypes, "MembershipCategories": MembershipCategories, "FunctionsDirect": FunctionsDirect, "Functions": Functions, "ID_UnitType": ID_UnitType, "DisplayName": DisplayName})

    # Synchronizovat google účet
    def GoogleAccountUpdateSync(self, ID_Login, ID, UnitEmail=None, PersonEmail=None, OldGroup=None, NewGroup=None):
        return self._client.service.GoogleAccountUpdateSync({"ID_Login": ID_Login, "ID": ID, "UnitEmail": UnitEmail, "PersonEmail": PersonEmail, "OldGroup": OldGroup, "NewGroup": NewGroup})

    # Upravit typ synchronizace google skupiny
    def GoogleGroupUpdateSyncType(self, ID_Login, ID, ID_Unit, DateCreate, ID_GoogleGroupMain, ID_Domain, MemberCount, Valid, LastSync, IsAutoSync, DisplayName=None, Email=None, Unit=None, RegistrationNumber=None, GoogleGroupMainEmail=None, Description=None, EmailName=None, OwnerEmail=None, ID_SyncType=None, SyncType=None):
        return self._client.service.GoogleGroupUpdateSyncType({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreate": DateCreate, "ID_GoogleGroupMain": ID_GoogleGroupMain, "ID_Domain": ID_Domain, "MemberCount": MemberCount, "Valid": Valid, "LastSync": LastSync, "IsAutoSync": IsAutoSync, "DisplayName": DisplayName, "Email": Email, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GoogleGroupMainEmail": GoogleGroupMainEmail, "Description": Description, "EmailName": EmailName, "OwnerEmail": OwnerEmail, "ID_SyncType": ID_SyncType, "SyncType": SyncType})

    # Synchronizovat google skupinu
    def GoogleGroupUpdateSync(self, ID_Login, ID, ID_Unit, DateCreate, ID_GoogleGroupMain, ID_Domain, MemberCount, Valid, LastSync, IsAutoSync, DisplayName=None, Email=None, Unit=None, RegistrationNumber=None, GoogleGroupMainEmail=None, Description=None, EmailName=None, OwnerEmail=None, ID_SyncType=None, SyncType=None):
        return self._client.service.GoogleGroupUpdateSync({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreate": DateCreate, "ID_GoogleGroupMain": ID_GoogleGroupMain, "ID_Domain": ID_Domain, "MemberCount": MemberCount, "Valid": Valid, "LastSync": LastSync, "IsAutoSync": IsAutoSync, "DisplayName": DisplayName, "Email": Email, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GoogleGroupMainEmail": GoogleGroupMainEmail, "Description": Description, "EmailName": EmailName, "OwnerEmail": OwnerEmail, "ID_SyncType": ID_SyncType, "SyncType": SyncType})

    # Založit požadavek na synchronizaci
    def GoogleGroupSyncRequestInsert(self, ID_Login, ID, ID_GoogleGroup, Created, Synced, IsSyncing, GoogleGroup=None, Exception=None):
        return self._client.service.GoogleGroupSyncRequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "Created": Created, "Synced": Synced, "IsSyncing": IsSyncing, "GoogleGroup": GoogleGroup, "Exception": Exception})

    # Dokončit požadavek na synchronizaci
    def GoogleGroupSyncRequestUpdateError(self, ID_Login, ID, ID_GoogleGroup, Created, Synced, IsSyncing, GoogleGroup=None, Exception=None):
        return self._client.service.GoogleGroupSyncRequestUpdateError({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "Created": Created, "Synced": Synced, "IsSyncing": IsSyncing, "GoogleGroup": GoogleGroup, "Exception": Exception})

    # Dokončit požadavek na synchronizaci
    def GoogleGroupSyncRequestUpdateFinish(self, ID_Login, ID, ID_GoogleGroup, Created, Synced, IsSyncing, GoogleGroup=None, Exception=None):
        return self._client.service.GoogleGroupSyncRequestUpdateFinish({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "Created": Created, "Synced": Synced, "IsSyncing": IsSyncing, "GoogleGroup": GoogleGroup, "Exception": Exception})

    # Načíst detail nastavení synchronizace Google skupiny
    def GoogleGroupSyncSettingsDetail(self, ID_Login, ID, ID_GoogleGroup):
        return self._client.service.GoogleGroupSyncSettingsDetail({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup})

    # Upravit nastavení synchronizace Google skupiny
    def GoogleGroupSyncSettingsUpdate(self, ID_Login, ID, ID_GoogleGroup, IsFunction, ID_Unit, GoogleGroup=None, ID_SyncLevelType=None, SyncLevelType=None, Units=None, SyncContactTypes=None, MembershipCategories=None, FunctionsDirect=None, Functions=None, ID_UnitType=None, DisplayName=None):
        return self._client.service.GoogleGroupSyncSettingsUpdate({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroup": ID_GoogleGroup, "IsFunction": IsFunction, "ID_Unit": ID_Unit, "GoogleGroup": GoogleGroup, "ID_SyncLevelType": ID_SyncLevelType, "SyncLevelType": SyncLevelType, "Units": Units, "SyncContactTypes": SyncContactTypes, "MembershipCategories": MembershipCategories, "FunctionsDirect": FunctionsDirect, "Functions": Functions, "ID_UnitType": ID_UnitType, "DisplayName": DisplayName})

    # Smazat sdílený disk
    def SharedDriveDelete(self, ID_Login, ID, IsComplete):
        return self._client.service.SharedDriveDelete({"ID_Login": ID_Login, "ID": ID, "IsComplete": IsComplete})

    # Načíst detail sdíleného disku
    def SharedDriveDetail(self, ID_Login, ID):
        return self._client.service.SharedDriveDetail({"ID_Login": ID_Login, "ID": ID})

    def SharedDriveInsert(self, ID_Login, ID, ID_Unit, DateCreated, ID_UserCreated, SpaceUsed, ID_PersonAdmin, DateUpdated, CheckConditions, ID_PersonCreated, ShowEventName, ShowAdminLink, DriveId=None, Unit=None, ID_SharedDriveType=None, SharedDriveType=None, DisplayName=None, EventName=None, UserCreated=None, AdminEmail=None, Note=None, OrgUnitPath=None, DateUpdatedClass=None):
        return self._client.service.SharedDriveInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreated": DateCreated, "ID_UserCreated": ID_UserCreated, "SpaceUsed": SpaceUsed, "ID_PersonAdmin": ID_PersonAdmin, "DateUpdated": DateUpdated, "CheckConditions": CheckConditions, "ID_PersonCreated": ID_PersonCreated, "ShowEventName": ShowEventName, "ShowAdminLink": ShowAdminLink, "DriveId": DriveId, "Unit": Unit, "ID_SharedDriveType": ID_SharedDriveType, "SharedDriveType": SharedDriveType, "DisplayName": DisplayName, "EventName": EventName, "UserCreated": UserCreated, "AdminEmail": AdminEmail, "Note": Note, "OrgUnitPath": OrgUnitPath, "DateUpdatedClass": DateUpdatedClass})

    # Načíst seznam typů sdíleného disku
    def SharedDriveTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.SharedDriveTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit sdílený disk
    def SharedDriveUpdate(self, ID_Login, ID, ID_Unit, DateCreated, ID_UserCreated, SpaceUsed, ID_PersonAdmin, DateUpdated, CheckConditions, ID_PersonCreated, ShowEventName, ShowAdminLink, DriveId=None, Unit=None, ID_SharedDriveType=None, SharedDriveType=None, DisplayName=None, EventName=None, UserCreated=None, AdminEmail=None, Note=None, OrgUnitPath=None, DateUpdatedClass=None):
        return self._client.service.SharedDriveUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreated": DateCreated, "ID_UserCreated": ID_UserCreated, "SpaceUsed": SpaceUsed, "ID_PersonAdmin": ID_PersonAdmin, "DateUpdated": DateUpdated, "CheckConditions": CheckConditions, "ID_PersonCreated": ID_PersonCreated, "ShowEventName": ShowEventName, "ShowAdminLink": ShowAdminLink, "DriveId": DriveId, "Unit": Unit, "ID_SharedDriveType": ID_SharedDriveType, "SharedDriveType": SharedDriveType, "DisplayName": DisplayName, "EventName": EventName, "UserCreated": UserCreated, "AdminEmail": AdminEmail, "Note": Note, "OrgUnitPath": OrgUnitPath, "DateUpdatedClass": DateUpdatedClass})

    # Typ kontaktu pro synchronizaci
    def SyncContactTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.SyncContactTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    def SyncLevelTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.SyncLevelTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů funkce v nastavení Google skupiny
    def SyncSettingsFunctionTypeAll(self, ID_Login, ID_GoogleGroupSyncSettings, ID, ID_FunctionType):
        return self._client.service.SyncSettingsFunctionTypeAll({"ID_Login": ID_Login, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID": ID, "ID_FunctionType": ID_FunctionType})

    # Smazat typ funkce v nastavení Google skupiny
    def SyncSettingsFunctionTypeDelete(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_FunctionType, IsDirect, FunctionType=None):
        return self._client.service.SyncSettingsFunctionTypeDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_FunctionType": ID_FunctionType, "IsDirect": IsDirect, "FunctionType": FunctionType})

    # Založit typ funkce v nastavení Google skupiny
    def SyncSettingsFunctionTypeInsert(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_FunctionType, IsDirect, FunctionType=None):
        return self._client.service.SyncSettingsFunctionTypeInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_FunctionType": ID_FunctionType, "IsDirect": IsDirect, "FunctionType": FunctionType})

    # Načíst seznam kategorií členství v nastavení synchronizace Google skupiny
    def SyncSettingsMembershipCategoryAll(self, ID_Login, ID_GoogleGroupSyncSettings, ID, ID_MembershipCategory=None):
        return self._client.service.SyncSettingsMembershipCategoryAll({"ID_Login": ID_Login, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID": ID, "ID_MembershipCategory": ID_MembershipCategory})

    # Smazat kategorii členství v nastavení synchronizace Google skupiny
    def SyncSettingsMembershipCategoryDelete(self, ID_Login, ID, ID_GoogleGroupSyncSettings, MembershipCategories=None, ID_MembershipCategory=None, MembershipCategory=None, DisplayName=None):
        return self._client.service.SyncSettingsMembershipCategoryDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "MembershipCategories": MembershipCategories, "ID_MembershipCategory": ID_MembershipCategory, "MembershipCategory": MembershipCategory, "DisplayName": DisplayName})

    # Založit kategorii členství v nastavení synchronizace Google skupiny
    def SyncSettingsMembershipCategoryInsert(self, ID_Login, ID, ID_GoogleGroupSyncSettings, MembershipCategories=None, ID_MembershipCategory=None, MembershipCategory=None, DisplayName=None):
        return self._client.service.SyncSettingsMembershipCategoryInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "MembershipCategories": MembershipCategories, "ID_MembershipCategory": ID_MembershipCategory, "MembershipCategory": MembershipCategory, "DisplayName": DisplayName})

    # Načíst seznam typů kontaktu v nastavení synchronizace Google skupiny
    def SyncSettingsSyncContactTypeAll(self, ID_Login, ID_GoogleGroupSyncSettings, ID, ID_SyncContactType=None):
        return self._client.service.SyncSettingsSyncContactTypeAll({"ID_Login": ID_Login, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID": ID, "ID_SyncContactType": ID_SyncContactType})

    # Založit typ kontaktu nastavení synchronizace Google skupiny
    def SyncSettingsSyncContactTypeInsert(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_SyncContactType=None, SyncContactType=None):
        return self._client.service.SyncSettingsSyncContactTypeInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_SyncContactType": ID_SyncContactType, "SyncContactType": SyncContactType})

    # Smazat typ kontaktu nastavení synchronizace Google skupiny
    def SyncSettingsSyncContactTypeDelete(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_SyncContactType=None, SyncContactType=None):
        return self._client.service.SyncSettingsSyncContactTypeDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_SyncContactType": ID_SyncContactType, "SyncContactType": SyncContactType})

    # Načíst seznam jednotek v nastavení Google skupiny
    def SyncSettingsUnitAll(self, ID_Login, ID_GoogleGroupSyncSettings, ID, ID_Unit):
        return self._client.service.SyncSettingsUnitAll({"ID_Login": ID_Login, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID": ID, "ID_Unit": ID_Unit})

    # Smazat jednotku v nastavení Google skupiny
    def SyncSettingsUnitDelete(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_Unit, Units=None, Unit=None, RegistrationNumber=None, DisplayName=None):
        return self._client.service.SyncSettingsUnitDelete({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_Unit": ID_Unit, "Units": Units, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "DisplayName": DisplayName})

    # Založit jednotku v nastavení Google skupiny
    def SyncSettingsUnitInsert(self, ID_Login, ID, ID_GoogleGroupSyncSettings, ID_Unit, Units=None, Unit=None, RegistrationNumber=None, DisplayName=None):
        return self._client.service.SyncSettingsUnitInsert({"ID_Login": ID_Login, "ID": ID, "ID_GoogleGroupSyncSettings": ID_GoogleGroupSyncSettings, "ID_Unit": ID_Unit, "Units": Units, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "DisplayName": DisplayName})

    def SyncTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.SyncTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam Google workspace předplatných jednotky
    def WorkspaceUnitAllUnit(self, ID_Login, ID_Unit, ID, ID_Person, SearchParent, DisplayName=None):
        return self._client.service.WorkspaceUnitAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_Person": ID_Person, "SearchParent": SearchParent, "DisplayName": DisplayName})

    # Načíst seznam GA účtů ke smazání
    def GoogleAccountAllInactive(self, ID_Login):
        return self._client.service.GoogleAccountAllInactive({"ID_Login": ID_Login})

    # Načíst seznam GA skupin ke smazání
    def GoogleGroupAllInactive(self, ID_Login):
        return self._client.service.GoogleGroupAllInactive({"ID_Login": ID_Login})

    # Načíst seznam správců domény
    def DomainAdminAll(self, ID_Login, ID_Domain, ID, ID_Person):
        return self._client.service.DomainAdminAll({"ID_Login": ID_Login, "ID_Domain": ID_Domain, "ID": ID, "ID_Person": ID_Person})

    # Načíst seznam správců domény
    def DomainAdminAllPerson(self, ID_Login, ID_Domain, ID, ID_Person):
        return self._client.service.DomainAdminAllPerson({"ID_Login": ID_Login, "ID_Domain": ID_Domain, "ID": ID, "ID_Person": ID_Person})

    # Smazat správce domény
    def DomainAdminDelete(self, ID_Login, ID):
        return self._client.service.DomainAdminDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit správce domény
    def DomainAdminInsert(self, ID_Login, ID, ID_Domain, ID_Person, Domain=None, Person=None):
        return self._client.service.DomainAdminInsert({"ID_Login": ID_Login, "ID": ID, "ID_Domain": ID_Domain, "ID_Person": ID_Person, "Domain": Domain, "Person": Person})

    # Načíst seznam domén
    def DomainAll(self, ID_Login, ID, ID_Unit, DisplayName=None, ID_DomainState=None):
        return self._client.service.DomainAll({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DisplayName": DisplayName, "ID_DomainState": ID_DomainState})

    # Načíst seznam domén dostupné pro osobu
    def DomainAllPerson(self, ID_Login, ID_Person, CanGoogleAccount):
        return self._client.service.DomainAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person, "CanGoogleAccount": CanGoogleAccount})

    # Načíst seznam domén jednotky
    def DomainAllUnit(self, ID_Login, ID, ID_Unit, DisplayName=None, ID_DomainState=None):
        return self._client.service.DomainAllUnit({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DisplayName": DisplayName, "ID_DomainState": ID_DomainState})

    # Načíst seznam domén na kterých může uživatel založit účet pro danou jednotku
    def DomainAllUnitCreate(self, ID_Login, ID_Unit, CanGoogleAccount):
        return self._client.service.DomainAllUnitCreate({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "CanGoogleAccount": CanGoogleAccount})

    # Načíst detail domény
    def DomainDetail(self, ID_Login, ID):
        return self._client.service.DomainDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst emaily založené pod doménou
    def DomainDetailEmails(self, ID_Login, ID):
        return self._client.service.DomainDetailEmails({"ID_Login": ID_Login, "ID": ID})

    # Založit doménu
    def DomainInsert(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Načíst seznam stavů domény
    def DomainStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.DomainStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam jednotek přiřezené doméně
    def DomainUnitAll(self, ID_Login, ID_Domain, ID, ID_Unit):
        return self._client.service.DomainUnitAll({"ID_Login": ID_Login, "ID_Domain": ID_Domain, "ID": ID, "ID_Unit": ID_Unit})

    # Smazat jednotku přiřazenou doméně
    def DomainUnitDelete(self, ID_Login, ID):
        return self._client.service.DomainUnitDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit jednotku přiřazenou doméně
    def DomainUnitInsert(self, ID_Login, ID, ID_Domain, ID_Unit, IncludeChildUnit, Domain=None, Unit=None, RegistrationNumber=None):
        return self._client.service.DomainUnitInsert({"ID_Login": ID_Login, "ID": ID, "ID_Domain": ID_Domain, "ID_Unit": ID_Unit, "IncludeChildUnit": IncludeChildUnit, "Domain": Domain, "Unit": Unit, "RegistrationNumber": RegistrationNumber})

    # Upravit doménu
    def DomainUpdate(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Odeslat požadavek na doménu na ústředí
    def DomainUpdateActivate(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateActivate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Upravit alias domény
    def DomainUpdateAlias(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateAlias({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Odeslat požadavek na doménu na ústředí
    def DomainUpdateApprove(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateApprove({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Upravit DNS záznam domény
    def DomainUpdateDNS(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateDNS({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Zapnout GA na doméně
    def DomainUpdateEnableGA(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateEnableGA({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Odeslat požadavek na doménu na ústředí
    def DomainUpdateSend(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateSend({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Upravit kdo na doméně může zakládat účty
    def DomainUpdateUsing(self, ID_Login, ID, ID_Unit, ID_PersonCreated, OnlyMember, OnlyAfter15, OnlyCinovnik, OnlyAdminCreate, DateActivate, IsUsed, ID_PersonAdmin, ActivateGA, ID_DomainMain, ValidateDomain, ValidateAdmin, Hosting, DisplayName=None, Description=None, Unit=None, RegistrationNumber=None, ID_DomainState=None, DomainState=None, PersonCreated=None, Note=None, Alias=None, DNS=None):
        return self._client.service.DomainUpdateUsing({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_PersonCreated": ID_PersonCreated, "OnlyMember": OnlyMember, "OnlyAfter15": OnlyAfter15, "OnlyCinovnik": OnlyCinovnik, "OnlyAdminCreate": OnlyAdminCreate, "DateActivate": DateActivate, "IsUsed": IsUsed, "ID_PersonAdmin": ID_PersonAdmin, "ActivateGA": ActivateGA, "ID_DomainMain": ID_DomainMain, "ValidateDomain": ValidateDomain, "ValidateAdmin": ValidateAdmin, "Hosting": Hosting, "DisplayName": DisplayName, "Description": Description, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_DomainState": ID_DomainState, "DomainState": DomainState, "PersonCreated": PersonCreated, "Note": Note, "Alias": Alias, "DNS": DNS})

    # Načíst seznam kontaktů osoby
    def GoogleAccountAll(self, ID_Login, ID_Person, ID, IsMain):
        return self._client.service.GoogleAccountAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "IsMain": IsMain})

    # Načíst seznam kontaktů osoby
    def GoogleAccountAllUnit(self, ID_Login, ID_Unit, ID, IsMain, ID_GoogleAccountMain, IncludeChildUnits):
        return self._client.service.GoogleAccountAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "IsMain": IsMain, "ID_GoogleAccountMain": ID_GoogleAccountMain, "IncludeChildUnits": IncludeChildUnits})

    # Smazat účet v GA
    def GoogleAccountDelete(self, ID_Login, ID):
        return self._client.service.GoogleAccountDelete({"ID_Login": ID_Login, "ID": ID})

    # Smazat hlavni účet v GA
    def GoogleAccountDeleteMain(self, ID_Login, ID_Person, ID_GoogleAccount):
        return self._client.service.GoogleAccountDeleteMain({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_GoogleAccount": ID_GoogleAccount})

    # Načíst detail hlavního účtu jednotky v GA
    def GoogleAccountDetail(self, ID_Login, ID):
        return self._client.service.GoogleAccountDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam kontaktů osoby
    def GoogleAccountDetailExists(self, ID_Login, IsMain, OnlyDb, Email=None):
        return self._client.service.GoogleAccountDetailExists({"ID_Login": ID_Login, "IsMain": IsMain, "OnlyDb": OnlyDb, "Email": Email})

    # Načíst detail hlavního účtu osoby v GA
    def GoogleAccountDetailMain(self, ID_Login, ID_Person, LoadMainEmail):
        return self._client.service.GoogleAccountDetailMain({"ID_Login": ID_Login, "ID_Person": ID_Person, "LoadMainEmail": LoadMainEmail})

    # Založit účet v GA osobě
    def GoogleAccountInsert(self, ID_Login, ID, ID_Person, ID_Unit, ID_Domain, IsMain, IsMainContact, Agrees, ID_UnitContact, ID_PersonContact, ID_PersonCreated, DateCreated, ID_GoogleAccount, OnlyValidate, ShareAllAdded, StorageCapacity, IsAdult, Person=None, Unit=None, UserName=None, Domain=None, Password=None, Password2=None, PersonCreated=None, Value=None, LoginUrl=None, DisplayNameFirst=None, DisplayNameLast=None, OrgUnitPath=None):
        return self._client.service.GoogleAccountInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Domain": ID_Domain, "IsMain": IsMain, "IsMainContact": IsMainContact, "Agrees": Agrees, "ID_UnitContact": ID_UnitContact, "ID_PersonContact": ID_PersonContact, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "ID_GoogleAccount": ID_GoogleAccount, "OnlyValidate": OnlyValidate, "ShareAllAdded": ShareAllAdded, "StorageCapacity": StorageCapacity, "IsAdult": IsAdult, "Person": Person, "Unit": Unit, "UserName": UserName, "Domain": Domain, "Password": Password, "Password2": Password2, "PersonCreated": PersonCreated, "Value": Value, "LoginUrl": LoginUrl, "DisplayNameFirst": DisplayNameFirst, "DisplayNameLast": DisplayNameLast, "OrgUnitPath": OrgUnitPath})

    # Vynutit změnu hesla při dalším přihlášení do GA
    def GoogleAccountUpdateChangePassword(self, ID_Login, ID, ID_Person, ID_Unit, ID_Domain, IsMain, IsMainContact, Agrees, ID_UnitContact, ID_PersonContact, ID_PersonCreated, DateCreated, ID_GoogleAccount, OnlyValidate, ShareAllAdded, StorageCapacity, IsAdult, Person=None, Unit=None, UserName=None, Domain=None, Password=None, Password2=None, PersonCreated=None, Value=None, LoginUrl=None, DisplayNameFirst=None, DisplayNameLast=None, OrgUnitPath=None):
        return self._client.service.GoogleAccountUpdateChangePassword({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Domain": ID_Domain, "IsMain": IsMain, "IsMainContact": IsMainContact, "Agrees": Agrees, "ID_UnitContact": ID_UnitContact, "ID_PersonContact": ID_PersonContact, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "ID_GoogleAccount": ID_GoogleAccount, "OnlyValidate": OnlyValidate, "ShareAllAdded": ShareAllAdded, "StorageCapacity": StorageCapacity, "IsAdult": IsAdult, "Person": Person, "Unit": Unit, "UserName": UserName, "Domain": Domain, "Password": Password, "Password2": Password2, "PersonCreated": PersonCreated, "Value": Value, "LoginUrl": LoginUrl, "DisplayNameFirst": DisplayNameFirst, "DisplayNameLast": DisplayNameLast, "OrgUnitPath": OrgUnitPath})

    # Změna hesla
    def GoogleAccountUpdatePassword(self, ID_Login, ID, ID_Person, ID_Unit, ID_Domain, IsMain, IsMainContact, Agrees, ID_UnitContact, ID_PersonContact, ID_PersonCreated, DateCreated, ID_GoogleAccount, OnlyValidate, ShareAllAdded, StorageCapacity, IsAdult, Person=None, Unit=None, UserName=None, Domain=None, Password=None, Password2=None, PersonCreated=None, Value=None, LoginUrl=None, DisplayNameFirst=None, DisplayNameLast=None, OrgUnitPath=None):
        return self._client.service.GoogleAccountUpdatePassword({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Domain": ID_Domain, "IsMain": IsMain, "IsMainContact": IsMainContact, "Agrees": Agrees, "ID_UnitContact": ID_UnitContact, "ID_PersonContact": ID_PersonContact, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "ID_GoogleAccount": ID_GoogleAccount, "OnlyValidate": OnlyValidate, "ShareAllAdded": ShareAllAdded, "StorageCapacity": StorageCapacity, "IsAdult": IsAdult, "Person": Person, "Unit": Unit, "UserName": UserName, "Domain": Domain, "Password": Password, "Password2": Password2, "PersonCreated": PersonCreated, "Value": Value, "LoginUrl": LoginUrl, "DisplayNameFirst": DisplayNameFirst, "DisplayNameLast": DisplayNameLast, "OrgUnitPath": OrgUnitPath})

    # Načíst seznam google skupin
    def GoogleGroupAll(self, ID_Login, ID_Unit, ID, ID_GoogleGroupMain, IncludeChildUnits, DisplayName=None):
        return self._client.service.GoogleGroupAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_GoogleGroupMain": ID_GoogleGroupMain, "IncludeChildUnits": IncludeChildUnits, "DisplayName": DisplayName})

    # Smazat google skupinu
    def GoogleGroupDelete(self, ID_Login, ID):
        return self._client.service.GoogleGroupDelete({"ID_Login": ID_Login, "ID": ID})

    # Smazat uzivatele z google skupiny
    def GoogleGroupDeleteMember(self, ID_Login, ID, Email=None):
        return self._client.service.GoogleGroupDeleteMember({"ID_Login": ID_Login, "ID": ID, "Email": Email})

    # Načíst detail google skupiny
    def GoogleGroupDetail(self, ID_Login, ID):
        return self._client.service.GoogleGroupDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit google skupinu
    def GoogleGroupInsert(self, ID_Login, ID, ID_Unit, DateCreate, ID_GoogleGroupMain, ID_Domain, MemberCount, Valid, LastSync, IsAutoSync, DisplayName=None, Email=None, Unit=None, RegistrationNumber=None, GoogleGroupMainEmail=None, Description=None, EmailName=None, OwnerEmail=None, ID_SyncType=None, SyncType=None):
        return self._client.service.GoogleGroupInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreate": DateCreate, "ID_GoogleGroupMain": ID_GoogleGroupMain, "ID_Domain": ID_Domain, "MemberCount": MemberCount, "Valid": Valid, "LastSync": LastSync, "IsAutoSync": IsAutoSync, "DisplayName": DisplayName, "Email": Email, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GoogleGroupMainEmail": GoogleGroupMainEmail, "Description": Description, "EmailName": EmailName, "OwnerEmail": OwnerEmail, "ID_SyncType": ID_SyncType, "SyncType": SyncType})

    # Upravit google skupinu
    def GoogleGroupUpdate(self, ID_Login, ID, ID_Unit, DateCreate, ID_GoogleGroupMain, ID_Domain, MemberCount, Valid, LastSync, IsAutoSync, DisplayName=None, Email=None, Unit=None, RegistrationNumber=None, GoogleGroupMainEmail=None, Description=None, EmailName=None, OwnerEmail=None, ID_SyncType=None, SyncType=None):
        return self._client.service.GoogleGroupUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateCreate": DateCreate, "ID_GoogleGroupMain": ID_GoogleGroupMain, "ID_Domain": ID_Domain, "MemberCount": MemberCount, "Valid": Valid, "LastSync": LastSync, "IsAutoSync": IsAutoSync, "DisplayName": DisplayName, "Email": Email, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GoogleGroupMainEmail": GoogleGroupMainEmail, "Description": Description, "EmailName": EmailName, "OwnerEmail": OwnerEmail, "ID_SyncType": ID_SyncType, "SyncType": SyncType})

    # Uložit členy skupiny dle emailu
    def GoogleGroupUpdateMemberEmail(self, ID_Login, ID, EmailArray=None):
        return self._client.service.GoogleGroupUpdateMemberEmail({"ID_Login": ID_Login, "ID": ID, "EmailArray": EmailArray})

    # Uložit osobu jako člena skupiny
    def GoogleGroupUpdateMemberPerson(self, ID_Login, ID, ID_Person):
        return self._client.service.GoogleGroupUpdateMemberPerson({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Upravit roli uzivatele
    def GoogleGroupUpdateMemberRole(self, ID_Login, ID, IsOwner, Email=None):
        return self._client.service.GoogleGroupUpdateMemberRole({"ID_Login": ID_Login, "ID": ID, "IsOwner": IsOwner, "Email": Email})

