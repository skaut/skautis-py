# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s časopisy a fakturami
class Journal(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Journal.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Journal.asmx?wsdl')

    # Nastavit ID_Document se zipem
    def JournalCopyOrderUpdateDocument(self, ID_Login, ID, DateSent, ID_Journal, ID_Document, DisplayName=None, Journal=None, Message=None):
        return self._client.service.JournalCopyOrderUpdateDocument({"ID_Login": ID_Login, "ID": ID, "DateSent": DateSent, "ID_Journal": ID_Journal, "ID_Document": ID_Document, "DisplayName": DisplayName, "Journal": Journal, "Message": Message})

    # Načíst seznam výtisků časopisu v balíku
    def JournalCopyPackAll(self, ID_Login, JournalCopyRoot=None):
        return self._client.service.JournalCopyPackAll({"ID_Login": ID_Login, "JournalCopyRoot": JournalCopyRoot})

    # Načíst seznam fakturovaných časopisů
    def JournalCopySentAllIInvoiceSummaryVat(self, ID_Login, ID_Invoice):
        return self._client.service.JournalCopySentAllIInvoiceSummaryVat({"ID_Login": ID_Login, "ID_Invoice": ID_Invoice})

    # Načíst detail výtisku časopisu pro vrácený časopis
    def JournalCopySentDetailReturned(self, ID_Login, ID, IsPackage):
        return self._client.service.JournalCopySentDetailReturned({"ID_Login": ID_Login, "ID": ID, "IsPackage": IsPackage})

    # Načíst seznam typů doručení
    def JournalDeliveryTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.JournalDeliveryTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam způsobů odběru balíčků pro nováčky
    def JournalNoviceAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.JournalNoviceAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravi/vlozi odpoved na rovera
    def RoverJournalUpdate(self, ID_Login, ID, ID_Person, DateCreated, ID_RoverJournalYear, Person=None, ID_RoverJournalType=None, RoverJournalType=None):
        return self._client.service.RoverJournalUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "DateCreated": DateCreated, "ID_RoverJournalYear": ID_RoverJournalYear, "Person": Person, "ID_RoverJournalType": ID_RoverJournalType, "RoverJournalType": RoverJournalType})

    # Upozornění na osoby v roverském věku
    def RoverJournalWarning(self, ID_Login):
        return self._client.service.RoverJournalWarning({"ID_Login": ID_Login})

    # Načíst aktuální rok pro rovera
    def RoverJournalYearDetail(self, ID_Login):
        return self._client.service.RoverJournalYearDetail({"ID_Login": ID_Login})

    # Typ odpovědi
    def RoverJournalTypeAll(self, ID_Login, DisplayName=None, ID=None):
        return self._client.service.RoverJournalTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID": ID})

    # Změnit data odeslání u vybraných záznamů
    def JournalCopyVipUpdateDateSentId(self, ID_Login, DateSent, ID=None):
        return self._client.service.JournalCopyVipUpdateDateSentId({"ID_Login": ID_Login, "DateSent": DateSent, "ID": ID})

    # Načíst seznam objednávek časopisu
    def JournalCopyOrderAll(self, ID_Login, ID, ID_Journal):
        return self._client.service.JournalCopyOrderAll({"ID_Login": ID_Login, "ID": ID, "ID_Journal": ID_Journal})

    # Načíst detail objednávky časopisu
    def JournalCopyOrderDetail(self, ID_Login, ID):
        return self._client.service.JournalCopyOrderDetail({"ID_Login": ID_Login, "ID": ID})

    # No documentation
    def JournalCopyOrderItemAll(self, ID_Login, ID_JournalCopyOrder, ID, DisplayName=None):
        return self._client.service.JournalCopyOrderItemAll({"ID_Login": ID_Login, "ID_JournalCopyOrder": ID_JournalCopyOrder, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail položky objednávky časopisů
    def JournalCopyOrderItemDetail(self, ID_Login, ID):
        return self._client.service.JournalCopyOrderItemDetail({"ID_Login": ID_Login, "ID": ID})

    # Odeslat připravené zprávy
    def JournalCopyOrderUpdateSendMessage(self, ID_Login, ID, DateSent, ID_Journal, ID_Document, DisplayName=None, Journal=None, Message=None):
        return self._client.service.JournalCopyOrderUpdateSendMessage({"ID_Login": ID_Login, "ID": ID, "DateSent": DateSent, "ID_Journal": ID_Journal, "ID_Document": ID_Document, "DisplayName": DisplayName, "Journal": Journal, "Message": Message})

    # Vygenerovat soubory s rozesílkou a odeslat IZS
    def JournalCopyUpdateSendMessage(self, ID_Login, DateSent, SendMessage, OrderVIP):
        return self._client.service.JournalCopyUpdateSendMessage({"ID_Login": ID_Login, "DateSent": DateSent, "SendMessage": SendMessage, "OrderVIP": OrderVIP})

    # Načíst seznam VIP časopisů
    def JournalCopyVipAll(self, ID_Login, ID, ID_Person, ID_Journal, ID_JournalAttachment, ID_PersonCreate, DateSent, Person=None):
        return self._client.service.JournalCopyVipAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Journal": ID_Journal, "ID_JournalAttachment": ID_JournalAttachment, "ID_PersonCreate": ID_PersonCreate, "DateSent": DateSent, "Person": Person})

    # Smazat VIP časopis
    def JournalCopyVipDelete(self, ID_Login, ID):
        return self._client.service.JournalCopyVipDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail VIP časopisu
    def JournalCopyVipDetail(self, ID_Login, ID):
        return self._client.service.JournalCopyVipDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit VIP časopis
    def JournalCopyVipInsert(self, ID_Login, ID, ID_Person, ID_Journal, ID_JournalAttachment, DateSent, ID_PersonCreate, ValidTo, Person=None, Journal=None, JournalAttachment=None, PersonCreate=None, FirstLine=None, Street=None, City=None, Postcode=None):
        return self._client.service.JournalCopyVipInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Journal": ID_Journal, "ID_JournalAttachment": ID_JournalAttachment, "DateSent": DateSent, "ID_PersonCreate": ID_PersonCreate, "ValidTo": ValidTo, "Person": Person, "Journal": Journal, "JournalAttachment": JournalAttachment, "PersonCreate": PersonCreate, "FirstLine": FirstLine, "Street": Street, "City": City, "Postcode": Postcode})

    # Upravit VIP časopis
    def JournalCopyVipUpdate(self, ID_Login, ID, ID_Person, ID_Journal, ID_JournalAttachment, DateSent, ID_PersonCreate, ValidTo, Person=None, Journal=None, JournalAttachment=None, PersonCreate=None, FirstLine=None, Street=None, City=None, Postcode=None):
        return self._client.service.JournalCopyVipUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Journal": ID_Journal, "ID_JournalAttachment": ID_JournalAttachment, "DateSent": DateSent, "ID_PersonCreate": ID_PersonCreate, "ValidTo": ValidTo, "Person": Person, "Journal": Journal, "JournalAttachment": JournalAttachment, "PersonCreate": PersonCreate, "FirstLine": FirstLine, "Street": Street, "City": City, "Postcode": Postcode})

    # Upravit VIP časopis
    def JournalCopyVipUpdateDateSent(self, ID_Login, DateSentOld, DateSentNew):
        return self._client.service.JournalCopyVipUpdateDateSent({"ID_Login": ID_Login, "DateSentOld": DateSentOld, "DateSentNew": DateSentNew})

    # Zjistit zda osoba odebírá časopis
    def PersonJournalDetailExists(self, ID_Login, ID_Person, ID_Journal):
        return self._client.service.PersonJournalDetailExists({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Journal": ID_Journal})

    # Upozornění na změnu časopisů zdarma
    def PersonJournalWarningFree(self, ID_Login):
        return self._client.service.PersonJournalWarningFree({"ID_Login": ID_Login})

    # Načíst fakturu v pdf
    def InvoiceDetailPdf(self, ID_Login, ID):
        return self._client.service.InvoiceDetailPdf({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam faktur v xml
    def InvoiceAllXml(self, ID_Login, ID, DateGeneratingFrom, DateGeneratingTo, ID_InvoiceState=None):
        return self._client.service.InvoiceAllXml({"ID_Login": ID_Login, "ID": ID, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "ID_InvoiceState": ID_InvoiceState})

    # Načíst seznam faktur v xml zabalenych do zipu
    def InvoiceAllZip(self, ID_Login, DateGeneratingFrom, DateGeneratingTo, ID_InvoiceState=None):
        return self._client.service.InvoiceAllZip({"ID_Login": ID_Login, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "ID_InvoiceState": ID_InvoiceState})

    # Smazat připravenou rozesílku
    def JournalCopyDeleteOne(self, ID_Login, ID_Journal, DateSent, DisplayName=None):
        return self._client.service.JournalCopyDeleteOne({"ID_Login": ID_Login, "ID_Journal": ID_Journal, "DateSent": DateSent, "DisplayName": DisplayName})

    # Změnit časopisy Zdarma dle věkové kategorie
    def PersonJournalChangeFree(self, ID_Login):
        return self._client.service.PersonJournalChangeFree({"ID_Login": ID_Login})

    # Načíst seznam odeslaných výtisků časopisů
    def JournalCopySentAll(self, ID_Login, ID_Person, ID_Unit, ID_Journal, ID_JournalCopySent, DisplayName=None):
        return self._client.service.JournalCopySentAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "ID_JournalCopySent": ID_JournalCopySent, "DisplayName": DisplayName})

    # Načíst seznam Stavů faktury
    def InvoiceStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.InvoiceStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst detail odeslaného výtisku časopisu
    def JournalCopySentDetail(self, ID_Login, ID):
        return self._client.service.JournalCopySentDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam vrácených časopisů jednotky
    def JournalReturnedAll(self, ID_Login, ID_Unit, ID_JournalCopySent, ID_JournalReturnedReason=None):
        return self._client.service.JournalReturnedAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_JournalCopySent": ID_JournalCopySent, "ID_JournalReturnedReason": ID_JournalReturnedReason})

    # Založit vrácený časopis
    def JournalReturnedInsert(self, ID_Login, ID_JournalCopySent, DateCreate, OnlyValidate, JournalCopySent=None, ID_JournalReturnedReason=None, Note=None):
        return self._client.service.JournalReturnedInsert({"ID_Login": ID_Login, "ID_JournalCopySent": ID_JournalCopySent, "DateCreate": DateCreate, "OnlyValidate": OnlyValidate, "JournalCopySent": JournalCopySent, "ID_JournalReturnedReason": ID_JournalReturnedReason, "Note": Note})

    # Načíst seznam důvodů nedoručitelnosti
    def JournalReturnedReasonAll(self, ID_Login, IsPackage, DisplayName=None):
        return self._client.service.JournalReturnedReasonAll({"ID_Login": ID_Login, "IsPackage": IsPackage, "DisplayName": DisplayName})

    # Načte počet zbývajících příloh zdarma
    def PersonJournalFreeAttachments(self, ID_Login, ID_Unit):
        return self._client.service.PersonJournalFreeAttachments({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načíst seznam faktur podle stavu
    def InvoiceAllInvoiceState(self, ID_Login, ID_InvoiceState=None):
        return self._client.service.InvoiceAllInvoiceState({"ID_Login": ID_Login, "ID_InvoiceState": ID_InvoiceState})

    # Ukončit ročník
    def JournalCopyUpdateCloseYear(self, ID_Login):
        return self._client.service.JournalCopyUpdateCloseYear({"ID_Login": ID_Login})

    # Načíst seznam faktur jednotky
    def InvoiceAllUnit(self, ID_Login, ID_Unit, DateGeneratingFrom, DateGeneratingTo, DisplayName=None, ID_InvoiceState=None):
        return self._client.service.InvoiceAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "DisplayName": DisplayName, "ID_InvoiceState": ID_InvoiceState})

    # Upravit fakturu
    def InvoiceUpdate(self, ID_Login, ID, ID_Unit, IsVatPayer, DateGenerating, Maturity, Sequence, ID_Person, TotalPrice, TotalPriceWithVat, Price, PriceBase, PriceFirst, PriceSecond, VatBase, VatFirst, VatSecond, ID_InvoiceGroup, DateTaxableSupply, DisplayName=None, Unit=None, Street=None, City=None, Postcode=None, State=None, StateCode=None, IC=None, DIC=None, ID_InvoiceState=None, InvoiceState=None, Person=None, QRCodeString=None, InvoiceGroupContractorIC=None, InvoiceGroupContractorDIC=None, InvoiceGroupContractorPhone=None, InvoiceGroupContractorEmail=None, InvoiceGroupWeb=None, InvoiceGroupFileReference=None, InvoiceGroupBankAccount=None, InvoiceGroupBankCode=None, InvoiceGroupBank=None, PaymentType=None, InvoiceGroupContractor=None, InvoiceGroupContractorAddress=None):
        return self._client.service.InvoiceUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "IsVatPayer": IsVatPayer, "DateGenerating": DateGenerating, "Maturity": Maturity, "Sequence": Sequence, "ID_Person": ID_Person, "TotalPrice": TotalPrice, "TotalPriceWithVat": TotalPriceWithVat, "Price": Price, "PriceBase": PriceBase, "PriceFirst": PriceFirst, "PriceSecond": PriceSecond, "VatBase": VatBase, "VatFirst": VatFirst, "VatSecond": VatSecond, "ID_InvoiceGroup": ID_InvoiceGroup, "DateTaxableSupply": DateTaxableSupply, "DisplayName": DisplayName, "Unit": Unit, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "StateCode": StateCode, "IC": IC, "DIC": DIC, "ID_InvoiceState": ID_InvoiceState, "InvoiceState": InvoiceState, "Person": Person, "QRCodeString": QRCodeString, "InvoiceGroupContractorIC": InvoiceGroupContractorIC, "InvoiceGroupContractorDIC": InvoiceGroupContractorDIC, "InvoiceGroupContractorPhone": InvoiceGroupContractorPhone, "InvoiceGroupContractorEmail": InvoiceGroupContractorEmail, "InvoiceGroupWeb": InvoiceGroupWeb, "InvoiceGroupFileReference": InvoiceGroupFileReference, "InvoiceGroupBankAccount": InvoiceGroupBankAccount, "InvoiceGroupBankCode": InvoiceGroupBankCode, "InvoiceGroupBank": InvoiceGroupBank, "PaymentType": PaymentType, "InvoiceGroupContractor": InvoiceGroupContractor, "InvoiceGroupContractorAddress": InvoiceGroupContractorAddress})

    # Načíst seznam fakturovaných časopisů
    def JournalCopySentAllInvoice(self, ID_Login, ID_Invoice):
        return self._client.service.JournalCopySentAllInvoice({"ID_Login": ID_Login, "ID_Invoice": ID_Invoice})

    # Načíst seznam faktur
    def InvoiceAll(self, ID_Login, ID_Unit, DateGeneratingFrom, DateGeneratingTo, DisplayName=None, ID_InvoiceState=None):
        return self._client.service.InvoiceAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "DisplayName": DisplayName, "ID_InvoiceState": ID_InvoiceState})

    # Načíst detail faktury
    def InvoiceDetail(self, ID_Login, ID):
        return self._client.service.InvoiceDetail({"ID_Login": ID_Login, "ID": ID})

    # Vygenerovat faktury za rozeslané a dosud neuhrazené časopisy
    def InvoiceInsert(self, ID_Login, AllUnits, ID_Unit, DateGenerating, Maturity):
        return self._client.service.InvoiceInsert({"ID_Login": ID_Login, "AllUnits": AllUnits, "ID_Unit": ID_Unit, "DateGenerating": DateGenerating, "Maturity": Maturity})

    # Číselník datumů odeslání připravených zásilek
    def JournalCopyALLDateSent(self, ID_Login):
        return self._client.service.JournalCopyALLDateSent({"ID_Login": ID_Login})

    # Přidat speciální zásilku
    def JournalCopyInsertSpecial(self, ID_Login, DateSent, AgeFrom, AgeTo, HasPreparedJournal, IsInsert, FunctionTypeNegation, RoverJournal, AlignmentTypeNegation, JournalParent, DisplayName=None, ID_FunctionTypeArray=None, ID_SexUnit=None, ID_TroopArtArray=None, ID_AlignmentTypeArray=None, ID_MembershipCategoryArray=None, ID_JournalArray=None, Note=None, ID_MembershipCategoryPersonNumberArray=None, ID_PersonNumberArray=None, IsAdultStem=None):
        return self._client.service.JournalCopyInsertSpecial({"ID_Login": ID_Login, "DateSent": DateSent, "AgeFrom": AgeFrom, "AgeTo": AgeTo, "HasPreparedJournal": HasPreparedJournal, "IsInsert": IsInsert, "FunctionTypeNegation": FunctionTypeNegation, "RoverJournal": RoverJournal, "AlignmentTypeNegation": AlignmentTypeNegation, "JournalParent": JournalParent, "DisplayName": DisplayName, "ID_FunctionTypeArray": ID_FunctionTypeArray, "ID_SexUnit": ID_SexUnit, "ID_TroopArtArray": ID_TroopArtArray, "ID_AlignmentTypeArray": ID_AlignmentTypeArray, "ID_MembershipCategoryArray": ID_MembershipCategoryArray, "ID_JournalArray": ID_JournalArray, "Note": Note, "ID_MembershipCategoryPersonNumberArray": ID_MembershipCategoryPersonNumberArray, "ID_PersonNumberArray": ID_PersonNumberArray, "IsAdultStem": IsAdultStem})

    # Přehled titulů připravených k rozesílce
    def JournalCopyAllSummary(self, ID_Login):
        return self._client.service.JournalCopyAllSummary({"ID_Login": ID_Login})

    # Smazat připravenou rozesílku
    def JournalCopyDelete(self, ID_Login):
        return self._client.service.JournalCopyDelete({"ID_Login": ID_Login})

    # Přidat časopis do rozesílky
    def JournalCopyInsert(self, ID_Login, ID_Journal, DateSent, Price, ID_VatRate, DisplayName=None):
        return self._client.service.JournalCopyInsert({"ID_Login": ID_Login, "ID_Journal": ID_Journal, "DateSent": DateSent, "Price": Price, "ID_VatRate": ID_VatRate, "DisplayName": DisplayName})

    # Generovat seznam adres k rozesílce
    def JournalCopyUpdateGenerate(self, ID_Login, DateSent, CreateOrder, OrderVIP):
        return self._client.service.JournalCopyUpdateGenerate({"ID_Login": ID_Login, "DateSent": DateSent, "CreateOrder": CreateOrder, "OrderVIP": OrderVIP})

    # Nastavit připravenou zásilku jako odeslanou
    def JournalCopyUpdateSent(self, ID_Login):
        return self._client.service.JournalCopyUpdateSent({"ID_Login": ID_Login})

    # Načíst detail titulu časopisu
    def JournalDetail(self, ID_Login, ID):
        return self._client.service.JournalDetail({"ID_Login": ID_Login, "ID": ID})

    # Objednat přílohu zdarma
    def PersonJournalInsertUnit(self, ID_Login, ID_Person, ValidFrom, ValidTo, ID, ID_Unit, ID_Journal, IsFree, IsAuthorized, IsPaid, IsNovice, Person=None, Unit=None, Journal=None, ID_JournalType=None, JournalType=None, ID_JournalDeliveryType=None, JournalDeliveryType=None, Key=None):
        return self._client.service.PersonJournalInsertUnit({"ID_Login": ID_Login, "ID_Person": ID_Person, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID": ID, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "IsFree": IsFree, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "IsNovice": IsNovice, "Person": Person, "Unit": Unit, "Journal": Journal, "ID_JournalType": ID_JournalType, "JournalType": JournalType, "ID_JournalDeliveryType": ID_JournalDeliveryType, "JournalDeliveryType": JournalDeliveryType, "Key": Key})

    # Načíst seznam objednaných časopisů
    def PersonJournalAllUnit(self, ID_Login, ID_Unit, ID_Person, ID_Journal, ShowHistory, IncludeChild, IncludeAttachmentCount, IsValid):
        return self._client.service.PersonJournalAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ID_Journal": ID_Journal, "ShowHistory": ShowHistory, "IncludeChild": IncludeChild, "IncludeAttachmentCount": IncludeAttachmentCount, "IsValid": IsValid})

    # Načíst seznam titulů časopisů
    def JournalAll(self, ID_Login, HideAttachment, DisplayName=None, ID_JournalType=None):
        return self._client.service.JournalAll({"ID_Login": ID_Login, "HideAttachment": HideAttachment, "DisplayName": DisplayName, "ID_JournalType": ID_JournalType})

    # Načíst seznam výtisků časopisů
    def JournalCopyAll(self, ID_Login, ID_Person, ID_Unit, ID_Journal, ID_JournalCopy, DisplayName=None):
        return self._client.service.JournalCopyAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "ID_JournalCopy": ID_JournalCopy, "DisplayName": DisplayName})

    # Načíst seznam objednaných časopisů
    def PersonJournalAll(self, ID_Login, ID_Person, ID_Unit, ID_Journal, ShowHistory, IsValid):
        return self._client.service.PersonJournalAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "ShowHistory": ShowHistory, "IsValid": IsValid})

    # Smazat objednaný časopis
    def PersonJournalDelete(self, ID_Login, ID, DeleteAttachment):
        return self._client.service.PersonJournalDelete({"ID_Login": ID_Login, "ID": ID, "DeleteAttachment": DeleteAttachment})

    # Načíst detail objednaného časopisu
    def PersonJournalDetail(self, ID_Login, ID):
        return self._client.service.PersonJournalDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit objednaný časopis
    def PersonJournalInsert(self, ID_Login, ID_Person, ValidFrom, ValidTo, ID, ID_Unit, ID_Journal, IsFree, IsAuthorized, IsPaid, IsNovice, Person=None, Unit=None, Journal=None, ID_JournalType=None, JournalType=None, ID_JournalDeliveryType=None, JournalDeliveryType=None, Key=None):
        return self._client.service.PersonJournalInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID": ID, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "IsFree": IsFree, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "IsNovice": IsNovice, "Person": Person, "Unit": Unit, "Journal": Journal, "ID_JournalType": ID_JournalType, "JournalType": JournalType, "ID_JournalDeliveryType": ID_JournalDeliveryType, "JournalDeliveryType": JournalDeliveryType, "Key": Key})

    # Upravit objednaný časopis
    def PersonJournalUpdate(self, ID_Login, ID_Person, ValidFrom, ValidTo, ID, ID_Unit, ID_Journal, IsFree, IsAuthorized, IsPaid, IsNovice, Person=None, Unit=None, Journal=None, ID_JournalType=None, JournalType=None, ID_JournalDeliveryType=None, JournalDeliveryType=None, Key=None):
        return self._client.service.PersonJournalUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID": ID, "ID_Unit": ID_Unit, "ID_Journal": ID_Journal, "IsFree": IsFree, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "IsNovice": IsNovice, "Person": Person, "Unit": Unit, "Journal": Journal, "ID_JournalType": ID_JournalType, "JournalType": JournalType, "ID_JournalDeliveryType": ID_JournalDeliveryType, "JournalDeliveryType": JournalDeliveryType, "Key": Key})

