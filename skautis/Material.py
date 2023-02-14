# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s materiálem a sklady
class Material(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Material.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Material.asmx?wsdl')

    # Převod položek do skladu
    def WarehouseItemUpdateTransfer(self, ID_Login, ID_Warehouse, WarehouseItems=None):
        return self._client.service.WarehouseItemUpdateTransfer({"ID_Login": ID_Login, "ID_Warehouse": ID_Warehouse, "WarehouseItems": WarehouseItems})

    # Načíst seznam typu pořízení
    def PurchaseTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.PurchaseTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam inventur
    def StockTakingAll(self, ID_Login, ID_Unit, ID, ID_Person, ID_DocumentStockTaking, ID_DocumentProtocol, OpenOnly, ID_StockTakingState=None):
        return self._client.service.StockTakingAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_Person": ID_Person, "ID_DocumentStockTaking": ID_DocumentStockTaking, "ID_DocumentProtocol": ID_DocumentProtocol, "OpenOnly": OpenOnly, "ID_StockTakingState": ID_StockTakingState})

    # Smazat inventuru
    def StockTakingDelete(self, ID_Login, ID):
        return self._client.service.StockTakingDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail inventury
    def StockTakingDetail(self, ID_Login, ID):
        return self._client.service.StockTakingDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit inventuru
    def StockTakingInsert(self, WarehouseList=None):
        return self._client.service.StockTakingInsert({"WarehouseList": WarehouseList})

    # Načíst seznam stavů inventury
    def StockTakingStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.StockTakingStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů inventarizace
    def StockTakingTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.StockTakingTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit stav inventury
    def StockTakingUpdateState(self, ID_Login, ID, ID_Person, Date, Created, ID_DocumentStockTaking, ID_DocumentProtocol, ID_DocumentStockTakingTempFile, ID_DocumentProtocolTempFile, ID_Unit, ID_StockTakingState=None, StockTakingState=None, ID_StockTakingType=None, StockTakingType=None, Person=None, Note=None, DocumentStockTaking=None, DocumentProtocol=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Warehouses=None):
        return self._client.service.StockTakingUpdateState({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Date": Date, "Created": Created, "ID_DocumentStockTaking": ID_DocumentStockTaking, "ID_DocumentProtocol": ID_DocumentProtocol, "ID_DocumentStockTakingTempFile": ID_DocumentStockTakingTempFile, "ID_DocumentProtocolTempFile": ID_DocumentProtocolTempFile, "ID_Unit": ID_Unit, "ID_StockTakingState": ID_StockTakingState, "StockTakingState": StockTakingState, "ID_StockTakingType": ID_StockTakingType, "StockTakingType": StockTakingType, "Person": Person, "Note": Note, "DocumentStockTaking": DocumentStockTaking, "DocumentProtocol": DocumentProtocol, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Warehouses": Warehouses})

    # Upravit inventuru
    def StockTakingUpdate(self, ID_Login, ID, ID_Person, Date, Created, ID_DocumentStockTaking, ID_DocumentProtocol, ID_DocumentStockTakingTempFile, ID_DocumentProtocolTempFile, ID_Unit, ID_StockTakingState=None, StockTakingState=None, ID_StockTakingType=None, StockTakingType=None, Person=None, Note=None, DocumentStockTaking=None, DocumentProtocol=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Warehouses=None):
        return self._client.service.StockTakingUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Date": Date, "Created": Created, "ID_DocumentStockTaking": ID_DocumentStockTaking, "ID_DocumentProtocol": ID_DocumentProtocol, "ID_DocumentStockTakingTempFile": ID_DocumentStockTakingTempFile, "ID_DocumentProtocolTempFile": ID_DocumentProtocolTempFile, "ID_Unit": ID_Unit, "ID_StockTakingState": ID_StockTakingState, "StockTakingState": StockTakingState, "ID_StockTakingType": ID_StockTakingType, "StockTakingType": StockTakingType, "Person": Person, "Note": Note, "DocumentStockTaking": DocumentStockTaking, "DocumentProtocol": DocumentProtocol, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Warehouses": Warehouses})

    # Načíst seznam inventarizovaných položek skladu
    def StockTakingWarehouseItemAll(self, ID_Login, ID_StockTaking, ID, ID_WarehouseItem):
        return self._client.service.StockTakingWarehouseItemAll({"ID_Login": ID_Login, "ID_StockTaking": ID_StockTaking, "ID": ID, "ID_WarehouseItem": ID_WarehouseItem})

    # Smazat inventarizovanou položku skladu
    def StockTakingWarehouseItemDelete(self, ID_Login, ID):
        return self._client.service.StockTakingWarehouseItemDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit inventarizovanou položku skladu
    def StockTakingWarehouseItemInsert(self, ID_Login, ID_StockTaking, ID_WarehouseItem, WarehouseItems=None, Note=None):
        return self._client.service.StockTakingWarehouseItemInsert({"ID_Login": ID_Login, "ID_StockTaking": ID_StockTaking, "ID_WarehouseItem": ID_WarehouseItem, "WarehouseItems": WarehouseItems, "Note": Note})

    # Načíst seznam správců skladu
    def WarehouseAdminAll(self, ID_Login, ID_Event, ID_EventEducation, ID_EventGeneral, ID, ID_Person):
        return self._client.service.WarehouseAdminAll({"ID_Login": ID_Login, "ID_Event": ID_Event, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID": ID, "ID_Person": ID_Person})

    # Smazat správce skladu
    def WarehouseAdminDelete(self, ID_Login, ID):
        return self._client.service.WarehouseAdminDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit správce skladu
    def WarehouseAdminInsert(self, ID_Login, ID, ID_Event, ID_EventEducation, ID_EventGeneral, ID_Person, Event=None, Person=None, Note=None):
        return self._client.service.WarehouseAdminInsert({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID_Person": ID_Person, "Event": Event, "Person": Person, "Note": Note})

    # Načíst seznam skladů
    def WarehouseAllProperty(self, ID_Login, ID_Unit, IsChildIncluded):
        return self._client.service.WarehouseAllProperty({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsChildIncluded": IsChildIncluded})

    # Načíst seznam skladů inventury jednotky
    def WarehouseAllStockTakingUnit(self, ID_Login, ID_Unit, IsChildIncluded):
        return self._client.service.WarehouseAllStockTakingUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsChildIncluded": IsChildIncluded})

    # Načíst seznam skladů k inventuře jednotky
    def WarehouseAllStockTaking(self, ID_Login, ID_StockTaking, ID_Warehouse):
        return self._client.service.WarehouseAllStockTaking({"ID_Login": ID_Login, "ID_StockTaking": ID_StockTaking, "ID_Warehouse": ID_Warehouse})

    # Načíst seznam skladů
    def WarehouseAllEvent(self, ID_Login, ID_EventEducation, ID_EventGeneral, ID, ID_WarehouseMain, ID_District, IsChildIncluded, DisplayName=None, ID_WarehouseType=None):
        return self._client.service.WarehouseAllEvent({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID": ID, "ID_WarehouseMain": ID_WarehouseMain, "ID_District": ID_District, "IsChildIncluded": IsChildIncluded, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType})

    # Načíst seznam skladů, ze kterých si můžu půjčovat
    def WarehouseAllBorrowable(self, ID_Login):
        return self._client.service.WarehouseAllBorrowable({"ID_Login": ID_Login})

    # Smazat sklad
    def WarehouseDelete(self, ID_Login, ID):
        return self._client.service.WarehouseDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam štítků položek
    def WarehouseItemAllBarcode(self, ID_Login, ID_Items=None):
        return self._client.service.WarehouseItemAllBarcode({"ID_Login": ID_Login, "ID_Items": ID_Items})

    # Načíst seznam položek k likvidaci inventurizace jednotky
    def WarehouseItemAllStockTakingDiscarded(self, ID_Login, ID_StockTaking, ID_Warehouse):
        return self._client.service.WarehouseItemAllStockTakingDiscarded({"ID_Login": ID_Login, "ID_StockTaking": ID_StockTaking, "ID_Warehouse": ID_Warehouse})

    # Načíst seznam položek inventurizace jednotky
    def WarehouseItemAllStockTaking(self, ID_Login, ID_StockTaking, ID_Warehouse):
        return self._client.service.WarehouseItemAllStockTaking({"ID_Login": ID_Login, "ID_StockTaking": ID_StockTaking, "ID_Warehouse": ID_Warehouse})

    # Načíst seznam položek jednotky
    def WarehouseItemAllEvent(self, ID_Login, ID_EventEducation, ID_EventGeneral, ID, IncludeChild, EventRent, UnitRent, CommercialRent, IsDelete, InWarehouse, Count, RowMin, Reverse, DisplayName=None, InventoryNumber=None, ID_WarehouseArray=None, ID_WarehouseTagArray=None, Sort=None, ID_WarehouseItemCategory=None):
        return self._client.service.WarehouseItemAllEvent({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID": ID, "IncludeChild": IncludeChild, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "IsDelete": IsDelete, "InWarehouse": InWarehouse, "Count": Count, "RowMin": RowMin, "Reverse": Reverse, "DisplayName": DisplayName, "InventoryNumber": InventoryNumber, "ID_WarehouseArray": ID_WarehouseArray, "ID_WarehouseTagArray": ID_WarehouseTagArray, "Sort": Sort, "ID_WarehouseItemCategory": ID_WarehouseItemCategory})

    # Načíst seznam všech položek skladu, které si lze zapůjčit
    def WarehouseItemAllBorrowable(self, ID_Login, ID_Application, MaxPrice, IsInStock, IsCommercial, DateFrom, DateTo, Keyword=None, Category=None, District=None, Region=None, City=None):
        return self._client.service.WarehouseItemAllBorrowable({"ID_Login": ID_Login, "ID_Application": ID_Application, "MaxPrice": MaxPrice, "IsInStock": IsInStock, "IsCommercial": IsCommercial, "DateFrom": DateFrom, "DateTo": DateTo, "Keyword": Keyword, "Category": Category, "District": District, "Region": Region, "City": City})

    # Načíst vypůjčené položky a rezervace
    def WarehouseItemAllLent(self, ID_Login, ID_Unit, ID, IncludeChild, EventRent, UnitRent, CommercialRent, IsDelete, InWarehouse, Count, RowMin, Reverse, ShowActive, ShowOnlyUnfinished, DisplayName=None, InventoryNumber=None, ID_WarehouseArray=None, ID_WarehouseTagArray=None, Sort=None, ID_WarehouseItemCategory=None):
        return self._client.service.WarehouseItemAllLent({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "IncludeChild": IncludeChild, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "IsDelete": IsDelete, "InWarehouse": InWarehouse, "Count": Count, "RowMin": RowMin, "Reverse": Reverse, "ShowActive": ShowActive, "ShowOnlyUnfinished": ShowOnlyUnfinished, "DisplayName": DisplayName, "InventoryNumber": InventoryNumber, "ID_WarehouseArray": ID_WarehouseArray, "ID_WarehouseTagArray": ID_WarehouseTagArray, "Sort": Sort, "ID_WarehouseItemCategory": ID_WarehouseItemCategory})

    # Načíst seznam položek jednotky
    def WarehouseItemAll(self, ID_Login, ID_Unit, ID, IncludeChild, EventRent, UnitRent, CommercialRent, IsDelete, InWarehouse, Count, RowMin, Reverse, ID_Items=None, DisplayName=None, InventoryNumber=None, ID_WarehouseArray=None, ID_WarehouseTagArray=None, Sort=None, ID_WarehouseItemCategory=None):
        return self._client.service.WarehouseItemAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "IncludeChild": IncludeChild, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "IsDelete": IsDelete, "InWarehouse": InWarehouse, "Count": Count, "RowMin": RowMin, "Reverse": Reverse, "ID_Items": ID_Items, "DisplayName": DisplayName, "InventoryNumber": InventoryNumber, "ID_WarehouseArray": ID_WarehouseArray, "ID_WarehouseTagArray": ID_WarehouseTagArray, "Sort": Sort, "ID_WarehouseItemCategory": ID_WarehouseItemCategory})

    # Načíst názvy položek
    def WarehouseItemAllDisplayName(self, ID_Login, ID=None):
        return self._client.service.WarehouseItemAllDisplayName({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam kategorií
    def WarehouseItemCategoryAllWithIntend(self, ID_Login, ID=None):
        return self._client.service.WarehouseItemCategoryAllWithIntend({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam kategorií
    def WarehouseItemCategoryAll(self, ID_Login, ID=None, DisplayName=None, ID_WarehouseItemCategoryParent=None):
        return self._client.service.WarehouseItemCategoryAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "ID_WarehouseItemCategoryParent": ID_WarehouseItemCategoryParent})

    # No documentation
    def WarehouseItemDelete(self, ID_Login, ID):
        return self._client.service.WarehouseItemDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail položky
    def WarehouseItemDetail(self, ID_Login, ID):
        return self._client.service.WarehouseItemDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail položky
    def WarehouseItemDetailPhoto(self, ID_Login, ID_Application, ID, Size=None):
        return self._client.service.WarehouseItemDetailPhoto({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "Size": Size})

    # Založit položku
    def WarehouseItemInsert(self, ID_Login, ID, ID_Unit, ID_Event, ID_Warehouse, ID_TempFile, ID_Document, PurchaseDate, PurchaseYear, PurchasePrice, ActualPrice, DeletionDate, EventRent, UnitRent, CommercialRent, RentPrice, InWarehouse, InventoryDate, EventName=None, DisplayName=None, Warehouse=None, ID_WarehouseItemCategory=None, WarehouseItemCategory=None, InventoryNumber=None, Description=None, FileExtension=None, ID_PurchaseType=None, PurchaseType=None, PurchaseNote=None, SerialNumber=None, Sails=None, AccountNumber=None, DeletionNote=None, RentNote=None, Note=None, Tags=None, WarehouseRentNote=None, WarehouseTag=None, InventoryNote=None):
        return self._client.service.WarehouseItemInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_Warehouse": ID_Warehouse, "ID_TempFile": ID_TempFile, "ID_Document": ID_Document, "PurchaseDate": PurchaseDate, "PurchaseYear": PurchaseYear, "PurchasePrice": PurchasePrice, "ActualPrice": ActualPrice, "DeletionDate": DeletionDate, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "RentPrice": RentPrice, "InWarehouse": InWarehouse, "InventoryDate": InventoryDate, "EventName": EventName, "DisplayName": DisplayName, "Warehouse": Warehouse, "ID_WarehouseItemCategory": ID_WarehouseItemCategory, "WarehouseItemCategory": WarehouseItemCategory, "InventoryNumber": InventoryNumber, "Description": Description, "FileExtension": FileExtension, "ID_PurchaseType": ID_PurchaseType, "PurchaseType": PurchaseType, "PurchaseNote": PurchaseNote, "SerialNumber": SerialNumber, "Sails": Sails, "AccountNumber": AccountNumber, "DeletionNote": DeletionNote, "RentNote": RentNote, "Note": Note, "Tags": Tags, "WarehouseRentNote": WarehouseRentNote, "WarehouseTag": WarehouseTag, "InventoryNote": InventoryNote})

    # Načíst seznam inventur
    def WarehouseItemInventoryAll(self, ID_Login, ID_WarehouseItem, ID, ID_Person):
        return self._client.service.WarehouseItemInventoryAll({"ID_Login": ID_Login, "ID_WarehouseItem": ID_WarehouseItem, "ID": ID, "ID_Person": ID_Person})

    # Založit inventuru
    def WarehouseItemInventoryInsert(self, ID_Login, ID, ID_WarehouseItem, ID_Person, Date, WarehouseItem=None, Person=None, Note=None):
        return self._client.service.WarehouseItemInventoryInsert({"ID_Login": ID_Login, "ID": ID, "ID_WarehouseItem": ID_WarehouseItem, "ID_Person": ID_Person, "Date": Date, "WarehouseItem": WarehouseItem, "Person": Person, "Note": Note})

    # Smazat výpůjčku
    def WarehouseItemRentDelete(self, ID_Login, ID_WarehouseItem=None):
        return self._client.service.WarehouseItemRentDelete({"ID_Login": ID_Login, "ID_WarehouseItem": ID_WarehouseItem})

    # Založit výpůjčku
    def WarehouseItemRentInsert(self, ID_Login, ID_WarehouseItemReservation, StartDate, EndDate, ID_WarehouseItem=None, Note=None):
        return self._client.service.WarehouseItemRentInsert({"ID_Login": ID_Login, "ID_WarehouseItemReservation": ID_WarehouseItemReservation, "StartDate": StartDate, "EndDate": EndDate, "ID_WarehouseItem": ID_WarehouseItem, "Note": Note})

    # Načíst seznam typů půjčení
    def WarehouseItemRentTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.WarehouseItemRentTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit výpůjčku
    def WarehouseItemRentUpdate(self, ID_Login, ID, ID_WarehouseItem, StartDate, EndDate, IsActive, WarehouseItem=None, Note=None):
        return self._client.service.WarehouseItemRentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_WarehouseItem": ID_WarehouseItem, "StartDate": StartDate, "EndDate": EndDate, "IsActive": IsActive, "WarehouseItem": WarehouseItem, "Note": Note})

    # Načíst seznam tagů položek
    def WarehouseItemTagAll(self, ID_Login, ID_WarehouseItem, ID, ID_WarehouseTag):
        return self._client.service.WarehouseItemTagAll({"ID_Login": ID_Login, "ID_WarehouseItem": ID_WarehouseItem, "ID": ID, "ID_WarehouseTag": ID_WarehouseTag})

    # Upravit položku
    def WarehouseItemUpdateBatch(self, ID_Login, ID, ID_Unit, ID_Event, ID_Warehouse, ID_TempFile, ID_Document, PurchaseDate, PurchaseYear, PurchasePrice, ActualPrice, DeletionDate, EventRent, UnitRent, CommercialRent, RentPrice, InWarehouse, InventoryDate, EventName=None, DisplayName=None, Warehouse=None, ID_WarehouseItemCategory=None, WarehouseItemCategory=None, InventoryNumber=None, Description=None, FileExtension=None, ID_PurchaseType=None, PurchaseType=None, PurchaseNote=None, SerialNumber=None, Sails=None, AccountNumber=None, DeletionNote=None, RentNote=None, Note=None, Tags=None, WarehouseRentNote=None, WarehouseTag=None, InventoryNote=None):
        return self._client.service.WarehouseItemUpdateBatch({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_Warehouse": ID_Warehouse, "ID_TempFile": ID_TempFile, "ID_Document": ID_Document, "PurchaseDate": PurchaseDate, "PurchaseYear": PurchaseYear, "PurchasePrice": PurchasePrice, "ActualPrice": ActualPrice, "DeletionDate": DeletionDate, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "RentPrice": RentPrice, "InWarehouse": InWarehouse, "InventoryDate": InventoryDate, "EventName": EventName, "DisplayName": DisplayName, "Warehouse": Warehouse, "ID_WarehouseItemCategory": ID_WarehouseItemCategory, "WarehouseItemCategory": WarehouseItemCategory, "InventoryNumber": InventoryNumber, "Description": Description, "FileExtension": FileExtension, "ID_PurchaseType": ID_PurchaseType, "PurchaseType": PurchaseType, "PurchaseNote": PurchaseNote, "SerialNumber": SerialNumber, "Sails": Sails, "AccountNumber": AccountNumber, "DeletionNote": DeletionNote, "RentNote": RentNote, "Note": Note, "Tags": Tags, "WarehouseRentNote": WarehouseRentNote, "WarehouseTag": WarehouseTag, "InventoryNote": InventoryNote})

    # Vyřadit položku
    def WarehouseItemUpdateDelete(self, ID_Login, DeletionDate, ID=None, DeletionNote=None):
        return self._client.service.WarehouseItemUpdateDelete({"ID_Login": ID_Login, "DeletionDate": DeletionDate, "ID": ID, "DeletionNote": DeletionNote})

    # Upravit fotografii u položky
    def WarehouseItemUpdatePhoto(self, ID_Login, ID, ID_Unit, ID_Event, ID_Warehouse, ID_TempFile, ID_Document, PurchaseDate, PurchaseYear, PurchasePrice, ActualPrice, DeletionDate, EventRent, UnitRent, CommercialRent, RentPrice, InWarehouse, InventoryDate, EventName=None, DisplayName=None, Warehouse=None, ID_WarehouseItemCategory=None, WarehouseItemCategory=None, InventoryNumber=None, Description=None, FileExtension=None, ID_PurchaseType=None, PurchaseType=None, PurchaseNote=None, SerialNumber=None, Sails=None, AccountNumber=None, DeletionNote=None, RentNote=None, Note=None, Tags=None, WarehouseRentNote=None, WarehouseTag=None, InventoryNote=None):
        return self._client.service.WarehouseItemUpdatePhoto({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_Warehouse": ID_Warehouse, "ID_TempFile": ID_TempFile, "ID_Document": ID_Document, "PurchaseDate": PurchaseDate, "PurchaseYear": PurchaseYear, "PurchasePrice": PurchasePrice, "ActualPrice": ActualPrice, "DeletionDate": DeletionDate, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "RentPrice": RentPrice, "InWarehouse": InWarehouse, "InventoryDate": InventoryDate, "EventName": EventName, "DisplayName": DisplayName, "Warehouse": Warehouse, "ID_WarehouseItemCategory": ID_WarehouseItemCategory, "WarehouseItemCategory": WarehouseItemCategory, "InventoryNumber": InventoryNumber, "Description": Description, "FileExtension": FileExtension, "ID_PurchaseType": ID_PurchaseType, "PurchaseType": PurchaseType, "PurchaseNote": PurchaseNote, "SerialNumber": SerialNumber, "Sails": Sails, "AccountNumber": AccountNumber, "DeletionNote": DeletionNote, "RentNote": RentNote, "Note": Note, "Tags": Tags, "WarehouseRentNote": WarehouseRentNote, "WarehouseTag": WarehouseTag, "InventoryNote": InventoryNote})

    # Upravit položku
    def WarehouseItemUpdate(self, DeletePhoto):
        return self._client.service.WarehouseItemUpdate({"DeletePhoto": DeletePhoto})

    # Upravit více položek
    def WarehouseItemUpdateMulti(self, ID_Login, ID=None, DisplayName=None, Description=None, ID_WarehouseItemCategory=None, ID_Warehouse=None, InventoryNumber=None, SerialNumber=None, PurchaseDate=None, PurchasePrice=None, ID_PurchaseType=None, PurchaseNote=None, ActualPrice=None, AccountNumber=None, DeletionDate=None, DeletionNote=None, EventRent=None, UnitRent=None, CommercialRent=None, RentPrice=None, RentNote=None, Note=None, ID_TempFilePhoto=None):
        return self._client.service.WarehouseItemUpdateMulti({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "Description": Description, "ID_WarehouseItemCategory": ID_WarehouseItemCategory, "ID_Warehouse": ID_Warehouse, "InventoryNumber": InventoryNumber, "SerialNumber": SerialNumber, "PurchaseDate": PurchaseDate, "PurchasePrice": PurchasePrice, "ID_PurchaseType": ID_PurchaseType, "PurchaseNote": PurchaseNote, "ActualPrice": ActualPrice, "AccountNumber": AccountNumber, "DeletionDate": DeletionDate, "DeletionNote": DeletionNote, "EventRent": EventRent, "UnitRent": UnitRent, "CommercialRent": CommercialRent, "RentPrice": RentPrice, "RentNote": RentNote, "Note": Note, "ID_TempFilePhoto": ID_TempFilePhoto})

    # Načíst seznam inventarizovaných skladu
    def WarehouseStockTakingAll(self, ID_Login, ID_Warehouse, ID, ID_StockTaking):
        return self._client.service.WarehouseStockTakingAll({"ID_Login": ID_Login, "ID_Warehouse": ID_Warehouse, "ID": ID, "ID_StockTaking": ID_StockTaking})

    # Smazat inventarizovaný skladu
    def WarehouseStockTakingDelete(self, ID_Login, ID):
        return self._client.service.WarehouseStockTakingDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit inventarizovaný skladu
    def WarehouseStockTakingInsert(self, ID_Login, ID, ID_Warehouse, ID_StockTaking, Warehouse=None, Note=None):
        return self._client.service.WarehouseStockTakingInsert({"ID_Login": ID_Login, "ID": ID, "ID_Warehouse": ID_Warehouse, "ID_StockTaking": ID_StockTaking, "Warehouse": Warehouse, "Note": Note})

    # Načíst seznam tagů
    def WarehouseTagAllUniversal(self, ID_Login, ID_EventEducation, ID_EventGeneral, ID_Unit, ID, DisplayName=None):
        return self._client.service.WarehouseTagAllUniversal({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID_Unit": ID_Unit, "ID": ID, "DisplayName": DisplayName})

    # Založit tag
    def WarehouseTagInsertEvent(self, ID_Login, ID, ID_Unit, ID_EventEducation, ID_EventGeneral, ID_Event, ID_Warehouse, CanUpdate, DisplayName=None, Unit=None, Event=None, RegistrationNumber=None, Color=None, Warehouse=None):
        return self._client.service.WarehouseTagInsertEvent({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID_Event": ID_Event, "ID_Warehouse": ID_Warehouse, "CanUpdate": CanUpdate, "DisplayName": DisplayName, "Unit": Unit, "Event": Event, "RegistrationNumber": RegistrationNumber, "Color": Color, "Warehouse": Warehouse})

    # Upravit platnost skladu
    def WarehouseUpdateEnabled(self, ID_Login, ID, ID_Unit, ID_Event, ID_WarehouseMain, IsDefault, ID_District, GpsLatitude, GpsLongitude, CanUpdate, ID_UnitCentral, IsEnabled, DisplayName=None, ID_WarehouseType=None, WarehouseType=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Event=None, WarehouseMain=None, Street=None, City=None, District=None, Postcode=None, Note=None, UnitCentral=None, UnitCentralFullName=None, UnitCentralRegistrationNumber=None):
        return self._client.service.WarehouseUpdateEnabled({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_WarehouseMain": ID_WarehouseMain, "IsDefault": IsDefault, "ID_District": ID_District, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "CanUpdate": CanUpdate, "ID_UnitCentral": ID_UnitCentral, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType, "WarehouseType": WarehouseType, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Event": Event, "WarehouseMain": WarehouseMain, "Street": Street, "City": City, "District": District, "Postcode": Postcode, "Note": Note, "UnitCentral": UnitCentral, "UnitCentralFullName": UnitCentralFullName, "UnitCentralRegistrationNumber": UnitCentralRegistrationNumber})

    # Načíst seznam skladů
    def WarehouseAll(self, ID_Login, ID_Unit, ID, ID_Event, ID_WarehouseMain, ID_District, IsChildIncluded, IsEnabled, DisplayName=None, ID_WarehouseType=None):
        return self._client.service.WarehouseAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_Event": ID_Event, "ID_WarehouseMain": ID_WarehouseMain, "ID_District": ID_District, "IsChildIncluded": IsChildIncluded, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType})

    # Načíst detail skladu
    def WarehouseDetail(self, ID_Login, ID):
        return self._client.service.WarehouseDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit sklad
    def WarehouseInsert(self, ID_Login, ID, ID_Unit, ID_Event, ID_WarehouseMain, IsDefault, ID_District, GpsLatitude, GpsLongitude, CanUpdate, ID_UnitCentral, IsEnabled, DisplayName=None, ID_WarehouseType=None, WarehouseType=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Event=None, WarehouseMain=None, Street=None, City=None, District=None, Postcode=None, Note=None, UnitCentral=None, UnitCentralFullName=None, UnitCentralRegistrationNumber=None):
        return self._client.service.WarehouseInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_WarehouseMain": ID_WarehouseMain, "IsDefault": IsDefault, "ID_District": ID_District, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "CanUpdate": CanUpdate, "ID_UnitCentral": ID_UnitCentral, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType, "WarehouseType": WarehouseType, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Event": Event, "WarehouseMain": WarehouseMain, "Street": Street, "City": City, "District": District, "Postcode": Postcode, "Note": Note, "UnitCentral": UnitCentral, "UnitCentralFullName": UnitCentralFullName, "UnitCentralRegistrationNumber": UnitCentralRegistrationNumber})

    # Načíst seznam tagů
    def WarehouseTagAll(self, ID_Login, ID_Unit, ID, ID_Warehouse, IncludeChild, UniqueOnly, DisplayName=None):
        return self._client.service.WarehouseTagAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_Warehouse": ID_Warehouse, "IncludeChild": IncludeChild, "UniqueOnly": UniqueOnly, "DisplayName": DisplayName})

    # Smazat tag
    def WarehouseTagDelete(self, ID_Login, ID, ID_Warehouse):
        return self._client.service.WarehouseTagDelete({"ID_Login": ID_Login, "ID": ID, "ID_Warehouse": ID_Warehouse})

    # Načíst detail tagu
    def WarehouseTagDetail(self, ID_Login, ID):
        return self._client.service.WarehouseTagDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit tag
    def WarehouseTagInsert(self, ID_Login, ID_Unit, DisplayName=None, Color=None, ID_Warehouse=None):
        return self._client.service.WarehouseTagInsert({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "DisplayName": DisplayName, "Color": Color, "ID_Warehouse": ID_Warehouse})

    # Upravit tag
    def WarehouseTagUpdate(self, ID_Login, ID, ID_Unit, ID_EventEducation, ID_EventGeneral, ID_Event, ID_Warehouse, CanUpdate, DisplayName=None, Unit=None, Event=None, RegistrationNumber=None, Color=None, Warehouse=None):
        return self._client.service.WarehouseTagUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_EventEducation": ID_EventEducation, "ID_EventGeneral": ID_EventGeneral, "ID_Event": ID_Event, "ID_Warehouse": ID_Warehouse, "CanUpdate": CanUpdate, "DisplayName": DisplayName, "Unit": Unit, "Event": Event, "RegistrationNumber": RegistrationNumber, "Color": Color, "Warehouse": Warehouse})

    # Načíst seznam typů skladů
    def WarehouseTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.WarehouseTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Nastavit sklad jako výchozí
    def WarehouseUpdateIsDefault(self, ID_Login, ID, ID_Unit, ID_Event, ID_WarehouseMain, IsDefault, ID_District, GpsLatitude, GpsLongitude, CanUpdate, ID_UnitCentral, IsEnabled, DisplayName=None, ID_WarehouseType=None, WarehouseType=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Event=None, WarehouseMain=None, Street=None, City=None, District=None, Postcode=None, Note=None, UnitCentral=None, UnitCentralFullName=None, UnitCentralRegistrationNumber=None):
        return self._client.service.WarehouseUpdateIsDefault({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_WarehouseMain": ID_WarehouseMain, "IsDefault": IsDefault, "ID_District": ID_District, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "CanUpdate": CanUpdate, "ID_UnitCentral": ID_UnitCentral, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType, "WarehouseType": WarehouseType, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Event": Event, "WarehouseMain": WarehouseMain, "Street": Street, "City": City, "District": District, "Postcode": Postcode, "Note": Note, "UnitCentral": UnitCentral, "UnitCentralFullName": UnitCentralFullName, "UnitCentralRegistrationNumber": UnitCentralRegistrationNumber})

    # Upravit sklad
    def WarehouseUpdate(self, ID_Login, ID, ID_Unit, ID_Event, ID_WarehouseMain, IsDefault, ID_District, GpsLatitude, GpsLongitude, CanUpdate, ID_UnitCentral, IsEnabled, DisplayName=None, ID_WarehouseType=None, WarehouseType=None, Unit=None, UnitFullName=None, RegistrationNumber=None, Event=None, WarehouseMain=None, Street=None, City=None, District=None, Postcode=None, Note=None, UnitCentral=None, UnitCentralFullName=None, UnitCentralRegistrationNumber=None):
        return self._client.service.WarehouseUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_WarehouseMain": ID_WarehouseMain, "IsDefault": IsDefault, "ID_District": ID_District, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "CanUpdate": CanUpdate, "ID_UnitCentral": ID_UnitCentral, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_WarehouseType": ID_WarehouseType, "WarehouseType": WarehouseType, "Unit": Unit, "UnitFullName": UnitFullName, "RegistrationNumber": RegistrationNumber, "Event": Event, "WarehouseMain": WarehouseMain, "Street": Street, "City": City, "District": District, "Postcode": Postcode, "Note": Note, "UnitCentral": UnitCentral, "UnitCentralFullName": UnitCentralFullName, "UnitCentralRegistrationNumber": UnitCentralRegistrationNumber})

