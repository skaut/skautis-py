# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s dokumentovým úložištěm
class DocumentStorage(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/DocumentStorage.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/DocumentStorage.asmx?wsdl')

    # Načíst seznam cloudových záznamů
    def CloudAll(self, ID_Login, ID, ID_DocumentVersion, ID_CloudState=None):
        return self._client.service.CloudAll({"ID_Login": ID_Login, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "ID_CloudState": ID_CloudState})

    # Smazat cloudový záznam
    def CloudDelete(self, ID_Login, ID):
        return self._client.service.CloudDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail cloudového záznamu
    def CloudDetail(self, ID_Login, ID):
        return self._client.service.CloudDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam cache cloudového záznamu
    def CloudFolderCacheAll(self, ID_Login, ID_DocumentVersion=None):
        return self._client.service.CloudFolderCacheAll({"ID_Login": ID_Login, "ID_DocumentVersion": ID_DocumentVersion})

    # Založit cache cloudového záznamu
    def CloudFolderCacheInsert(self, ID_Login, ID, Date, Path=None, CloudGuid=None):
        return self._client.service.CloudFolderCacheInsert({"ID_Login": ID_Login, "ID": ID, "Date": Date, "Path": Path, "CloudGuid": CloudGuid})

    # Založit cloudový záznam
    def CloudInsert(self, ID_Login, ID_Application, ID, ID_DocumentVersion, ValidTo, DocumentVersion=None, ID_CloudState=None, CloudState=None, CloudGuid=None):
        return self._client.service.CloudInsert({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "ValidTo": ValidTo, "DocumentVersion": DocumentVersion, "ID_CloudState": ID_CloudState, "CloudState": CloudState, "CloudGuid": CloudGuid})

    # Načíst seznam požadavků na dokument
    def CloudRequestAll(self, ID_Login, ID_Cloud, ID, ID_User):
        return self._client.service.CloudRequestAll({"ID_Login": ID_Login, "ID_Cloud": ID_Cloud, "ID": ID, "ID_User": ID_User})

    # Smazat požadavek na dokument
    def CloudRequestDelete(self, ID_Login, ID):
        return self._client.service.CloudRequestDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail požadavku na dokument
    def CloudRequestDetail(self, ID_Login, ID):
        return self._client.service.CloudRequestDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit požadavek na dokument
    def CloudRequestInsert(self, ID_Login, ID, ID_User, ID_Cloud):
        return self._client.service.CloudRequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Cloud": ID_Cloud})

    # Upravit požadavek na dokument
    def CloudRequestUpdate(self, ID_Login, ID, ID_User, ID_Cloud):
        return self._client.service.CloudRequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Cloud": ID_Cloud})

    # Načíst seznam stavů záznamu (v Cloudu)
    def CloudStateAll(self, ID_Application, ID_Login, ID=None, DisplayName=None):
        return self._client.service.CloudStateAll({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail stavu záznamu (v Cloudu)
    def CloudStateDetail(self, ID_Login, ID=None):
        return self._client.service.CloudStateDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit cloudový záznam
    def CloudUpdateDocumentVersion(self, ID_Login, ID_Application, ID, ID_DocumentVersion, ValidTo, DocumentVersion=None, ID_CloudState=None, CloudState=None, CloudGuid=None):
        return self._client.service.CloudUpdateDocumentVersion({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "ValidTo": ValidTo, "DocumentVersion": DocumentVersion, "ID_CloudState": ID_CloudState, "CloudState": CloudState, "CloudGuid": CloudGuid})

    # Upravit cloudový záznam
    def CloudUpdate(self, ID_Login, ID_Application, ID, ID_DocumentVersion, ValidTo, DocumentVersion=None, ID_CloudState=None, CloudState=None, CloudGuid=None):
        return self._client.service.CloudUpdate({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "ValidTo": ValidTo, "DocumentVersion": DocumentVersion, "ID_CloudState": ID_CloudState, "CloudState": CloudState, "CloudGuid": CloudGuid})

    # Načíst seznam dokumentů
    def DocumentAllUnused(self, ID_Login):
        return self._client.service.DocumentAllUnused({"ID_Login": ID_Login})

    # Načíst seznam dokumentů
    def DocumentAll(self, ID_Application, ID_Login, ID, ID_DocumentVersion, ID_DocumentClass=None):
        return self._client.service.DocumentAll({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "ID_DocumentClass": ID_DocumentClass})

    # Načíst seznam tříd dokumentu
    def DocumentClassAll(self, ID_Application, ID_Login, ID=None, DisplayName=None, ID_Table=None, ID_ActionDetail=None, ID_ActionEdit=None, ID_ActionDel=None):
        return self._client.service.DocumentClassAll({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "ID_Table": ID_Table, "ID_ActionDetail": ID_ActionDetail, "ID_ActionEdit": ID_ActionEdit, "ID_ActionDel": ID_ActionDel})

    # Načíst detail třídy dokumentu
    def DocumentClassDetail(self, ID_Login, ID=None):
        return self._client.service.DocumentClassDetail({"ID_Login": ID_Login, "ID": ID})

    # Smazat dokument
    def DocumentDelete(self, ID_Login, ID, CheckPermissions):
        return self._client.service.DocumentDelete({"ID_Login": ID_Login, "ID": ID, "CheckPermissions": CheckPermissions})

    # Načíst data dokumentu
    def DocumentDetailData(self, ID_Application, ID_Login, ID):
        return self._client.service.DocumentDetailData({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID})

    # Načíst detail dokumentu
    def DocumentDetail(self, ID_Application, ID_Login, ID):
        return self._client.service.DocumentDetail({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID})

    # Založit dokument
    def DocumentInsert(self, ID_Login, ID, ID_DocumentVersion, Created, Date, ID_Document, ID_User, ID_Person, Size, Version, ImageWidth, ImageHeight, UseCurrentVersion, ID_Cloud, CloudValidTo, DocumentVersion=None, ID_DocumentClass=None, DocumentClass=None, DisplayName=None, Person=None, FileName=None, ContentType=None, Extension=None, Hash=None, Storage=None, FileNameExtension=None, ID_CloudState=None, CloudGuid=None):
        return self._client.service.DocumentInsert({"ID_Login": ID_Login, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "Created": Created, "Date": Date, "ID_Document": ID_Document, "ID_User": ID_User, "ID_Person": ID_Person, "Size": Size, "Version": Version, "ImageWidth": ImageWidth, "ImageHeight": ImageHeight, "UseCurrentVersion": UseCurrentVersion, "ID_Cloud": ID_Cloud, "CloudValidTo": CloudValidTo, "DocumentVersion": DocumentVersion, "ID_DocumentClass": ID_DocumentClass, "DocumentClass": DocumentClass, "DisplayName": DisplayName, "Person": Person, "FileName": FileName, "ContentType": ContentType, "Extension": Extension, "Hash": Hash, "Storage": Storage, "FileNameExtension": FileNameExtension, "ID_CloudState": ID_CloudState, "CloudGuid": CloudGuid})

    # Smazat dokument v tabulce
    def DocumentDeleteDocumentInTable(self, ID_Login, ID, ID_DocumentClass=None, Table=None, TableAction=None, Column=None):
        return self._client.service.DocumentDeleteDocumentInTable({"ID_Login": ID_Login, "ID": ID, "ID_DocumentClass": ID_DocumentClass, "Table": Table, "TableAction": TableAction, "Column": Column})

    # Upravit dokument v tabulce
    def DocumentUpdateDocumentInTable(self, ID_Login, ID, ID_TempFile, MoveDocument, ID_RelatedTable, ID_DocumentClass=None, Table=None, TableAction=None, Column=None):
        return self._client.service.DocumentUpdateDocumentInTable({"ID_Login": ID_Login, "ID": ID, "ID_TempFile": ID_TempFile, "MoveDocument": MoveDocument, "ID_RelatedTable": ID_RelatedTable, "ID_DocumentClass": ID_DocumentClass, "Table": Table, "TableAction": TableAction, "Column": Column})

    # Upravit dokument
    def DocumentUpdate(self, ID_Login, ID, ID_DocumentVersion, Created, Date, ID_Document, ID_User, ID_Person, Size, Version, ImageWidth, ImageHeight, UseCurrentVersion, ID_Cloud, CloudValidTo, DocumentVersion=None, ID_DocumentClass=None, DocumentClass=None, DisplayName=None, Person=None, FileName=None, ContentType=None, Extension=None, Hash=None, Storage=None, FileNameExtension=None, ID_CloudState=None, CloudGuid=None):
        return self._client.service.DocumentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_DocumentVersion": ID_DocumentVersion, "Created": Created, "Date": Date, "ID_Document": ID_Document, "ID_User": ID_User, "ID_Person": ID_Person, "Size": Size, "Version": Version, "ImageWidth": ImageWidth, "ImageHeight": ImageHeight, "UseCurrentVersion": UseCurrentVersion, "ID_Cloud": ID_Cloud, "CloudValidTo": CloudValidTo, "DocumentVersion": DocumentVersion, "ID_DocumentClass": ID_DocumentClass, "DocumentClass": DocumentClass, "DisplayName": DisplayName, "Person": Person, "FileName": FileName, "ContentType": ContentType, "Extension": Extension, "Hash": Hash, "Storage": Storage, "FileNameExtension": FileNameExtension, "ID_CloudState": ID_CloudState, "CloudGuid": CloudGuid})

    # Načíst seznam verzí dokumentu
    def DocumentVersionAllToBackup(self, ID_Login):
        return self._client.service.DocumentVersionAllToBackup({"ID_Login": ID_Login})

    # Načíst seznam verzí dokumentu
    def DocumentVersionAll(self, ID_Login, ID, ID_Document, ID_User, DisplayName=None):
        return self._client.service.DocumentVersionAll({"ID_Login": ID_Login, "ID": ID, "ID_Document": ID_Document, "ID_User": ID_User, "DisplayName": DisplayName})

    # Smazat verzi dokumentu
    def DocumentVersionDelete(self, ID_Login, ID):
        return self._client.service.DocumentVersionDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail verze dokumentu
    def DocumentVersionDetail(self, ID_Login, ID):
        return self._client.service.DocumentVersionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit verzi dokumentu
    def DocumentVersionInsert(self, ID_Login, ID, Date, ID_Document, ID_User, Size, Version, ImageWidth, ImageHeight, DisplayName=None, FileName=None, ContentType=None, Extension=None, Hash=None, Storage=None, FileNameExtension=None):
        return self._client.service.DocumentVersionInsert({"ID_Login": ID_Login, "ID": ID, "Date": Date, "ID_Document": ID_Document, "ID_User": ID_User, "Size": Size, "Version": Version, "ImageWidth": ImageWidth, "ImageHeight": ImageHeight, "DisplayName": DisplayName, "FileName": FileName, "ContentType": ContentType, "Extension": Extension, "Hash": Hash, "Storage": Storage, "FileNameExtension": FileNameExtension})

    # Upravit verzi dokumentu
    def DocumentVersionUpdate(self, ID_Login, ID, Date, ID_Document, ID_User, Size, Version, ImageWidth, ImageHeight, DisplayName=None, FileName=None, ContentType=None, Extension=None, Hash=None, Storage=None, FileNameExtension=None):
        return self._client.service.DocumentVersionUpdate({"ID_Login": ID_Login, "ID": ID, "Date": Date, "ID_Document": ID_Document, "ID_User": ID_User, "Size": Size, "Version": Version, "ImageWidth": ImageWidth, "ImageHeight": ImageHeight, "DisplayName": DisplayName, "FileName": FileName, "ContentType": ContentType, "Extension": Extension, "Hash": Hash, "Storage": Storage, "FileNameExtension": FileNameExtension})

