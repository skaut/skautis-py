# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s organizačními jednotkami a osobami
class OrganizationUnit(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/OrganizationUnit.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/OrganizationUnit.asmx?wsdl')

    # Načíst seznam pohlaví
    def SexAll(self, ID_Login, ID_Application, DisplayName=None):
        return self._client.service.SexAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "DisplayName": DisplayName})

    # Načíst seznam hospodářských výkazů
    def StatementAll(self, ID_Login, ID_Unit, Year, ID_StatementType=None):
        return self._client.service.StatementAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "Year": Year, "ID_StatementType": ID_StatementType})

    # Smazat hospodářský výkaz
    def StatementDelete(self, ID_Login, ID):
        return self._client.service.StatementDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail hospodářského výkazu
    def StatementDetail(self, ID_Login, ID):
        return self._client.service.StatementDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam položek hospodářského výkazu
    def StatementEntryAll(self, ID_Login, ID_Statement, ID_StatementEntryType, IsMoney):
        return self._client.service.StatementEntryAll({"ID_Login": ID_Login, "ID_Statement": ID_Statement, "ID_StatementEntryType": ID_StatementEntryType, "IsMoney": IsMoney})

    # Načíst seznam závěrkových položky
    def StatementEntryTypeAll(self, ID_Login, DisplayName=None, ID_StatementType=None):
        return self._client.service.StatementEntryTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_StatementType": ID_StatementType})

    # Upravit položku hospodářského výkazu
    def StatementEntryUpdate(self, ID_Login, ID, ID_Statement, ID_StatementEntryType, Amount, AmountLastYear, AmountMain, AmountEconomic):
        return self._client.service.StatementEntryUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Statement": ID_Statement, "ID_StatementEntryType": ID_StatementEntryType, "Amount": Amount, "AmountLastYear": AmountLastYear, "AmountMain": AmountMain, "AmountEconomic": AmountEconomic})

    # Založit hospodářský výkaz
    def StatementInsert(self, ID_Login, ID, ID_Unit, Year, IsError, IsDelivered, DateDelivered, DateCreated, IsThousands, IsConsultant, ID_Document, ID_DocumentTempFile, DateSent, ID_PersonSent, DateConfirmed, ID_PersonConfirmed, ID_Registry, ShowOverview, Unit=None, RegistrationNumber=None, ID_StatementType=None, StatementType=None, ID_StatementState=None, StatementState=None, PersonSent=None, PersonConfirmed=None):
        return self._client.service.StatementInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "IsError": IsError, "IsDelivered": IsDelivered, "DateDelivered": DateDelivered, "DateCreated": DateCreated, "IsThousands": IsThousands, "IsConsultant": IsConsultant, "ID_Document": ID_Document, "ID_DocumentTempFile": ID_DocumentTempFile, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "DateConfirmed": DateConfirmed, "ID_PersonConfirmed": ID_PersonConfirmed, "ID_Registry": ID_Registry, "ShowOverview": ShowOverview, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StatementType": ID_StatementType, "StatementType": StatementType, "ID_StatementState": ID_StatementState, "StatementState": StatementState, "PersonSent": PersonSent, "PersonConfirmed": PersonConfirmed})

    # Načíst seznam typů hospodářského výkazu
    def StatementTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.StatementTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit hospodářský výkaz
    def StatementUpdate(self, ID_Login, ID, ID_Unit, Year, IsError, IsDelivered, DateDelivered, DateCreated, IsThousands, IsConsultant, ID_Document, ID_DocumentTempFile, DateSent, ID_PersonSent, DateConfirmed, ID_PersonConfirmed, ID_Registry, ShowOverview, Unit=None, RegistrationNumber=None, ID_StatementType=None, StatementType=None, ID_StatementState=None, StatementState=None, PersonSent=None, PersonConfirmed=None):
        return self._client.service.StatementUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "IsError": IsError, "IsDelivered": IsDelivered, "DateDelivered": DateDelivered, "DateCreated": DateCreated, "IsThousands": IsThousands, "IsConsultant": IsConsultant, "ID_Document": ID_Document, "ID_DocumentTempFile": ID_DocumentTempFile, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "DateConfirmed": DateConfirmed, "ID_PersonConfirmed": ID_PersonConfirmed, "ID_Registry": ID_Registry, "ShowOverview": ShowOverview, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StatementType": ID_StatementType, "StatementType": StatementType, "ID_StatementState": ID_StatementState, "StatementState": StatementState, "PersonSent": PersonSent, "PersonConfirmed": PersonConfirmed})

    # Načíst seznam  typů oddílu
    def TroopArtAll(self, ID_Login, DisplayName=None):
        return self._client.service.TroopArtAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam jednotek
    def UnitAll(self, ID_Login, ID_Application, ID, ID_Group, ID_UnitParent, ID_UnitChild, ID_UnitTree, RegistrationNumberStartWith, ID_AlignmentType, ID_UnitType=None, RegistrationNumber=None, DisplayName=None, Location=None, AccountNumber=None, IC=None, Email=None, Phone=None):
        return self._client.service.UnitAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_Group": ID_Group, "ID_UnitParent": ID_UnitParent, "ID_UnitChild": ID_UnitChild, "ID_UnitTree": ID_UnitTree, "RegistrationNumberStartWith": RegistrationNumberStartWith, "ID_AlignmentType": ID_AlignmentType, "ID_UnitType": ID_UnitType, "RegistrationNumber": RegistrationNumber, "DisplayName": DisplayName, "Location": Location, "AccountNumber": AccountNumber, "IC": IC, "Email": Email, "Phone": Phone})

    # Načíst seznam kontaktů jednotky
    def UnitContactAll(self, ID_Login, ID_Application, ID_Unit, Publish, ID_ContactType=None):
        return self._client.service.UnitContactAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "Publish": Publish, "ID_ContactType": ID_ContactType})

    # Smazat kontakt jednotky
    def UnitContactDelete(self, ID_Login, ID):
        return self._client.service.UnitContactDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit kontakt jednotky
    def UnitContactInsert(self, ID_Login, ID_Unit, ID, Publish, ID_ContactType=None, Value=None, Note=None):
        return self._client.service.UnitContactInsert({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "Publish": Publish, "ID_ContactType": ID_ContactType, "Value": Value, "Note": Note})

    # Upravit kontakt jednotky
    def UnitContactUpdate(self, ID_Login, ID_Unit, ID, Publish, ID_ContactType=None, Value=None, Note=None):
        return self._client.service.UnitContactUpdate({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "Publish": Publish, "ID_ContactType": ID_ContactType, "Value": Value, "Note": Note})

    # Založit podřízenou jednotku
    def UnitInsertUnit(self, ID_Login, ID, ID_Group, ID_Unit, ContainsMembers, CommissionDeadline, IsVatPayer, ID_TroopArt, CanUpdateRegistrationNumber, ID_DocumentLogo, IsUnitCancel, JournalParent, ChangeFreeJournal, ID_UnitParent, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, ID_PersonChangeName, DateChangeName, IsPropertyOwner, ID_TempFilePropertyAgreement, ID_DocumentDecision, ID_DocumentPropertyAgreement, ID_TempFileSeatChange, ID_TempFileUnitLogo, ID_UnitType=None, UnitType=None, DisplayName=None, SortName=None, RegistrationNumber=None, ShortRegistrationNumber=None, Location=None, LocationNew=None, IC=None, DIC=None, FileReference=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, TroopArt=None, LogoContent=None, LogoExtension=None, AddressDistrict=None, PostalDistrict=None, NewDisplayName=None, CompleteDisplayName=None, PersonChangeName=None, PropertyAgreementExtension=None, PropertyAgreementContent=None, TroopArtKey=None, ID_JournalNovice=None, ID_JournalDeliveryType=None, FullDisplayName=None, DecisionSeatChangeExtension=None, ShopDiscountBarcode=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitInsertUnit({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_Unit": ID_Unit, "ContainsMembers": ContainsMembers, "CommissionDeadline": CommissionDeadline, "IsVatPayer": IsVatPayer, "ID_TroopArt": ID_TroopArt, "CanUpdateRegistrationNumber": CanUpdateRegistrationNumber, "ID_DocumentLogo": ID_DocumentLogo, "IsUnitCancel": IsUnitCancel, "JournalParent": JournalParent, "ChangeFreeJournal": ChangeFreeJournal, "ID_UnitParent": ID_UnitParent, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_PersonChangeName": ID_PersonChangeName, "DateChangeName": DateChangeName, "IsPropertyOwner": IsPropertyOwner, "ID_TempFilePropertyAgreement": ID_TempFilePropertyAgreement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "ID_TempFileSeatChange": ID_TempFileSeatChange, "ID_TempFileUnitLogo": ID_TempFileUnitLogo, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "DisplayName": DisplayName, "SortName": SortName, "RegistrationNumber": RegistrationNumber, "ShortRegistrationNumber": ShortRegistrationNumber, "Location": Location, "LocationNew": LocationNew, "IC": IC, "DIC": DIC, "FileReference": FileReference, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "TroopArt": TroopArt, "LogoContent": LogoContent, "LogoExtension": LogoExtension, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "NewDisplayName": NewDisplayName, "CompleteDisplayName": CompleteDisplayName, "PersonChangeName": PersonChangeName, "PropertyAgreementExtension": PropertyAgreementExtension, "PropertyAgreementContent": PropertyAgreementContent, "TroopArtKey": TroopArtKey, "ID_JournalNovice": ID_JournalNovice, "ID_JournalDeliveryType": ID_JournalDeliveryType, "FullDisplayName": FullDisplayName, "DecisionSeatChangeExtension": DecisionSeatChangeExtension, "ShopDiscountBarcode": ShopDiscountBarcode, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Smazat registrační vadu jednotky
    def UnitMistakeReportDelete(self, ID_Login, ID):
        return self._client.service.UnitMistakeReportDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit registrační vadu jednotky
    def UnitMistakeReportInsert(self, ID_Login, ID, ID_Unit, ID_Mistake, Unit=None, RegistrationNumber=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.UnitMistakeReportInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Mistake": ID_Mistake, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Načíst seznam registrací jednotky
    def UnitRegistrationAll(self, ID_Login, ID_Unit, Year):
        return self._client.service.UnitRegistrationAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "Year": Year})

    # Provede kontrolu zadané registrace jednotky a vrátí nalezené vady
    def UnitRegistrationCheck(self, ID_Login, ID):
        return self._client.service.UnitRegistrationCheck({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail registrace jednotky
    def UnitRegistrationDetail(self, ID_Login, ID, ID_Unit, Year, Instructions=None):
        return self._client.service.UnitRegistrationDetail({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "Instructions": Instructions})

    # Založit registraci jednotky
    def UnitRegistrationInsert(self, ID_Login, ID, ID_Unit, Year, DateChecked, DateConfirmed, IsDelivered, IsAccepted, ShowServices, ID_UnitRegistrationParent, ParentIsDelivered, ParentIsAccepted, ParentHasCreated, ParentShowServices, DisplayName=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Instructions=None, UnitRegistrationParent=None, InstructionsParent=None):
        return self._client.service.UnitRegistrationInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "DateChecked": DateChecked, "DateConfirmed": DateConfirmed, "IsDelivered": IsDelivered, "IsAccepted": IsAccepted, "ShowServices": ShowServices, "ID_UnitRegistrationParent": ID_UnitRegistrationParent, "ParentIsDelivered": ParentIsDelivered, "ParentIsAccepted": ParentIsAccepted, "ParentHasCreated": ParentHasCreated, "ParentShowServices": ParentShowServices, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Instructions": Instructions, "UnitRegistrationParent": UnitRegistrationParent, "InstructionsParent": InstructionsParent})

    # Upravit registraci jednotky
    def UnitRegistrationUpdate(self, ID_Login, ID, ID_Unit, Year, DateChecked, DateConfirmed, IsDelivered, IsAccepted, ShowServices, ID_UnitRegistrationParent, ParentIsDelivered, ParentIsAccepted, ParentHasCreated, ParentShowServices, DisplayName=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Instructions=None, UnitRegistrationParent=None, InstructionsParent=None):
        return self._client.service.UnitRegistrationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "DateChecked": DateChecked, "DateConfirmed": DateConfirmed, "IsDelivered": IsDelivered, "IsAccepted": IsAccepted, "ShowServices": ShowServices, "ID_UnitRegistrationParent": ID_UnitRegistrationParent, "ParentIsDelivered": ParentIsDelivered, "ParentIsAccepted": ParentIsAccepted, "ParentHasCreated": ParentHasCreated, "ParentShowServices": ParentShowServices, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Instructions": Instructions, "UnitRegistrationParent": UnitRegistrationParent, "InstructionsParent": InstructionsParent})

    # Načíst seznam podřízených jednotek
    def UnitTreeAll(self, ID_Login, ID_Application, ID_UnitParent, ShowHistory, IsValid):
        return self._client.service.UnitTreeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_UnitParent": ID_UnitParent, "ShowHistory": ShowHistory, "IsValid": IsValid})

    # Načíst detail existence jednotky
    def UnitTreeDetail(self, ID_Login, ID):
        return self._client.service.UnitTreeDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam důvodů ukončení existence
    def UnitTreeReasonAll(self, ID_Login, DisplayName=None):
        return self._client.service.UnitTreeReasonAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Ukončit existenci jednotky
    def UnitTreeUpdate(self, ID_Login, ID, ValidFrom, ValidTo, ID_Unit, ID_UnitParent, ID_UnitMerge, ID_UnitTreeReason=None, Unit=None, UnitParent=None, RegistrationNumber=None, ID_UnitType=None, UnitMerge=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitTreeUpdate({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Unit": ID_Unit, "ID_UnitParent": ID_UnitParent, "ID_UnitMerge": ID_UnitMerge, "ID_UnitTreeReason": ID_UnitTreeReason, "Unit": Unit, "UnitParent": UnitParent, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "UnitMerge": UnitMerge, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Načíst seznam typů jednotek
    def UnitTypeAll(self, ID_Login, DisplayName=None, ID_UnitTypeCreate=None, ID_UnitTypeParent=None):
        return self._client.service.UnitTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_UnitTypeCreate": ID_UnitTypeCreate, "ID_UnitTypeParent": ID_UnitTypeParent})

    # Upravit jednotku
    def UnitUpdate(self, ID_Login, ID, ID_Group, ID_Unit, ContainsMembers, CommissionDeadline, IsVatPayer, ID_TroopArt, CanUpdateRegistrationNumber, ID_DocumentLogo, IsUnitCancel, JournalParent, ChangeFreeJournal, ID_UnitParent, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, ID_PersonChangeName, DateChangeName, IsPropertyOwner, ID_TempFilePropertyAgreement, ID_DocumentDecision, ID_DocumentPropertyAgreement, ID_TempFileSeatChange, ID_TempFileUnitLogo, ID_UnitType=None, UnitType=None, DisplayName=None, SortName=None, RegistrationNumber=None, ShortRegistrationNumber=None, Location=None, LocationNew=None, IC=None, DIC=None, FileReference=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, TroopArt=None, LogoContent=None, LogoExtension=None, AddressDistrict=None, PostalDistrict=None, NewDisplayName=None, CompleteDisplayName=None, PersonChangeName=None, PropertyAgreementExtension=None, PropertyAgreementContent=None, TroopArtKey=None, ID_JournalNovice=None, ID_JournalDeliveryType=None, FullDisplayName=None, DecisionSeatChangeExtension=None, ShopDiscountBarcode=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_Unit": ID_Unit, "ContainsMembers": ContainsMembers, "CommissionDeadline": CommissionDeadline, "IsVatPayer": IsVatPayer, "ID_TroopArt": ID_TroopArt, "CanUpdateRegistrationNumber": CanUpdateRegistrationNumber, "ID_DocumentLogo": ID_DocumentLogo, "IsUnitCancel": IsUnitCancel, "JournalParent": JournalParent, "ChangeFreeJournal": ChangeFreeJournal, "ID_UnitParent": ID_UnitParent, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_PersonChangeName": ID_PersonChangeName, "DateChangeName": DateChangeName, "IsPropertyOwner": IsPropertyOwner, "ID_TempFilePropertyAgreement": ID_TempFilePropertyAgreement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "ID_TempFileSeatChange": ID_TempFileSeatChange, "ID_TempFileUnitLogo": ID_TempFileUnitLogo, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "DisplayName": DisplayName, "SortName": SortName, "RegistrationNumber": RegistrationNumber, "ShortRegistrationNumber": ShortRegistrationNumber, "Location": Location, "LocationNew": LocationNew, "IC": IC, "DIC": DIC, "FileReference": FileReference, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "TroopArt": TroopArt, "LogoContent": LogoContent, "LogoExtension": LogoExtension, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "NewDisplayName": NewDisplayName, "CompleteDisplayName": CompleteDisplayName, "PersonChangeName": PersonChangeName, "PropertyAgreementExtension": PropertyAgreementExtension, "PropertyAgreementContent": PropertyAgreementContent, "TroopArtKey": TroopArtKey, "ID_JournalNovice": ID_JournalNovice, "ID_JournalDeliveryType": ID_JournalDeliveryType, "FullDisplayName": FullDisplayName, "DecisionSeatChangeExtension": DecisionSeatChangeExtension, "ShopDiscountBarcode": ShopDiscountBarcode, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Přiřadit osobě uživatelský účet
    def PersonUpdateUser(self, ID_Login, ID, Overwrite, UserName=None, SecurityCode=None):
        return self._client.service.PersonUpdateUser({"ID_Login": ID_Login, "ID": ID, "Overwrite": Overwrite, "UserName": UserName, "SecurityCode": SecurityCode})

    # Načtení informací o osobě
    def PersonDetail(self, ID_Login, ID):
        return self._client.service.PersonDetail({"ID_Login": ID_Login, "ID": ID})

    # Načtení informací o jednotce
    def UnitDetail(self, ID_Login, ID_Application, ID, FindStredisko, FindUstredi):
        return self._client.service.UnitDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "FindStredisko": FindStredisko, "FindUstredi": FindUstredi})

    # Načíst detail banky
    def BankDetail(self, ID_Login, ID):
        return self._client.service.BankDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam typů kontaktů
    def ContactTypeAll(self, ID_Login, IsForPerson, IsForUnit, ID=None, DisplayName=None):
        return self._client.service.ContactTypeAll({"ID_Login": ID_Login, "IsForPerson": IsForPerson, "IsForUnit": IsForUnit, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam vzdělávacích akcí
    def EducatationSeminaryAll(self, ID_Login, ID_Person, DisplayName=None):
        return self._client.service.EducatationSeminaryAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "DisplayName": DisplayName})

    # Smazat vzdělávací akci
    def EducatationSeminaryDelete(self, ID_Login, ID):
        return self._client.service.EducatationSeminaryDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit vzdělávací akci
    def EducatationSeminaryInsert(self, ID_Login, ID_Person, ID, YearFrom, ID_EventEducationType, DisplayName=None, Note=None, ParticipationType=None):
        return self._client.service.EducatationSeminaryInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "YearFrom": YearFrom, "ID_EventEducationType": ID_EventEducationType, "DisplayName": DisplayName, "Note": Note, "ParticipationType": ParticipationType})

    # Upravit vzdělávací akci
    def EducatationSeminaryUpdate(self, ID_Login, ID_Person, ID, YearFrom, ID_EventEducationType, DisplayName=None, Note=None, ParticipationType=None):
        return self._client.service.EducatationSeminaryUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "YearFrom": YearFrom, "ID_EventEducationType": ID_EventEducationType, "DisplayName": DisplayName, "Note": Note, "ParticipationType": ParticipationType})

    # Načíst seznam osob členem kandidátní komise
    def PersonAllEventCongressFunction(self, ID_Login, ID, ID_EventCongressFunction, DisplayName=None):
        return self._client.service.PersonAllEventCongressFunction({"ID_Login": ID_Login, "ID": ID, "ID_EventCongressFunction": ID_EventCongressFunction, "DisplayName": DisplayName})

    # Načíst detail dalších údajů osoby
    def PersonOtherDetail(self, ID_Login, ID):
        return self._client.service.PersonOtherDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit další údaje osoby
    def PersonOtherUpdate(self, ID_Login, ID, ID_Person, ID_DistrictBirth, ID_Assurance, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, DateChangeSocialNetwork, DateChangeMarketing, DateChangeDataStorage, DateChangeAudiovisual, IsRPS, IsEPS, IsEduParticipantExt, OnlyValidate, ID_EventCongress, ID_TempFileHealth, ID_DocumentHealth, IdCardValidTo, IsAdult, IsNonMemberWithGoogleServicesAccess, PromiseChild, PromiseScout, PromiseOfficial, BirthCity=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, Person=None, MaidenName=None, DistrictBirth=None, Assurance=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Note=None, ParentNote=None, IdCardNumber=None, TrailProgress=None):
        return self._client.service.PersonOtherUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_DistrictBirth": ID_DistrictBirth, "ID_Assurance": ID_Assurance, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "DateChangeSocialNetwork": DateChangeSocialNetwork, "DateChangeMarketing": DateChangeMarketing, "DateChangeDataStorage": DateChangeDataStorage, "DateChangeAudiovisual": DateChangeAudiovisual, "IsRPS": IsRPS, "IsEPS": IsEPS, "IsEduParticipantExt": IsEduParticipantExt, "OnlyValidate": OnlyValidate, "ID_EventCongress": ID_EventCongress, "ID_TempFileHealth": ID_TempFileHealth, "ID_DocumentHealth": ID_DocumentHealth, "IdCardValidTo": IdCardValidTo, "IsAdult": IsAdult, "IsNonMemberWithGoogleServicesAccess": IsNonMemberWithGoogleServicesAccess, "PromiseChild": PromiseChild, "PromiseScout": PromiseScout, "PromiseOfficial": PromiseOfficial, "BirthCity": BirthCity, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "Person": Person, "MaidenName": MaidenName, "DistrictBirth": DistrictBirth, "Assurance": Assurance, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Note": Note, "ParentNote": ParentNote, "IdCardNumber": IdCardNumber, "TrailProgress": TrailProgress})

    # Načte fotografii osoby
    def PersonPhoto(self, ID_Login, ID, Size=None):
        return self._client.service.PersonPhoto({"ID_Login": ID_Login, "ID": ID, "Size": Size})

    # Načíst obsazení funkcí v jednotce pro zobrazení v registru OJ
    def FunctionAllRegistry(self, ID_Login, ID_Application, ID_Unit, ReturnStatutory, ReturnAssistant, ReturnContact):
        return self._client.service.FunctionAllRegistry({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ReturnStatutory": ReturnStatutory, "ReturnAssistant": ReturnAssistant, "ReturnContact": ReturnContact})

    # Načíst seznam termínů schůzek
    def MeetingDateAll(self, ID_Login, ID_Application, ID_Unit, ID_Occupation, ID_WeekDay=None):
        return self._client.service.MeetingDateAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ID_Occupation": ID_Occupation, "ID_WeekDay": ID_WeekDay})

    # Smazat termín schůzek
    def MeetingDateDelete(self, ID_Login, ID):
        return self._client.service.MeetingDateDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail termínu schůzek
    def MeetingDateDetail(self, ID_Login, ID):
        return self._client.service.MeetingDateDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit termín schůzek
    def MeetingDateInsert(self, ID_Login, ID, ID_Unit, ID_Occupation, DisplayName=None, Unit=None, ID_WeekDay=None, WeekDay=None, TimeFrom=None, TimeTo=None, Periodicity=None, Occupation=None):
        return self._client.service.MeetingDateInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Occupation": ID_Occupation, "DisplayName": DisplayName, "Unit": Unit, "ID_WeekDay": ID_WeekDay, "WeekDay": WeekDay, "TimeFrom": TimeFrom, "TimeTo": TimeTo, "Periodicity": Periodicity, "Occupation": Occupation})

    # Upravit termín schůzek
    def MeetingDateUpdate(self, ID_Login, ID, ID_Unit, ID_Occupation, DisplayName=None, Unit=None, ID_WeekDay=None, WeekDay=None, TimeFrom=None, TimeTo=None, Periodicity=None, Occupation=None):
        return self._client.service.MeetingDateUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Occupation": ID_Occupation, "DisplayName": DisplayName, "Unit": Unit, "ID_WeekDay": ID_WeekDay, "WeekDay": WeekDay, "TimeFrom": TimeFrom, "TimeTo": TimeTo, "Periodicity": Periodicity, "Occupation": Occupation})

    # Hledání v registru OJ
    def UnitAllRegistry(self, ID_Login, ID_Application, IsValid, DisplayName=None, IC=None, RegistrationNumber=None, Location=None, ParentDisplayName=None, ParentRegistrationNumber=None):
        return self._client.service.UnitAllRegistry({"ID_Login": ID_Login, "ID_Application": ID_Application, "IsValid": IsValid, "DisplayName": DisplayName, "IC": IC, "RegistrationNumber": RegistrationNumber, "Location": Location, "ParentDisplayName": ParentDisplayName, "ParentRegistrationNumber": ParentRegistrationNumber})

    # Načíst seznam zrušení jednotky
    def UnitCancelAll(self, ID_Login, ID_Application, ID_Unit, ID_Person, IsValid, ID_UnitCancelType=None):
        return self._client.service.UnitCancelAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "IsValid": IsValid, "ID_UnitCancelType": ID_UnitCancelType})

    # Založit zrušení jednotky
    def UnitCancelInsert(self, ID_Login, ID, ID_Unit, DateDecision, ID_Person, ValidTo, Unit=None, ID_UnitCancelType=None, UnitCancelType=None, Description=None, Person=None):
        return self._client.service.UnitCancelInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "DateDecision": DateDecision, "ID_Person": ID_Person, "ValidTo": ValidTo, "Unit": Unit, "ID_UnitCancelType": ID_UnitCancelType, "UnitCancelType": UnitCancelType, "Description": Description, "Person": Person})

    # Načíst seznam typů rozhodnutí
    def UnitCancelTypeAll(self, ID_Login, ID_Unit, DisplayName=None):
        return self._client.service.UnitCancelTypeAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "DisplayName": DisplayName})

    # Přehled počtu členů podle poslední uzavřené registrace
    def UnitDetailMembersRegistry(self, ID_Login, ID_Application, ID):
        return self._client.service.UnitDetailMembersRegistry({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Zobrazit detail jednotky v registru OJ
    def UnitDetailRegistry(self, ID_Login, ID_Application, ID):
        return self._client.service.UnitDetailRegistry({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načte logo jednotky
    def UnitLogo(self, ID_Login, ID_Application, ID):
        return self._client.service.UnitLogo({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Statistika členů a jednotek v registraci
    def UnitRegistrationMembers(self, ID_Login, ID):
        return self._client.service.UnitRegistrationMembers({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam hospodářských výkazů
    def StatementErrors(self, ID_Login, ID):
        return self._client.service.StatementErrors({"ID_Login": ID_Login, "ID": ID})

    # Spočítat, zda hospodářský výkaz obsahuje chyby
    def StatementComputeIsError(self, ID_Login, ID, ID_Unit, Year, IsError, IsDelivered, DateDelivered, DateCreated, IsThousands, IsConsultant, ID_Document, ID_DocumentTempFile, DateSent, ID_PersonSent, DateConfirmed, ID_PersonConfirmed, ID_Registry, ShowOverview, Unit=None, RegistrationNumber=None, ID_StatementType=None, StatementType=None, ID_StatementState=None, StatementState=None, PersonSent=None, PersonConfirmed=None):
        return self._client.service.StatementComputeIsError({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "IsError": IsError, "IsDelivered": IsDelivered, "DateDelivered": DateDelivered, "DateCreated": DateCreated, "IsThousands": IsThousands, "IsConsultant": IsConsultant, "ID_Document": ID_Document, "ID_DocumentTempFile": ID_DocumentTempFile, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "DateConfirmed": DateConfirmed, "ID_PersonConfirmed": ID_PersonConfirmed, "ID_Registry": ID_Registry, "ShowOverview": ShowOverview, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StatementType": ID_StatementType, "StatementType": StatementType, "ID_StatementState": ID_StatementState, "StatementState": StatementState, "PersonSent": PersonSent, "PersonConfirmed": PersonConfirmed})

    # Načíst seznam hospodářských výkazů podřízených jednotek
    def StatementAllChild(self, ID_Login, ID):
        return self._client.service.StatementAllChild({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam položek hospodářského výkazu včetně součtů oblastí
    def StatementEntryAllTotals(self, ID_Login, ID_Statement, ID_StatementEntryType, IsMoney):
        return self._client.service.StatementEntryAllTotals({"ID_Login": ID_Login, "ID_Statement": ID_Statement, "ID_StatementEntryType": ID_StatementEntryType, "IsMoney": IsMoney})

    # Obnovit existenci jednotky
    def UnitTreeRenew(self, ID_Login, ID, ValidFrom, ValidTo, ID_Unit, ID_UnitParent, ID_UnitMerge, ID_UnitTreeReason=None, Unit=None, UnitParent=None, RegistrationNumber=None, ID_UnitType=None, UnitMerge=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitTreeRenew({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Unit": ID_Unit, "ID_UnitParent": ID_UnitParent, "ID_UnitMerge": ID_UnitMerge, "ID_UnitTreeReason": ID_UnitTreeReason, "Unit": Unit, "UnitParent": UnitParent, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "UnitMerge": UnitMerge, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Načíst detail vady registrace
    def MistakeDetail(self, ID_Login, ID):
        return self._client.service.MistakeDetail({"ID_Login": ID_Login, "ID": ID})

    # Ověření, zda lze osobu převést do zadané jednotky
    def PersonDetailIdentificationCode(self, ID_Login, ID_Unit, IdentificationCode=None):
        return self._client.service.PersonDetailIdentificationCode({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IdentificationCode": IdentificationCode})

    # Načíst seznam jednotek ve stejném středisku a nebo všech podřízených
    def UnitAllUnit(self, ID_Login, ID_Unit, SearchStredisko):
        return self._client.service.UnitAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "SearchStredisko": SearchStredisko})

    # Obnovit členství osoby v jednotce
    def MembershipRenew(self, ID_Login, ID, ID_Unit, ID_Person, ID_User, ValidFrom, ValidTo, IsUnique, CreateNew, OnlyValidate, IsFunction, IsUnitFunction, IsSts, IsDelegate, PersonDateBirth, Person=None, ID_MembershipType=None, ID_MembershipCategory=None, ID_MembershipReason=None):
        return self._client.service.MembershipRenew({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ID_User": ID_User, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "IsUnique": IsUnique, "CreateNew": CreateNew, "OnlyValidate": OnlyValidate, "IsFunction": IsFunction, "IsUnitFunction": IsUnitFunction, "IsSts": IsSts, "IsDelegate": IsDelegate, "PersonDateBirth": PersonDateBirth, "Person": Person, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "ID_MembershipReason": ID_MembershipReason})

    # Hledání osob (helpdesk)
    def PersonAllHelpdesk(self, ID_Login, IsValid, FirstName=None, LastName=None, NickName=None, IdentificationCode=None, City=None, UserName=None, Email=None, Phone=None):
        return self._client.service.PersonAllHelpdesk({"ID_Login": ID_Login, "IsValid": IsValid, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "IdentificationCode": IdentificationCode, "City": City, "UserName": UserName, "Email": Email, "Phone": Phone})

    # Načíst seznam žádostí o převod
    def RequestAll(self, ID_Login, ID_Person, ID_UserCreate, ID_Unit, ID_UserDecision, ID_MembershipType=None, ID_MembershipCategory=None, ID_RequestState=None):
        return self._client.service.RequestAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_UserCreate": ID_UserCreate, "ID_Unit": ID_Unit, "ID_UserDecision": ID_UserDecision, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "ID_RequestState": ID_RequestState})

    # Načíst detail žádosti o převod
    def RequestDetail(self, ID_Login, ID):
        return self._client.service.RequestDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit žádost o převod
    def RequestInsert(self, ID_Login, ID, ID_Person, Birthday, ValidFrom, ID_UserCreate, ID_PersonCreate, DateCreate, ID_Unit, ID_UserDecision, ID_PersonDecision, DateDecision, NewMembership, IdentificationCode=None, Person=None, ID_Sex=None, Sex=None, Reason=None, ID_MembershipType=None, MembershipType=None, ID_MembershipCategory=None, MembershipCategory=None, PersonCreate=None, Unit=None, RegistrationNumber=None, ID_RequestState=None, RequestState=None, PersonDecision=None, Decision=None):
        return self._client.service.RequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "ValidFrom": ValidFrom, "ID_UserCreate": ID_UserCreate, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "ID_UserDecision": ID_UserDecision, "ID_PersonDecision": ID_PersonDecision, "DateDecision": DateDecision, "NewMembership": NewMembership, "IdentificationCode": IdentificationCode, "Person": Person, "ID_Sex": ID_Sex, "Sex": Sex, "Reason": Reason, "ID_MembershipType": ID_MembershipType, "MembershipType": MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "MembershipCategory": MembershipCategory, "PersonCreate": PersonCreate, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_RequestState": ID_RequestState, "RequestState": RequestState, "PersonDecision": PersonDecision, "Decision": Decision})

    # Načíst seznam stavů žadosti o převod
    def RequestStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.RequestStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit žádost o převod
    def RequestUpdate(self, ID_Login, ID, ID_Person, Birthday, ValidFrom, ID_UserCreate, ID_PersonCreate, DateCreate, ID_Unit, ID_UserDecision, ID_PersonDecision, DateDecision, NewMembership, IdentificationCode=None, Person=None, ID_Sex=None, Sex=None, Reason=None, ID_MembershipType=None, MembershipType=None, ID_MembershipCategory=None, MembershipCategory=None, PersonCreate=None, Unit=None, RegistrationNumber=None, ID_RequestState=None, RequestState=None, PersonDecision=None, Decision=None):
        return self._client.service.RequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "ValidFrom": ValidFrom, "ID_UserCreate": ID_UserCreate, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "ID_UserDecision": ID_UserDecision, "ID_PersonDecision": ID_PersonDecision, "DateDecision": DateDecision, "NewMembership": NewMembership, "IdentificationCode": IdentificationCode, "Person": Person, "ID_Sex": ID_Sex, "Sex": Sex, "Reason": Reason, "ID_MembershipType": ID_MembershipType, "MembershipType": MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "MembershipCategory": MembershipCategory, "PersonCreate": PersonCreate, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_RequestState": ID_RequestState, "RequestState": RequestState, "PersonDecision": PersonDecision, "Decision": Decision})

    # Přehled registračních komentářů
    def UnitRegistrationReport(self, ID_Login, ID):
        return self._client.service.UnitRegistrationReport({"ID_Login": ID_Login, "ID": ID})

    # Detailní informace o osobách v jednotce (pro export do CSV)
    def PersonAllExport(self, ID_Login, ID_Unit):
        return self._client.service.PersonAllExport({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načíst seznam registrací podřízených jednotek
    def UnitRegistrationAllChild(self, ID_Login, ID_UnitRegistration):
        return self._client.service.UnitRegistrationAllChild({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration})

    # Upravit historickou funkci
    def FunctionUpdateHistory(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionUpdateHistory({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Založit historickou funkci
    def FunctionInsertHistory(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionInsertHistory({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Smazat historickou funkci
    def FunctionDeleteHistory(self, ID_Login, ID):
        return self._client.service.FunctionDeleteHistory({"ID_Login": ID_Login, "ID": ID})

    # Smazat historickou kvalifikaci
    def QualificationDeleteHistory(self, ID_Login, ID):
        return self._client.service.QualificationDeleteHistory({"ID_Login": ID_Login, "ID": ID})

    # Založit historickou kvalifikaci
    def QualificationInsertHistory(self, ID_Login, ID_Person, ID, ValidFrom, ValidTo, ID_QualificationType, IsUsed, SendMessage, ID_Document, Person=None, QualificationType=None, LetterNumber=None, Note=None):
        return self._client.service.QualificationInsertHistory({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_QualificationType": ID_QualificationType, "IsUsed": IsUsed, "SendMessage": SendMessage, "ID_Document": ID_Document, "Person": Person, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "Note": Note})

    # Upravit historickou kvalifikaci
    def QualificationUpdateHistory(self, ID_Login, ID_Person, ID, ValidFrom, ValidTo, ID_QualificationType, IsUsed, SendMessage, ID_Document, Person=None, QualificationType=None, LetterNumber=None, Note=None):
        return self._client.service.QualificationUpdateHistory({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_QualificationType": ID_QualificationType, "IsUsed": IsUsed, "SendMessage": SendMessage, "ID_Document": ID_Document, "Person": Person, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "Note": Note})

    # Přehled odvodů pro nadřízené jednotky
    def UnitRegistrationSummary(self, ID_Login, ID):
        return self._client.service.UnitRegistrationSummary({"ID_Login": ID_Login, "ID": ID})

    # Hledání osob
    def PersonAllLogin(self, ID_Login, Birthday, FirstName=None, LastName=None, NickName=None, IdentificationCode=None, IdentificationCodeStartsWith=None, ID_MembershipType=None, ID_MembershipCategory=None, Phone=None, Email=None, City=None, RegistrationNumber=None):
        return self._client.service.PersonAllLogin({"ID_Login": ID_Login, "Birthday": Birthday, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "IdentificationCode": IdentificationCode, "IdentificationCodeStartsWith": IdentificationCodeStartsWith, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "Phone": Phone, "Email": Email, "City": City, "RegistrationNumber": RegistrationNumber})

    # Načtení informací o osobě podle bezpečnostního kódu a uživatelského jména
    def PersonDetailSecurityCode(self, ID_Login, UserName=None, SecurityCode=None):
        return self._client.service.PersonDetailSecurityCode({"ID_Login": ID_Login, "UserName": UserName, "SecurityCode": SecurityCode})

    # Ověření platnosti rodného čísla
    def PersonParseIdentificationCode(self, ID_Login, IdentificationCode=None):
        return self._client.service.PersonParseIdentificationCode({"ID_Login": ID_Login, "IdentificationCode": IdentificationCode})

    # Načíst seznam registrací osoby
    def PersonRegistrationAllPerson(self, ID_Login, ID_Person, Year, IsLastRegistration, Unit=None):
        return self._client.service.PersonRegistrationAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person, "Year": Year, "IsLastRegistration": IsLastRegistration, "Unit": Unit})

    # Načíst seznam funkcí osoby
    def FunctionAllPerson(self, ID_Login, ID_Person, ID_Unit, ID_FunctionType, ShowHistory, IsOficial, IsValid, ID_FunctionReason=None):
        return self._client.service.FunctionAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ShowHistory": ShowHistory, "IsOficial": IsOficial, "IsValid": IsValid, "ID_FunctionReason": ID_FunctionReason})

    # Načíst seznam členství osob v jednotce
    def MembershipAllPerson(self, ID_Login, ID_Person, ID_Unit, ShowHistory, IsValid, ID_MembershipType=None, ID_MembershipCategory=None):
        return self._client.service.MembershipAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ShowHistory": ShowHistory, "IsValid": IsValid, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory})

    # Vrátí seznam uživatelů, kteří nejsou zaregistrovaní v registraci jednotky odpovídající zadané kategorii
    def PersonAllRegistrationCategory(self, ID_Login, ID_RegistrationCategory, ID, IncludeChild):
        return self._client.service.PersonAllRegistrationCategory({"ID_Login": ID_Login, "ID_RegistrationCategory": ID_RegistrationCategory, "ID": ID, "IncludeChild": IncludeChild})

    # Smazat registrační vadu osoby
    def PersonMistakeReportDelete(self, ID_Login, ID):
        return self._client.service.PersonMistakeReportDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit registrační vadu osoby
    def PersonMistakeReportInsert(self, ID_Login, ID, ID_Person, ID_Unit, ID_UnitRegistration, ID_Mistake, Person=None, UnitRegistrationNumber=None, Unit=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.PersonMistakeReportInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_UnitRegistration": ID_UnitRegistration, "ID_Mistake": ID_Mistake, "Person": Person, "UnitRegistrationNumber": UnitRegistrationNumber, "Unit": Unit, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Načíst seznam registrací osob v jednotce
    def PersonRegistrationAll(self, ID_Login, ID_UnitRegistration, IncludeChild):
        return self._client.service.PersonRegistrationAll({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration, "IncludeChild": IncludeChild})

    # Smazat registraci osoby
    def PersonRegistrationDelete(self, ID_Login, ID, ID_UnitRegistration, ID_Items=None):
        return self._client.service.PersonRegistrationDelete({"ID_Login": ID_Login, "ID": ID, "ID_UnitRegistration": ID_UnitRegistration, "ID_Items": ID_Items})

    # Založit registraci osoby
    def PersonRegistrationInsert(self, ID_Login, ID_Membership, ID_RegistrationCategory, RegisterWithMemberCard, ID_RegistrationServiceArray=None):
        return self._client.service.PersonRegistrationInsert({"ID_Login": ID_Login, "ID_Membership": ID_Membership, "ID_RegistrationCategory": ID_RegistrationCategory, "RegisterWithMemberCard": RegisterWithMemberCard, "ID_RegistrationServiceArray": ID_RegistrationServiceArray})

    # Založit registraci jednotky
    def RegistrationCategoryCopyFromParentUnit(self, ID_Login, ID_UnitRegistrationCopy):
        return self._client.service.RegistrationCategoryCopyFromParentUnit({"ID_Login": ID_Login, "ID_UnitRegistrationCopy": ID_UnitRegistrationCopy})

    # Načíst seznam titulů osoby
    def DegreeAll(self, ID_Login, ID_Person, ID_DegreeType):
        return self._client.service.DegreeAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_DegreeType": ID_DegreeType})

    # Smazat titul osoby
    def DegreeDelete(self, ID_Login, ID):
        return self._client.service.DegreeDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit titul osoby
    def DegreeInsert(self, ID_Login, ID_Person, ID, ID_DegreeType):
        return self._client.service.DegreeInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_DegreeType": ID_DegreeType})

    # Načíst seznam titulů
    def DegreeTypeAll(self, ID_Login, ID_Application, ID, DisplayName=None):
        return self._client.service.DegreeTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Upravit titul osoby
    def DegreeUpdate(self, ID_Login, ID_Person, ID, ID_DegreeType):
        return self._client.service.DegreeUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_DegreeType": ID_DegreeType})

    # Načíst seznam vzdělání osoby
    def EducationAll(self, ID_Login, ID_Person, ID_EducationType):
        return self._client.service.EducationAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_EducationType": ID_EducationType})

    # Smazat vzdělání osoby
    def EducationDelete(self, ID_Login, ID):
        return self._client.service.EducationDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit vzdělání osoby
    def EducationInsert(self, ID_Login, ID_Person, ID, ID_EducationType, Note=None):
        return self._client.service.EducationInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_EducationType": ID_EducationType, "Note": Note})

    # Načíst seznam typů vzdělání
    def EducationTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.EducationTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit vzdělání osoby
    def EducationUpdate(self, ID_Login, ID_Person, ID, ID_EducationType, Note=None):
        return self._client.service.EducationUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_EducationType": ID_EducationType, "Note": Note})

    # Načíst seznam funkcí v jednotce
    def FunctionAll(self, ID_Login, ID_Person, ID_Unit, ID_FunctionType, IsValid, ShowHistory, IsAgency, ID_Agency, IsStatutory, ID_FunctionReason=None, Person=None):
        return self._client.service.FunctionAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "IsValid": IsValid, "ShowHistory": ShowHistory, "IsAgency": IsAgency, "ID_Agency": ID_Agency, "IsStatutory": IsStatutory, "ID_FunctionReason": ID_FunctionReason, "Person": Person})

    # Načíst detail funkce
    def FunctionDetail(self, ID_Login, ID):
        return self._client.service.FunctionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit funkci
    def FunctionInsert(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionInsert({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Načíst seznam důvodů ukončení funkce
    def FunctionReasonAll(self, ID_Login, DisplayName=None):
        return self._client.service.FunctionReasonAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam typů funkcí
    def FunctionTypeAll(self, ID_Login, ID_Role, IsElective, DisplayName=None, ID_UnitType=None):
        return self._client.service.FunctionTypeAll({"ID_Login": ID_Login, "ID_Role": ID_Role, "IsElective": IsElective, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType})

    # Smazat typ funkce
    def FunctionTypeDelete(self, ID_Login, ID):
        return self._client.service.FunctionTypeDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail typu funkce
    def FunctionTypeDetail(self, ID_Login, ID):
        return self._client.service.FunctionTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit typ funkce
    def FunctionTypeInsert(self, ID_Login, ID, ID_Role, MinCount, MaxCount, IsStatutory, IsAssistant, IsAudit, IsOficial, IsElective, IsNotCongress, IsSpecification, IsAgencyMember, IsAgencyLeader, ID_Agency, Order, DisplayName=None, Code=None, ID_UnitType=None, Note=None, Agency=None):
        return self._client.service.FunctionTypeInsert({"ID_Login": ID_Login, "ID": ID, "ID_Role": ID_Role, "MinCount": MinCount, "MaxCount": MaxCount, "IsStatutory": IsStatutory, "IsAssistant": IsAssistant, "IsAudit": IsAudit, "IsOficial": IsOficial, "IsElective": IsElective, "IsNotCongress": IsNotCongress, "IsSpecification": IsSpecification, "IsAgencyMember": IsAgencyMember, "IsAgencyLeader": IsAgencyLeader, "ID_Agency": ID_Agency, "Order": Order, "DisplayName": DisplayName, "Code": Code, "ID_UnitType": ID_UnitType, "Note": Note, "Agency": Agency})

    # Upravit typ funkce
    def FunctionTypeUpdate(self, ID_Login, ID, ID_Role, MinCount, MaxCount, IsStatutory, IsAssistant, IsAudit, IsOficial, IsElective, IsNotCongress, IsSpecification, IsAgencyMember, IsAgencyLeader, ID_Agency, Order, DisplayName=None, Code=None, ID_UnitType=None, Note=None, Agency=None):
        return self._client.service.FunctionTypeUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Role": ID_Role, "MinCount": MinCount, "MaxCount": MaxCount, "IsStatutory": IsStatutory, "IsAssistant": IsAssistant, "IsAudit": IsAudit, "IsOficial": IsOficial, "IsElective": IsElective, "IsNotCongress": IsNotCongress, "IsSpecification": IsSpecification, "IsAgencyMember": IsAgencyMember, "IsAgencyLeader": IsAgencyLeader, "ID_Agency": ID_Agency, "Order": Order, "DisplayName": DisplayName, "Code": Code, "ID_UnitType": ID_UnitType, "Note": Note, "Agency": Agency})

    # Upravit funkci
    def FunctionUpdate(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionUpdate({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Načíst seznam členství osob v jednotce k aktualizaci
    def MembershipAllUnitUpdate(self, ID_Login, ID_Unit, OnlyDirectMember, LastValidOnly):
        return self._client.service.MembershipAllUnitUpdate({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "OnlyDirectMember": OnlyDirectMember, "LastValidOnly": LastValidOnly})

    # Načíst seznam výchovných kategorií
    def MembershipCategoryAll(self, ID_Login, Age, ID_Unit, AddCombinations, ID=None, DisplayName=None, ID_Sex=None):
        return self._client.service.MembershipCategoryAll({"ID_Login": ID_Login, "Age": Age, "ID_Unit": ID_Unit, "AddCombinations": AddCombinations, "ID": ID, "DisplayName": DisplayName, "ID_Sex": ID_Sex})

    # Načíst detail členství osoby v jednotce
    def MembershipDetail(self, ID_Login, ID):
        return self._client.service.MembershipDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit členství osoby v jednotce
    def MembershipInsert(self, ID_Login, ID, ID_Unit, ID_Person, ID_User, ValidFrom, ValidTo, IsUnique, CreateNew, OnlyValidate, IsFunction, IsUnitFunction, IsSts, IsDelegate, PersonDateBirth, Person=None, ID_MembershipType=None, ID_MembershipCategory=None, ID_MembershipReason=None):
        return self._client.service.MembershipInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ID_User": ID_User, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "IsUnique": IsUnique, "CreateNew": CreateNew, "OnlyValidate": OnlyValidate, "IsFunction": IsFunction, "IsUnitFunction": IsUnitFunction, "IsSts": IsSts, "IsDelegate": IsDelegate, "PersonDateBirth": PersonDateBirth, "Person": Person, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "ID_MembershipReason": ID_MembershipReason})

    # Načíst seznam důvodů změny/ukončení členství
    def MembershipReasonAll(self, ID_Login, IsMulti, ID=None, DisplayName=None):
        return self._client.service.MembershipReasonAll({"ID_Login": ID_Login, "IsMulti": IsMulti, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů členství
    def MembershipTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.MembershipTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit členství osoby v jednotce
    def MembershipUpdate(self, ID_Login, ID, ID_Unit, ID_Person, ID_User, ValidFrom, ValidTo, IsUnique, CreateNew, OnlyValidate, IsFunction, IsUnitFunction, IsSts, IsDelegate, PersonDateBirth, Person=None, ID_MembershipType=None, ID_MembershipCategory=None, ID_MembershipReason=None):
        return self._client.service.MembershipUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ID_User": ID_User, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "IsUnique": IsUnique, "CreateNew": CreateNew, "OnlyValidate": OnlyValidate, "IsFunction": IsFunction, "IsUnitFunction": IsUnitFunction, "IsSts": IsSts, "IsDelegate": IsDelegate, "PersonDateBirth": PersonDateBirth, "Person": Person, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "ID_MembershipReason": ID_MembershipReason})

    # Načíst seznam užívání nemovitosti
    def OccupationAll(self, ID_Login, ID_Application, ID_Unit, IncludeChildUnits, ID_Realty, Publish, ID_RealtyType, Distance, GpsLatitude, GpsLongitude, GpsLatitudeStart, GpsLongitudeStart, GpsLatitudeEnd, GpsLongitudeEnd, AdvertisingCategories=None):
        return self._client.service.OccupationAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "IncludeChildUnits": IncludeChildUnits, "ID_Realty": ID_Realty, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "Distance": Distance, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "GpsLatitudeStart": GpsLatitudeStart, "GpsLongitudeStart": GpsLongitudeStart, "GpsLatitudeEnd": GpsLatitudeEnd, "GpsLongitudeEnd": GpsLongitudeEnd, "AdvertisingCategories": AdvertisingCategories})

    # Smazat užívání nemovitosti
    def OccupationDelete(self, ID_Login, ID):
        return self._client.service.OccupationDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail užívání nemovitosti
    def OccupationDetail(self, ID_Login, ID):
        return self._client.service.OccupationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit užívání nemovitosti
    def OccupationInsert(self, ID_Login, ID, ID_Unit, ID_Realty, Publish, ID_RealtyType, Note=None, RealtyType=None):
        return self._client.service.OccupationInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Realty": ID_Realty, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "Note": Note, "RealtyType": RealtyType})

    # Upravit užívání nemovitosti
    def OccupationUpdate(self, ID_Login, ID, ID_Unit, ID_Realty, Publish, ID_RealtyType, Note=None, RealtyType=None):
        return self._client.service.OccupationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Realty": ID_Realty, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "Note": Note, "RealtyType": RealtyType})

    # Načíst seznam nabídky činnosti
    def OfferAll(self, ID_Login, ID_Person, ID_OfferType, ShowHistory):
        return self._client.service.OfferAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_OfferType": ID_OfferType, "ShowHistory": ShowHistory})

    # Smazat nabídku činnosti
    def OfferDelete(self, ID_Login, ID):
        return self._client.service.OfferDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit nabídku činnosti
    def OfferInsert(self, ID_Login, ID_Person, ID, ID_OfferType, Note=None):
        return self._client.service.OfferInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_OfferType": ID_OfferType, "Note": Note})

    # Načíst seznam činností
    def OfferTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.OfferTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit nabídku činnosti
    def OfferUpdate(self, ID_Login, ID_Person, ID, ID_OfferType, Note=None):
        return self._client.service.OfferUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_OfferType": ID_OfferType, "Note": Note})

    # Načíst seznam osob
    def PersonAll(self, ID_Login, ID, ID_Unit, OnlyDirectMember, ID_FunctionType, ID_QualificationType, DisplayName=None, ID_Sex=None, IdentificationCode=None, FirstName=None, LastName=None, SecurityCode=None, IdentificationCodeStartsWith=None, RegistrationNumber=None):
        return self._client.service.PersonAll({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "OnlyDirectMember": OnlyDirectMember, "ID_FunctionType": ID_FunctionType, "ID_QualificationType": ID_QualificationType, "DisplayName": DisplayName, "ID_Sex": ID_Sex, "IdentificationCode": IdentificationCode, "FirstName": FirstName, "LastName": LastName, "SecurityCode": SecurityCode, "IdentificationCodeStartsWith": IdentificationCodeStartsWith, "RegistrationNumber": RegistrationNumber})

    # Načíst seznam kontaktů osoby
    def PersonContactAll(self, ID_Login, ID_Person, IsCatalog, IsMain, IsHidden, ID_ContactType=None):
        return self._client.service.PersonContactAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "IsCatalog": IsCatalog, "IsMain": IsMain, "IsHidden": IsHidden, "ID_ContactType": ID_ContactType})

    # Smazat kontakt osoby
    def PersonContactDelete(self, ID_Login, ID):
        return self._client.service.PersonContactDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit kontakt osoby
    def PersonContactInsert(self, ID_Login, ID_Person, ID, IsGa, IsCatalog, IsHidden, ID_ContactType=None, Value=None, Note=None):
        return self._client.service.PersonContactInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "IsGa": IsGa, "IsCatalog": IsCatalog, "IsHidden": IsHidden, "ID_ContactType": ID_ContactType, "Value": Value, "Note": Note})

    # Upravit kontakt osoby
    def PersonContactUpdate(self, ID_Login, ID_Person, ID, IsGa, IsCatalog, IsHidden, ID_ContactType=None, Value=None, Note=None):
        return self._client.service.PersonContactUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "IsGa": IsGa, "IsCatalog": IsCatalog, "IsHidden": IsHidden, "ID_ContactType": ID_ContactType, "Value": Value, "Note": Note})

    # Založení osoby
    def PersonInsert(self, ID_Login, Birthday, BirthdayYear, IsForeign, YearFrom, ID_User, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, IdentificationCodeForce, ID_UnitEnrollTempFile, IdentificationCode=None, FirstName=None, LastName=None, NickName=None, Address=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalAddress=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, ID_Sex=None, RegistrationNumber=None, PhotoExtension=None, MaidenName=None, AddressDistrict=None, PostalDistrict=None, UnitEnrollExtension=None, UnitEnroll=None):
        return self._client.service.PersonInsert({"ID_Login": ID_Login, "Birthday": Birthday, "BirthdayYear": BirthdayYear, "IsForeign": IsForeign, "YearFrom": YearFrom, "ID_User": ID_User, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "IdentificationCodeForce": IdentificationCodeForce, "ID_UnitEnrollTempFile": ID_UnitEnrollTempFile, "IdentificationCode": IdentificationCode, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "Address": Address, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalAddress": PostalAddress, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "ID_Sex": ID_Sex, "RegistrationNumber": RegistrationNumber, "PhotoExtension": PhotoExtension, "MaidenName": MaidenName, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "UnitEnrollExtension": UnitEnrollExtension, "UnitEnroll": UnitEnroll})

    # Editace osoby
    def PersonUpdate(self, ID_Login, ID, Birthday, BirthdayYear, IsForeign, YearFrom, ID_User, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, RejectDataStorage, IdentificationCodeForce, GenerateSecurityCode, ID_TempFile, ID_PersonPhotoBig, ID_PersonPhotoMedium, ID_PersonPhotoNormal, ID_PersonPhotoSmall, IdentificationCode=None, FirstName=None, LastName=None, NickName=None, Address=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalAddress=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, ID_Sex=None, RegistrationNumber=None, PhotoExtension=None, PhotoContent=None, MaidenName=None, AddressDistrict=None, PostalDistrict=None, UnitEnrollExtension=None, UnitEnroll=None):
        return self._client.service.PersonUpdate({"ID_Login": ID_Login, "ID": ID, "Birthday": Birthday, "BirthdayYear": BirthdayYear, "IsForeign": IsForeign, "YearFrom": YearFrom, "ID_User": ID_User, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "RejectDataStorage": RejectDataStorage, "IdentificationCodeForce": IdentificationCodeForce, "GenerateSecurityCode": GenerateSecurityCode, "ID_TempFile": ID_TempFile, "ID_PersonPhotoBig": ID_PersonPhotoBig, "ID_PersonPhotoMedium": ID_PersonPhotoMedium, "ID_PersonPhotoNormal": ID_PersonPhotoNormal, "ID_PersonPhotoSmall": ID_PersonPhotoSmall, "IdentificationCode": IdentificationCode, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "Address": Address, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalAddress": PostalAddress, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "ID_Sex": ID_Sex, "RegistrationNumber": RegistrationNumber, "PhotoExtension": PhotoExtension, "PhotoContent": PhotoContent, "MaidenName": MaidenName, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "UnitEnrollExtension": UnitEnrollExtension, "UnitEnroll": UnitEnroll})

    # Načíst seznam kvalifikací
    def QualificationAll(self, ShowHistory, ID_Login, ID_Person, ID_QualificationType, IsValid, QualificationTypeKey=None):
        return self._client.service.QualificationAll({"ShowHistory": ShowHistory, "ID_Login": ID_Login, "ID_Person": ID_Person, "ID_QualificationType": ID_QualificationType, "IsValid": IsValid, "QualificationTypeKey": QualificationTypeKey})

    # Načíst detail kvalifikace
    def QualificationDetail(self, ID_Login, ID):
        return self._client.service.QualificationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit kvalifikaci
    def QualificationInsert(self, ID_Login, ID_Person, ID, ValidFrom, ValidTo, ID_QualificationType, IsUsed, SendMessage, ID_Document, Person=None, QualificationType=None, LetterNumber=None, Note=None):
        return self._client.service.QualificationInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_QualificationType": ID_QualificationType, "IsUsed": IsUsed, "SendMessage": SendMessage, "ID_Document": ID_Document, "Person": Person, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "Note": Note})

    # Načíst seznam typů kvalfikace
    def QualificationTypeAll(self, ID_Login, IsExam, ShowManualIssue, DisplayName=None):
        return self._client.service.QualificationTypeAll({"ID_Login": ID_Login, "IsExam": IsExam, "ShowManualIssue": ShowManualIssue, "DisplayName": DisplayName})

    # Upravit kvalifikaci
    def QualificationUpdate(self, ID_Login, ID_Person, ID, ValidFrom, ValidTo, ID_QualificationType, IsUsed, SendMessage, ID_Document, Person=None, QualificationType=None, LetterNumber=None, Note=None):
        return self._client.service.QualificationUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_QualificationType": ID_QualificationType, "IsUsed": IsUsed, "SendMessage": SendMessage, "ID_Document": ID_Document, "Person": Person, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "Note": Note})

    # Načíst seznam nemovitostí
    def RealtyAll(self, ID_Login, ID, ID_RealtyType, SearchByCity, SearchByName, SearchString=None):
        return self._client.service.RealtyAll({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "SearchByCity": SearchByCity, "SearchByName": SearchByName, "SearchString": SearchString})

    # Načíst detail nemovitosti
    def RealtyDetail(self, ID_Login, ID):
        return self._client.service.RealtyDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit nemovitost
    def RealtyInsert(self, ID_Login, ID, ID_RealtyType, GpsLatitude, GpsLongitude, ID_RealtyCollection, IsPower, ValidTo, IsActive, ID_TempFilePhoto, IsAddressAuthenticated, ID_Document, LVNumber, Acreage, RealtyGpsLatitude, RealtyGpsLongitude, CoordinateX, CoordinateY, DisplayName=None, RealtyType=None, Street=None, City=None, Postcode=None, Description=None, Note=None, RealtyCollection=None, ID_OwnerType=None, OwnerType=None, OwnerTypeNote=None, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, District=None, Storage=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None, Unit=None, UnitRegistrationNumber=None):
        return self._client.service.RealtyInsert({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ValidTo": ValidTo, "IsActive": IsActive, "ID_TempFilePhoto": ID_TempFilePhoto, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_Document": ID_Document, "LVNumber": LVNumber, "Acreage": Acreage, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "CoordinateX": CoordinateX, "CoordinateY": CoordinateY, "DisplayName": DisplayName, "RealtyType": RealtyType, "Street": Street, "City": City, "Postcode": Postcode, "Description": Description, "Note": Note, "RealtyCollection": RealtyCollection, "ID_OwnerType": ID_OwnerType, "OwnerType": OwnerType, "OwnerTypeNote": OwnerTypeNote, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "District": District, "Storage": Storage, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber})

    # Načíst seznam typů nemovitostí
    def RealtyTypeAll(self, ID_Login, ID_Application, DisplayName=None):
        return self._client.service.RealtyTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "DisplayName": DisplayName})

    # Upravit nemovitost
    def RealtyUpdate(self, ID_Login, ID, ID_RealtyType, GpsLatitude, GpsLongitude, ID_RealtyCollection, IsPower, ValidTo, IsActive, ID_TempFilePhoto, IsAddressAuthenticated, ID_Document, LVNumber, Acreage, RealtyGpsLatitude, RealtyGpsLongitude, CoordinateX, CoordinateY, DisplayName=None, RealtyType=None, Street=None, City=None, Postcode=None, Description=None, Note=None, RealtyCollection=None, ID_OwnerType=None, OwnerType=None, OwnerTypeNote=None, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, District=None, Storage=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None, Unit=None, UnitRegistrationNumber=None):
        return self._client.service.RealtyUpdate({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ValidTo": ValidTo, "IsActive": IsActive, "ID_TempFilePhoto": ID_TempFilePhoto, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_Document": ID_Document, "LVNumber": LVNumber, "Acreage": Acreage, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "CoordinateX": CoordinateX, "CoordinateY": CoordinateY, "DisplayName": DisplayName, "RealtyType": RealtyType, "Street": Street, "City": City, "Postcode": Postcode, "Description": Description, "Note": Note, "RealtyCollection": RealtyCollection, "ID_OwnerType": ID_OwnerType, "OwnerType": OwnerType, "OwnerTypeNote": OwnerTypeNote, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "District": District, "Storage": Storage, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber})

    # Načíst seznam registračních kategorií
    def RegistrationCategoryAll(self, ID_Login, ID_UnitRegistration, ID_RegistrationCategoryParent, ShowParentUnit, ShowUsable, IsAfterDeadline, DisplayName=None, ID_MembershipType=None):
        return self._client.service.RegistrationCategoryAll({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration, "ID_RegistrationCategoryParent": ID_RegistrationCategoryParent, "ShowParentUnit": ShowParentUnit, "ShowUsable": ShowUsable, "IsAfterDeadline": IsAfterDeadline, "DisplayName": DisplayName, "ID_MembershipType": ID_MembershipType})

    # Smazat registrační kategorii
    def RegistrationCategoryDelete(self, ID_Login, ID):
        return self._client.service.RegistrationCategoryDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit registrační kategorii
    def RegistrationCategoryInsert(self, ID_Login, ID_UnitRegistration, ID_RegistrationCategoryParent, Amount, IsAfterDeadline, IsJournal, DisplayName=None, ID_MembershipType=None, Note=None):
        return self._client.service.RegistrationCategoryInsert({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration, "ID_RegistrationCategoryParent": ID_RegistrationCategoryParent, "Amount": Amount, "IsAfterDeadline": IsAfterDeadline, "IsJournal": IsJournal, "DisplayName": DisplayName, "ID_MembershipType": ID_MembershipType, "Note": Note})

    # upravit poznámku registru OJ
    def RegistryUpdateNote(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistryUpdateNote({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Načíst seznam typů razítka
    def StampTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.StampTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail hospodářského výkazu pro sestavu
    def StatementDetailReport(self, ID_Login, ID):
        return self._client.service.StatementDetailReport({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam stavů hospodářského výkazu
    def StatementStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.StatementStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit stav hospodářského výkazu
    def StatementUpdateState(self, ID_Login, ID, ID_Unit, Year, IsError, IsDelivered, DateDelivered, DateCreated, IsThousands, IsConsultant, ID_Document, ID_DocumentTempFile, DateSent, ID_PersonSent, DateConfirmed, ID_PersonConfirmed, ID_Registry, ShowOverview, Unit=None, RegistrationNumber=None, ID_StatementType=None, StatementType=None, ID_StatementState=None, StatementState=None, PersonSent=None, PersonConfirmed=None):
        return self._client.service.StatementUpdateState({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "IsError": IsError, "IsDelivered": IsDelivered, "DateDelivered": DateDelivered, "DateCreated": DateCreated, "IsThousands": IsThousands, "IsConsultant": IsConsultant, "ID_Document": ID_Document, "ID_DocumentTempFile": ID_DocumentTempFile, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "DateConfirmed": DateConfirmed, "ID_PersonConfirmed": ID_PersonConfirmed, "ID_Registry": ID_Registry, "ShowOverview": ShowOverview, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StatementType": ID_StatementType, "StatementType": StatementType, "ID_StatementState": ID_StatementState, "StatementState": StatementState, "PersonSent": PersonSent, "PersonConfirmed": PersonConfirmed})

    # Načíst seznam jednotek pro Google synchronizaci
    def UnitAllGoogleGroupSync(self, ID_Login, ID_GoogleGroup):
        return self._client.service.UnitAllGoogleGroupSync({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup})

    # Načíst seznam jednotek v STS
    def UnitAllTelephony(self, ID_Login, ID_Application, ID, ID_Group, RegistrationNumberStartWith, ID_UnitType=None, RegistrationNumber=None, DisplayName=None, Location=None, AccountNumber=None, IC=None):
        return self._client.service.UnitAllTelephony({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_Group": ID_Group, "RegistrationNumberStartWith": RegistrationNumberStartWith, "ID_UnitType": ID_UnitType, "RegistrationNumber": RegistrationNumber, "DisplayName": DisplayName, "Location": Location, "AccountNumber": AccountNumber, "IC": IC})

    # Načíst seznam jednotek pro menu
    def UnitAllMenu(self, ID_Login, ID_Application, ID, ID_UnitParent, ID_UnitChild):
        return self._client.service.UnitAllMenu({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_UnitParent": ID_UnitParent, "ID_UnitChild": ID_UnitChild})

    # Načíst seznam evidencí provedených kontrol
    def UnitAuditRegisterAllUnit(self, ID_Login, ID_Unit):
        return self._client.service.UnitAuditRegisterAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načíst seznam evidencí provedených kontrol
    def UnitAuditRegisterAll(self, ID_Login, ID, ID_Unit):
        return self._client.service.UnitAuditRegisterAll({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit})

    # Načíst detail evidence provedené kontroly
    def UnitAuditRegisterDetail(self, ID_Login, ID):
        return self._client.service.UnitAuditRegisterDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit evidenci provedené kontroly
    def UnitAuditRegisterInsert(self, ID_Login, ID, ID_Unit, Year, ID_DocumentReport, ID_PersonReport, ReportDone, ID_DocumentAudit, ID_PersonAudit, AuditDone, ID_TempFileReport, ID_TempFileAudit, Unit=None, RegistrationNumber=None, PersonReport=None, ReportText=None, PersonAudit=None, AuditText=None):
        return self._client.service.UnitAuditRegisterInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "ID_DocumentReport": ID_DocumentReport, "ID_PersonReport": ID_PersonReport, "ReportDone": ReportDone, "ID_DocumentAudit": ID_DocumentAudit, "ID_PersonAudit": ID_PersonAudit, "AuditDone": AuditDone, "ID_TempFileReport": ID_TempFileReport, "ID_TempFileAudit": ID_TempFileAudit, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonReport": PersonReport, "ReportText": ReportText, "PersonAudit": PersonAudit, "AuditText": AuditText})

    # Zadat soubory
    def UnitAuditRegisterUpdate(self, ID_Login, ID, ID_Unit, Year, ID_DocumentReport, ID_PersonReport, ReportDone, ID_DocumentAudit, ID_PersonAudit, AuditDone, ID_TempFileReport, ID_TempFileAudit, Unit=None, RegistrationNumber=None, PersonReport=None, ReportText=None, PersonAudit=None, AuditText=None):
        return self._client.service.UnitAuditRegisterUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "ID_DocumentReport": ID_DocumentReport, "ID_PersonReport": ID_PersonReport, "ReportDone": ReportDone, "ID_DocumentAudit": ID_DocumentAudit, "ID_PersonAudit": ID_PersonAudit, "AuditDone": AuditDone, "ID_TempFileReport": ID_TempFileReport, "ID_TempFileAudit": ID_TempFileAudit, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonReport": PersonReport, "ReportText": ReportText, "PersonAudit": PersonAudit, "AuditText": AuditText})

    # Načtení informací o slevovém kódu jednotky
    def UnitDetailShopDiscount(self, ID_Login, ID, ID_Person):
        return self._client.service.UnitDetailShopDiscount({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person})

    # Načíst seznam důvodů založení jednotky
    def UnitFoundReasonAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.UnitFoundReasonAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam adres
    def UnitJournalDeliveryAll(self, ID_Login, ID, ID_Unit):
        return self._client.service.UnitJournalDeliveryAll({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit})

    # Načíst detail adresy
    def UnitJournalDeliveryDetail(self, ID_Login, ID, ID_Unit, ID_Person, Unit=None, RegistrationNumber=None, Street=None, Ciry=None, PostCode=None, FirstLine=None, State=None, ID_JournalDeliveryType=None):
        return self._client.service.UnitJournalDeliveryDetail({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Street": Street, "Ciry": Ciry, "PostCode": PostCode, "FirstLine": FirstLine, "State": State, "ID_JournalDeliveryType": ID_JournalDeliveryType})

    # Založit adresu
    def UnitJournalDeliveryInsert(self, ID_Login, ID, ID_Unit, ID_Person, Unit=None, RegistrationNumber=None, Street=None, Ciry=None, PostCode=None, FirstLine=None, State=None, ID_JournalDeliveryType=None):
        return self._client.service.UnitJournalDeliveryInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Street": Street, "Ciry": Ciry, "PostCode": PostCode, "FirstLine": FirstLine, "State": State, "ID_JournalDeliveryType": ID_JournalDeliveryType})

    # Upravit adresu
    def UnitJournalDeliveryUpdate(self, ID_Login, ID, ID_Unit, ID_Person, Unit=None, RegistrationNumber=None, Street=None, Ciry=None, PostCode=None, FirstLine=None, State=None, ID_JournalDeliveryType=None):
        return self._client.service.UnitJournalDeliveryUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Street": Street, "Ciry": Ciry, "PostCode": PostCode, "FirstLine": FirstLine, "State": State, "ID_JournalDeliveryType": ID_JournalDeliveryType})

    # Načíst seznam razítek jednotky
    def UnitStampAll(self, ID_Login, ID_Unit, ID, ID_StampType=None):
        return self._client.service.UnitStampAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_StampType": ID_StampType})

    # Smazat razítko jednotky
    def UnitStampDelete(self, ID_Login, ID):
        return self._client.service.UnitStampDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail razítka jednotky
    def UnitStampDetail(self, ID_Login, ID):
        return self._client.service.UnitStampDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit razítko jednotky
    def UnitStampInsert(self, ID_Login, ID, ID_Unit, Count, Unit=None, RegistrationNumber=None, ID_StampType=None, StampType=None, Email=None, Web=None):
        return self._client.service.UnitStampInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Count": Count, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StampType": ID_StampType, "StampType": StampType, "Email": Email, "Web": Web})

    # Upravit razítko jednotky
    def UnitStampUpdate(self, ID_Login, ID, ID_Unit, Count, Unit=None, RegistrationNumber=None, ID_StampType=None, StampType=None, Email=None, Web=None):
        return self._client.service.UnitStampUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Count": Count, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StampType": ID_StampType, "StampType": StampType, "Email": Email, "Web": Web})

    # Nastavit typ rozesílky balíčků pro nováčky
    def UnitUpdateJournalDeliveryType(self, ID_Login, ID, ID_JournalDeliveryType=None):
        return self._client.service.UnitUpdateJournalDeliveryType({"ID_Login": ID_Login, "ID": ID, "ID_JournalDeliveryType": ID_JournalDeliveryType})

    # Nastavit způsob odběru balíčků pro nováčky
    def UnitUpdateChangeJournalNovice(self, ID_Login, ID, ID_JournalNovice=None):
        return self._client.service.UnitUpdateChangeJournalNovice({"ID_Login": ID_Login, "ID": ID, "ID_JournalNovice": ID_JournalNovice})

    # Upravit jméno jednotky
    def UnitUpdateName(self, ID_Login, ID, ID_Group, ID_Unit, ContainsMembers, CommissionDeadline, IsVatPayer, ID_TroopArt, CanUpdateRegistrationNumber, ID_DocumentLogo, IsUnitCancel, JournalParent, ChangeFreeJournal, ID_UnitParent, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, ID_PersonChangeName, DateChangeName, IsPropertyOwner, ID_TempFilePropertyAgreement, ID_DocumentDecision, ID_DocumentPropertyAgreement, ID_TempFileSeatChange, ID_TempFileUnitLogo, ID_UnitType=None, UnitType=None, DisplayName=None, SortName=None, RegistrationNumber=None, ShortRegistrationNumber=None, Location=None, LocationNew=None, IC=None, DIC=None, FileReference=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, TroopArt=None, LogoContent=None, LogoExtension=None, AddressDistrict=None, PostalDistrict=None, NewDisplayName=None, CompleteDisplayName=None, PersonChangeName=None, PropertyAgreementExtension=None, PropertyAgreementContent=None, TroopArtKey=None, ID_JournalNovice=None, ID_JournalDeliveryType=None, FullDisplayName=None, DecisionSeatChangeExtension=None, ShopDiscountBarcode=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitUpdateName({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_Unit": ID_Unit, "ContainsMembers": ContainsMembers, "CommissionDeadline": CommissionDeadline, "IsVatPayer": IsVatPayer, "ID_TroopArt": ID_TroopArt, "CanUpdateRegistrationNumber": CanUpdateRegistrationNumber, "ID_DocumentLogo": ID_DocumentLogo, "IsUnitCancel": IsUnitCancel, "JournalParent": JournalParent, "ChangeFreeJournal": ChangeFreeJournal, "ID_UnitParent": ID_UnitParent, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_PersonChangeName": ID_PersonChangeName, "DateChangeName": DateChangeName, "IsPropertyOwner": IsPropertyOwner, "ID_TempFilePropertyAgreement": ID_TempFilePropertyAgreement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "ID_TempFileSeatChange": ID_TempFileSeatChange, "ID_TempFileUnitLogo": ID_TempFileUnitLogo, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "DisplayName": DisplayName, "SortName": SortName, "RegistrationNumber": RegistrationNumber, "ShortRegistrationNumber": ShortRegistrationNumber, "Location": Location, "LocationNew": LocationNew, "IC": IC, "DIC": DIC, "FileReference": FileReference, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "TroopArt": TroopArt, "LogoContent": LogoContent, "LogoExtension": LogoExtension, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "NewDisplayName": NewDisplayName, "CompleteDisplayName": CompleteDisplayName, "PersonChangeName": PersonChangeName, "PropertyAgreementExtension": PropertyAgreementExtension, "PropertyAgreementContent": PropertyAgreementContent, "TroopArtKey": TroopArtKey, "ID_JournalNovice": ID_JournalNovice, "ID_JournalDeliveryType": ID_JournalDeliveryType, "FullDisplayName": FullDisplayName, "DecisionSeatChangeExtension": DecisionSeatChangeExtension, "ShopDiscountBarcode": ShopDiscountBarcode, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Ukončit platnost účtu
    def AccountUpdateCancel(self, ID_Login, ID, ID_Unit, ValidTo, ID_Bank, IsMain, DisplayName=None, Unit=None, Bank=None, AccountPrefix=None, AccountNumber=None, Street=None, City=None, Postcode=None, Note=None):
        return self._client.service.AccountUpdateCancel({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ValidTo": ValidTo, "ID_Bank": ID_Bank, "IsMain": IsMain, "DisplayName": DisplayName, "Unit": Unit, "Bank": Bank, "AccountPrefix": AccountPrefix, "AccountNumber": AccountNumber, "Street": Street, "City": City, "Postcode": Postcode, "Note": Note})

    # Načíst seznam věkových kategorií
    def AgeCategoryAll(self, ID_Login, IsMore):
        return self._client.service.AgeCategoryAll({"ID_Login": ID_Login, "IsMore": IsMore})

    # Načíst seznam ústředních orgánů
    def AgencyAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.AgencyAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam členských karet
    def MemberCardAll(self, ID_Login, ID_Person, ID, ID_PersonSchool, ID_MemberCardState=None, DisplayName=None, ID_MemberCardType=None):
        return self._client.service.MemberCardAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_PersonSchool": ID_PersonSchool, "ID_MemberCardState": ID_MemberCardState, "DisplayName": DisplayName, "ID_MemberCardType": ID_MemberCardType})

    # Smazat členskou kartu
    def MemberCardDelete(self, ID_Login, ID):
        return self._client.service.MemberCardDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail členské karty
    def MemberCardDetail(self, ID_Login, ID, DisplayName=None):
        return self._client.service.MemberCardDetail({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit členskou kartu
    def MemberCardInsert(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Upravit členskou kartu
    def MemberCardUpdate(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Objednat ztracenou kartu
    def MemberCardUpdateRerequest(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardUpdateRerequest({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Načíst kartu, na kterou má osoba právo
    def PersonDetailMemberCard(self, ID_Login, ID):
        return self._client.service.PersonDetailMemberCard({"ID_Login": ID_Login, "ID": ID})

    # Načíst aktuální potvrzení o studiu
    def PersonDetailSchool(self, ID_Login, ID):
        return self._client.service.PersonDetailSchool({"ID_Login": ID_Login, "ID": ID})

    # Smazat potvrzení o studiu
    def PersonSchoolDelete(self, ID_Login, ID):
        return self._client.service.PersonSchoolDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit potvrzení o studiu
    def PersonSchoolInsert(self, ID_Login, ID, ID_Person, DateCreate, ID_TempFile, ID_PersonSchoolTempFile, ID_DocumentPhoto, ID_DocumentScan, Person=None, DisplayName=None, City=None, Extension=None, Scan=None, PhotoExtension=None, Photo=None):
        return self._client.service.PersonSchoolInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "DateCreate": DateCreate, "ID_TempFile": ID_TempFile, "ID_PersonSchoolTempFile": ID_PersonSchoolTempFile, "ID_DocumentPhoto": ID_DocumentPhoto, "ID_DocumentScan": ID_DocumentScan, "Person": Person, "DisplayName": DisplayName, "City": City, "Extension": Extension, "Scan": Scan, "PhotoExtension": PhotoExtension, "Photo": Photo})

    # Načíst detail registrační vady osoby
    def PersonMistakeReportDetail(self, ID_Login, ID):
        return self._client.service.PersonMistakeReportDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit registrační vadu osoby
    def PersonMistakeReportUpdate(self, ID_Login, ID, ID_Person, ID_Unit, ID_UnitRegistration, ID_Mistake, Person=None, UnitRegistrationNumber=None, Unit=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.PersonMistakeReportUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_UnitRegistration": ID_UnitRegistration, "ID_Mistake": ID_Mistake, "Person": Person, "UnitRegistrationNumber": UnitRegistrationNumber, "Unit": Unit, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Načíst celkový počet odvodů za doplňkové služby pro nadřízenou jednotku
    def PersonRegistrationServiceAllSummary(self, ID_Login, ID_UnitRegistration):
        return self._client.service.PersonRegistrationServiceAllSummary({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration})

    # Načíst detail registrační vady jednotky
    def UnitMistakeReportDetail(self, ID_Login, ID):
        return self._client.service.UnitMistakeReportDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit registrační vadu jednotky
    def UnitMistakeReportUpdate(self, ID_Login, ID, ID_Unit, ID_Mistake, Unit=None, RegistrationNumber=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.UnitMistakeReportUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Mistake": ID_Mistake, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Načíst věkovou kategorii oddílu
    def UnitAgeCategoryDetail(self, ID_Login, ID_Unit):
        return self._client.service.UnitAgeCategoryDetail({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Nastaví věkovou kategorii oddílu
    def UnitAgeCategoryUpdate(self, ID_Login, ID, ID_AgeCategory):
        return self._client.service.UnitAgeCategoryUpdate({"ID_Login": ID_Login, "ID": ID, "ID_AgeCategory": ID_AgeCategory})

    # Načte seznam handicapů a počty lidí s handicapem pro oddíl
    def UnitHandicapAllUnit(self, ID_Login, ID_Unit):
        return self._client.service.UnitHandicapAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Načte datum poslení editace handicapů jednotky
    def UnitHandicapLastUpdated(self, ID_Login, ID_Unit):
        return self._client.service.UnitHandicapLastUpdated({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Nastaví pro jednotku počet lidí s příslušným handicapem
    def UnitHandicapUpdate(self, ID_Login, ID_Unit, ID_HandicapType, Value):
        return self._client.service.UnitHandicapUpdate({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_HandicapType": ID_HandicapType, "Value": Value})

    # Nastavit zda se provede automatická změna časopisů zdarma
    def UnitUpdateChangeFreeJournal(self, ID_Login, ID, ChangeFreeJournal, IncludeChild=None):
        return self._client.service.UnitUpdateChangeFreeJournal({"ID_Login": ID_Login, "ID": ID, "ChangeFreeJournal": ChangeFreeJournal, "IncludeChild": IncludeChild})

    # Načíst seznam požadavků na změnu v registru OJ
    def RegistryAll(self, ID_Login, ID_Unit, DateCreateFrom, DateCreateTo, DateCreateMonth, DateCreateYear, DisplayName=None, ID_RegistryObject=None, ID_RegistryType=None, ID_RegistryState=None):
        return self._client.service.RegistryAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "DateCreateFrom": DateCreateFrom, "DateCreateTo": DateCreateTo, "DateCreateMonth": DateCreateMonth, "DateCreateYear": DateCreateYear, "DisplayName": DisplayName, "ID_RegistryObject": ID_RegistryObject, "ID_RegistryType": ID_RegistryType, "ID_RegistryState": ID_RegistryState})

    # Načíst seznam požadavků pro odeslání zpráv
    def RegistryAllMessage(self, ID_Login):
        return self._client.service.RegistryAllMessage({"ID_Login": ID_Login})

    # Načíst seznam požadavků na změnu pro MV ČR
    def RegistryAllMinistry(self, ID_Login):
        return self._client.service.RegistryAllMinistry({"ID_Login": ID_Login})

    # Načíst detail požadavku na změnu v registru OJ
    def RegistryDetail(self, ID_Login, ID):
        return self._client.service.RegistryDetail({"ID_Login": ID_Login, "ID": ID})

    # Odeslat zprávu o změně statutára střediska nadřízené jednotce
    def RegistrySendFunctionParentMessage(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistrySendFunctionParentMessage({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Načíst seznam stavů požadavku registru OJ
    def RegistryStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.RegistryStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam typů požadavku registru OJ
    def RegistryTypeAll(self, ID_Login, DisplayName=None, ID_RegistryObject=None):
        return self._client.service.RegistryTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_RegistryObject": ID_RegistryObject})

    # Zrušit požadavek na změnu v registru OJ
    def RegistryUpdateCancel(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistryUpdateCancel({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Uzavřít požadavek na změnu v registru OJ
    def RegistryUpdateClose(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistryUpdateClose({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Odeslat požadavek na změnu v registru OJ na MV ČR
    def RegistryUpdateSend(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistryUpdateSend({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Odeslat zprávy požadavků na změnu registru OJ
    def RegistryUpdateSendMessage(self, ID_Login, ID, Sequence, ID_Unit, IsPropertyOwner, IsPropertyOwnerOld, OldHistoryObjectId, NewHistoryObjectId, ID_PersonCreate, DateCreate, ID_PersonUpdate, DateUpdate, ID_PersonSent, DateSent, ID_PersonClosed, DateClosed, ID_PersonCancel, DateCancel, ID_Function, ID_FunctionType, NewAccount, ID_PersonFunction, ID_PersonFunctionOld, ID_PersonSolving, DateSolving, ID_Document, ID_Statement, StatementYear, ID_DocumentStatement, ID_DocumentDecision, ID_DocumentPropertyAgreement, DisplayName=None, Unit=None, RegistrationNumber=None, IC=None, Street=None, City=None, Postcode=None, PropertyAgreementExtension=None, UnitOld=None, StreetOld=None, CityOld=None, PostcodeOld=None, ID_RegistryObject=None, RegistryObject=None, ID_RegistryType=None, RegistryType=None, ID_RegistryState=None, RegistryState=None, PersonCreate=None, PersonUpdate=None, PersonSent=None, PersonClosed=None, PersonCancel=None, CancelDecision=None, FunctionType=None, PersonFunction=None, PersonFunctionOld=None, Account=None, Note=None, PersonSolving=None, DecisionSeatChangeExtension=None):
        return self._client.service.RegistryUpdateSendMessage({"ID_Login": ID_Login, "ID": ID, "Sequence": Sequence, "ID_Unit": ID_Unit, "IsPropertyOwner": IsPropertyOwner, "IsPropertyOwnerOld": IsPropertyOwnerOld, "OldHistoryObjectId": OldHistoryObjectId, "NewHistoryObjectId": NewHistoryObjectId, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_PersonUpdate": ID_PersonUpdate, "DateUpdate": DateUpdate, "ID_PersonSent": ID_PersonSent, "DateSent": DateSent, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "ID_PersonCancel": ID_PersonCancel, "DateCancel": DateCancel, "ID_Function": ID_Function, "ID_FunctionType": ID_FunctionType, "NewAccount": NewAccount, "ID_PersonFunction": ID_PersonFunction, "ID_PersonFunctionOld": ID_PersonFunctionOld, "ID_PersonSolving": ID_PersonSolving, "DateSolving": DateSolving, "ID_Document": ID_Document, "ID_Statement": ID_Statement, "StatementYear": StatementYear, "ID_DocumentStatement": ID_DocumentStatement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "IC": IC, "Street": Street, "City": City, "Postcode": Postcode, "PropertyAgreementExtension": PropertyAgreementExtension, "UnitOld": UnitOld, "StreetOld": StreetOld, "CityOld": CityOld, "PostcodeOld": PostcodeOld, "ID_RegistryObject": ID_RegistryObject, "RegistryObject": RegistryObject, "ID_RegistryType": ID_RegistryType, "RegistryType": RegistryType, "ID_RegistryState": ID_RegistryState, "RegistryState": RegistryState, "PersonCreate": PersonCreate, "PersonUpdate": PersonUpdate, "PersonSent": PersonSent, "PersonClosed": PersonClosed, "PersonCancel": PersonCancel, "CancelDecision": CancelDecision, "FunctionType": FunctionType, "PersonFunction": PersonFunction, "PersonFunctionOld": PersonFunctionOld, "Account": Account, "Note": Note, "PersonSolving": PersonSolving, "DecisionSeatChangeExtension": DecisionSeatChangeExtension})

    # Zrušit odevzdání hospodářského výkazu jednotky
    def StatementUpdateOpen(self, ID_Login, ID, ID_Unit, Year, IsError, IsDelivered, DateDelivered, DateCreated, IsThousands, IsConsultant, ID_Document, ID_DocumentTempFile, DateSent, ID_PersonSent, DateConfirmed, ID_PersonConfirmed, ID_Registry, ShowOverview, Unit=None, RegistrationNumber=None, ID_StatementType=None, StatementType=None, ID_StatementState=None, StatementState=None, PersonSent=None, PersonConfirmed=None):
        return self._client.service.StatementUpdateOpen({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "IsError": IsError, "IsDelivered": IsDelivered, "DateDelivered": DateDelivered, "DateCreated": DateCreated, "IsThousands": IsThousands, "IsConsultant": IsConsultant, "ID_Document": ID_Document, "ID_DocumentTempFile": ID_DocumentTempFile, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "DateConfirmed": DateConfirmed, "ID_PersonConfirmed": ID_PersonConfirmed, "ID_Registry": ID_Registry, "ShowOverview": ShowOverview, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_StatementType": ID_StatementType, "StatementType": StatementType, "ID_StatementState": ID_StatementState, "StatementState": StatementState, "PersonSent": PersonSent, "PersonConfirmed": PersonConfirmed})

    # Stáhnout soubor se scanem návrhu
    def PersonHonourDownloadScan(self, ID_Login, ID):
        return self._client.service.PersonHonourDownloadScan({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam vyznamenání, které osoba může udělit
    def HonourAllGrant(self, ID_Login, ID, DisplayName=None):
        return self._client.service.HonourAllGrant({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam vyznamenání
    def HonourAll(self, ID_Login, ID, IsActive, DisplayName=None):
        return self._client.service.HonourAll({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "DisplayName": DisplayName})

    # Načíst detail vyznamenání
    def HonourDetail(self, ID_Login, ID):
        return self._client.service.HonourDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst obrázek vyznamenání
    def HonourImage(self, ID_Login, ID):
        return self._client.service.HonourImage({"ID_Login": ID_Login, "ID": ID})

    # Založit vyznamenání
    def HonourInsert(self, ID_Login, ID, IsActive, MaxCount, DisplayName=None, Description=None, FileName=None, ImageContent=None, StateUrl=None, DescriptionUrl=None):
        return self._client.service.HonourInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "MaxCount": MaxCount, "DisplayName": DisplayName, "Description": Description, "FileName": FileName, "ImageContent": ImageContent, "StateUrl": StateUrl, "DescriptionUrl": DescriptionUrl})

    # Načíst seznam jednotek vyznamenání
    def HonourUnitAll(self, ID_Login, ID_Honour, ID_Unit):
        return self._client.service.HonourUnitAll({"ID_Login": ID_Login, "ID_Honour": ID_Honour, "ID_Unit": ID_Unit})

    # Smazat jednotku,  ve které se vyznamenání uděluje
    def HonourUnitDelete(self, ID_Login, ID):
        return self._client.service.HonourUnitDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit jednotku,  ve které se vyznamenání uděluje
    def HonourUnitInsert(self, ID_Login, ID_Honour, ID_Unit):
        return self._client.service.HonourUnitInsert({"ID_Login": ID_Login, "ID_Honour": ID_Honour, "ID_Unit": ID_Unit})

    # Upravit vyznamenání
    def HonourUpdate(self, ID_Login, ID, IsActive, MaxCount, DisplayName=None, Description=None, FileName=None, ImageContent=None, StateUrl=None, DescriptionUrl=None):
        return self._client.service.HonourUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "MaxCount": MaxCount, "DisplayName": DisplayName, "Description": Description, "FileName": FileName, "ImageContent": ImageContent, "StateUrl": StateUrl, "DescriptionUrl": DescriptionUrl})

    # Hledání dospělých osob
    def PersonAllJobs(self, ID_Login, ID, FirstName=None, LastName=None, NickName=None):
        return self._client.service.PersonAllJobs({"ID_Login": ID_Login, "ID": ID, "FirstName": FirstName, "LastName": LastName, "NickName": NickName})

    # Načíst seznam  jubilantů
    def PersonAllJubilant(self, ID_Login, Settings=None):
        return self._client.service.PersonAllJubilant({"ID_Login": ID_Login, "Settings": Settings})

    # Načíst seznam vyznamenání osoby
    def PersonHonourAll(self, IsValid, ID_Login, ID_Person, ID_Honour, YearValidFrom, PersonDisplayName=None, LetterNumber=None, Suggester=None):
        return self._client.service.PersonHonourAll({"IsValid": IsValid, "ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Honour": ID_Honour, "YearValidFrom": YearValidFrom, "PersonDisplayName": PersonDisplayName, "LetterNumber": LetterNumber, "Suggester": Suggester})

    # Načíst seznam vyznamenání osoby
    def PersonHonourAllLogin(self, IsValid, ID_Login, ID_Person, ID_Honour, YearValidFrom, PersonDisplayName=None, LetterNumber=None, Suggester=None):
        return self._client.service.PersonHonourAllLogin({"IsValid": IsValid, "ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Honour": ID_Honour, "YearValidFrom": YearValidFrom, "PersonDisplayName": PersonDisplayName, "LetterNumber": LetterNumber, "Suggester": Suggester})

    # Načíst seznam vyznamenání osoby
    def PersonHonourAllPerson(self, ShowHistory, ID_Login, ID_Person, ID_Honour, IsValid):
        return self._client.service.PersonHonourAllPerson({"ShowHistory": ShowHistory, "ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Honour": ID_Honour, "IsValid": IsValid})

    # Smazat vyznamenání osoby
    def PersonHonourDelete(self, ID_Login, ID):
        return self._client.service.PersonHonourDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail vyznamenání osoby
    def PersonHonourDetail(self, ID_Login, ID):
        return self._client.service.PersonHonourDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit vyznamenání osoby
    def PersonHonourInsert(self, ID_Login, ID_Person, ID_Honour, ValidFrom, ValidTo, ID_PersonSuggester, ID_UnitSuggester, InMemorian, Suggester=None, LetterNumber=None, Reason=None, FileName=None, FileContent=None, Person=None):
        return self._client.service.PersonHonourInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Honour": ID_Honour, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSuggester": ID_PersonSuggester, "ID_UnitSuggester": ID_UnitSuggester, "InMemorian": InMemorian, "Suggester": Suggester, "LetterNumber": LetterNumber, "Reason": Reason, "FileName": FileName, "FileContent": FileContent, "Person": Person})

    # Upravit vyznamenání osoby
    def PersonHonourUpdate(self, ID_Login, ID, ID_Person, ID_Honour, ValidFrom, ValidTo, ID_PersonSuggester, ID_UnitSuggester, InMemorian, Person=None, Honour=None, Suggester=None, SuggesterDisplayName=None, LetterNumber=None, Reason=None, FileName=None, FileContent=None, IdentificationCode=None, IdentificationCodeSuggester=None):
        return self._client.service.PersonHonourUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Honour": ID_Honour, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSuggester": ID_PersonSuggester, "ID_UnitSuggester": ID_UnitSuggester, "InMemorian": InMemorian, "Person": Person, "Honour": Honour, "Suggester": Suggester, "SuggesterDisplayName": SuggesterDisplayName, "LetterNumber": LetterNumber, "Reason": Reason, "FileName": FileName, "FileContent": FileContent, "IdentificationCode": IdentificationCode, "IdentificationCodeSuggester": IdentificationCodeSuggester})

    # Editace typu osoby
    def PersonUpdatePersonType(self, ID_Login, ID, ID_PersonType=None):
        return self._client.service.PersonUpdatePersonType({"ID_Login": ID_Login, "ID": ID, "ID_PersonType": ID_PersonType})

    # Načíst seznam služeb registrace
    def RegistrationServiceAll(self, ID_Login, ID_UnitRegistration, ID_RegistrationServiceType=None):
        return self._client.service.RegistrationServiceAll({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration, "ID_RegistrationServiceType": ID_RegistrationServiceType})

    # Založit službu registrace
    def RegistrationServiceInsert(self, ID_Login, ID_UnitRegistration, Ammount, ID_VatRate, ID_RegistrationServiceType=None):
        return self._client.service.RegistrationServiceInsert({"ID_Login": ID_Login, "ID_UnitRegistration": ID_UnitRegistration, "Ammount": Ammount, "ID_VatRate": ID_VatRate, "ID_RegistrationServiceType": ID_RegistrationServiceType})

    # Načíst seznam typů služeb registrace
    def RegistrationServiceTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.RegistrationServiceTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam registrací nadřízené jednotky
    def UnitRegistrationAllParent(self, ID_Login, ID_Unit):
        return self._client.service.UnitRegistrationAllParent({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Nastavit zasílání časopisu pro rodiče členům jednotky
    def UnitUpdateJournalParent(self, ID_Login, ID, ID_Group, ID_Unit, ContainsMembers, CommissionDeadline, IsVatPayer, ID_TroopArt, CanUpdateRegistrationNumber, ID_DocumentLogo, IsUnitCancel, JournalParent, ChangeFreeJournal, ID_UnitParent, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, ID_PersonChangeName, DateChangeName, IsPropertyOwner, ID_TempFilePropertyAgreement, ID_DocumentDecision, ID_DocumentPropertyAgreement, ID_TempFileSeatChange, ID_TempFileUnitLogo, ID_UnitType=None, UnitType=None, DisplayName=None, SortName=None, RegistrationNumber=None, ShortRegistrationNumber=None, Location=None, LocationNew=None, IC=None, DIC=None, FileReference=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, TroopArt=None, LogoContent=None, LogoExtension=None, AddressDistrict=None, PostalDistrict=None, NewDisplayName=None, CompleteDisplayName=None, PersonChangeName=None, PropertyAgreementExtension=None, PropertyAgreementContent=None, TroopArtKey=None, ID_JournalNovice=None, ID_JournalDeliveryType=None, FullDisplayName=None, DecisionSeatChangeExtension=None, ShopDiscountBarcode=None, ID_UnitFoundReason=None, UnitFoundReason=None, UnitFoundDescription=None):
        return self._client.service.UnitUpdateJournalParent({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_Unit": ID_Unit, "ContainsMembers": ContainsMembers, "CommissionDeadline": CommissionDeadline, "IsVatPayer": IsVatPayer, "ID_TroopArt": ID_TroopArt, "CanUpdateRegistrationNumber": CanUpdateRegistrationNumber, "ID_DocumentLogo": ID_DocumentLogo, "IsUnitCancel": IsUnitCancel, "JournalParent": JournalParent, "ChangeFreeJournal": ChangeFreeJournal, "ID_UnitParent": ID_UnitParent, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_PersonChangeName": ID_PersonChangeName, "DateChangeName": DateChangeName, "IsPropertyOwner": IsPropertyOwner, "ID_TempFilePropertyAgreement": ID_TempFilePropertyAgreement, "ID_DocumentDecision": ID_DocumentDecision, "ID_DocumentPropertyAgreement": ID_DocumentPropertyAgreement, "ID_TempFileSeatChange": ID_TempFileSeatChange, "ID_TempFileUnitLogo": ID_TempFileUnitLogo, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "DisplayName": DisplayName, "SortName": SortName, "RegistrationNumber": RegistrationNumber, "ShortRegistrationNumber": ShortRegistrationNumber, "Location": Location, "LocationNew": LocationNew, "IC": IC, "DIC": DIC, "FileReference": FileReference, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "TroopArt": TroopArt, "LogoContent": LogoContent, "LogoExtension": LogoExtension, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "NewDisplayName": NewDisplayName, "CompleteDisplayName": CompleteDisplayName, "PersonChangeName": PersonChangeName, "PropertyAgreementExtension": PropertyAgreementExtension, "PropertyAgreementContent": PropertyAgreementContent, "TroopArtKey": TroopArtKey, "ID_JournalNovice": ID_JournalNovice, "ID_JournalDeliveryType": ID_JournalDeliveryType, "FullDisplayName": FullDisplayName, "DecisionSeatChangeExtension": DecisionSeatChangeExtension, "ShopDiscountBarcode": ShopDiscountBarcode, "ID_UnitFoundReason": ID_UnitFoundReason, "UnitFoundReason": UnitFoundReason, "UnitFoundDescription": UnitFoundDescription})

    # Načíst seznam činovníků bez vyplněného kontaktu
    def PersonAllUnitRegistrationMistake(self, ID_Login, ID_Unit, ID_ContactType=None):
        return self._client.service.PersonAllUnitRegistrationMistake({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_ContactType": ID_ContactType})

    # Načíst souhrné informace o skautském adresáři
    def PersonCatalogSummary(self, ID_Login):
        return self._client.service.PersonCatalogSummary({"ID_Login": ID_Login})

    # Načíst seznam osob pro skautský adresář
    def PersonAllCatalog(self, ID_Login, RegistrationNumberStartWith, ID_OfferType, Name=None, City=None, RegistrationNumber=None, Unit=None, Phone=None, Email=None):
        return self._client.service.PersonAllCatalog({"ID_Login": ID_Login, "RegistrationNumberStartWith": RegistrationNumberStartWith, "ID_OfferType": ID_OfferType, "Name": Name, "City": City, "RegistrationNumber": RegistrationNumber, "Unit": Unit, "Phone": Phone, "Email": Email})

    # Načtení limitů sts čísel pro osobu
    def PersonDetailTelephonyLimit(self, ID_Login, ID):
        return self._client.service.PersonDetailTelephonyLimit({"ID_Login": ID_Login, "ID": ID})

    # Editace limitů STS čísel osoby
    def PersonUpdateTelephonyLimit(self, ID_Login, ID, TelephonyLimit, DataLimit):
        return self._client.service.PersonUpdateTelephonyLimit({"ID_Login": ID_Login, "ID": ID, "TelephonyLimit": TelephonyLimit, "DataLimit": DataLimit})

    # Zobrazit detail limitů STS čísel jednotky
    def UnitDetailTelephonyLimit(self, ID_Login, ID):
        return self._client.service.UnitDetailTelephonyLimit({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam typů jednotek  s limity čísel
    def UnitTypeAllLimit(self, ID_Login, DisplayName=None):
        return self._client.service.UnitTypeAllLimit({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit typ jednotky
    def UnitTypeUpdate(self, ID_Login, Level, ContainsMembers, FreeAttachments, CommissionCount, CommissionDeadline, CallLimit, DataLimit, ID=None, DisplayName=None, Note=None, Birdos=None, ID_Instance=None):
        return self._client.service.UnitTypeUpdate({"ID_Login": ID_Login, "Level": Level, "ContainsMembers": ContainsMembers, "FreeAttachments": FreeAttachments, "CommissionCount": CommissionCount, "CommissionDeadline": CommissionDeadline, "CallLimit": CallLimit, "DataLimit": DataLimit, "ID": ID, "DisplayName": DisplayName, "Note": Note, "Birdos": Birdos, "ID_Instance": ID_Instance})

    # Upravit limit STS čísel jednotky
    def UnitUpdateTelephonyLimit(self, ID_Login, ID, TelephonyLimit, DataLimit, DefaultCallLimit, DefaultDataLimit):
        return self._client.service.UnitUpdateTelephonyLimit({"ID_Login": ID_Login, "ID": ID, "TelephonyLimit": TelephonyLimit, "DataLimit": DataLimit, "DefaultCallLimit": DefaultCallLimit, "DefaultDataLimit": DefaultDataLimit})

    # Načíst seznam osob
    def PersonAllIdentificationCode(self, ID_Login, IdentificationCode=None, IdentificationCodeStartsWith=None):
        return self._client.service.PersonAllIdentificationCode({"ID_Login": ID_Login, "IdentificationCode": IdentificationCode, "IdentificationCodeStartsWith": IdentificationCodeStartsWith})

    # Hledání v registru OJ
    def UnitAllRegistryBasic(self, ID_Login, ID_Application, IsValid, Search=None):
        return self._client.service.UnitAllRegistryBasic({"ID_Login": ID_Login, "ID_Application": ID_Application, "IsValid": IsValid, "Search": Search})

    # Editace základních údajů osoby
    def PersonUpdateAddress(self, ID_Login, ID, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None):
        return self._client.service.PersonUpdateAddress({"ID_Login": ID_Login, "ID": ID, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState})

    # Editace základních údajů osoby
    def PersonUpdateBasic(self, ID_Login, ID, Birthday, YearFrom, ID_Sex=None, FirstName=None, LastName=None, NickName=None, MaidenName=None, Street=None, City=None, Postcode=None, State=None):
        return self._client.service.PersonUpdateBasic({"ID_Login": ID_Login, "ID": ID, "Birthday": Birthday, "YearFrom": YearFrom, "ID_Sex": ID_Sex, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "MaidenName": MaidenName, "Street": Street, "City": City, "Postcode": Postcode, "State": State})

    # Hledání osob pro účastníky tábora
    def PersonAllEventCamp(self, ID_Login, ID_EventCamp, ID, DisplayName=None, IdentificationCode=None, IdentificationCodeStartsWith=None, EventFunctionTypeKey=None):
        return self._client.service.PersonAllEventCamp({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "ID": ID, "DisplayName": DisplayName, "IdentificationCode": IdentificationCode, "IdentificationCodeStartsWith": IdentificationCodeStartsWith, "EventFunctionTypeKey": EventFunctionTypeKey})

    # Hledání osob pro hromadné přidání účastníků tábora
    def PersonAllEventCampMulti(self, ID_Login, ID_EventCamp):
        return self._client.service.PersonAllEventCampMulti({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp})

    # Načíst seznam středisek, pro založení tábora
    def UnitAllCamp(self, ID_Login):
        return self._client.service.UnitAllCamp({"ID_Login": ID_Login})

    # Hledání osob pro účast na sněmu
    def PersonAllUstredi(self, ID_Login, ID_EventCongress, ID, DisplayName=None):
        return self._client.service.PersonAllUstredi({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID": ID, "DisplayName": DisplayName})

    # Hledání dospělých osob
    def PersonAllPublic(self, ID_Login, ID, FirstName=None, LastName=None, NickName=None):
        return self._client.service.PersonAllPublic({"ID_Login": ID_Login, "ID": ID, "FirstName": FirstName, "LastName": LastName, "NickName": NickName})

    # Načíst seznam účtů
    def AccountAll(self, ID_Login, ID_Application, ID_Unit, ID_Bank, ShowHistory, IsValid):
        return self._client.service.AccountAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ID_Bank": ID_Bank, "ShowHistory": ShowHistory, "IsValid": IsValid})

    # Smazat účet
    def AccountDelete(self, ID_Login, ID):
        return self._client.service.AccountDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail účtu
    def AccountDetail(self, ID_Login, ID):
        return self._client.service.AccountDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit účet
    def AccountInsert(self, ID_Login, ID, ID_Unit, ValidTo, ID_Bank, IsMain, DisplayName=None, Unit=None, Bank=None, AccountPrefix=None, AccountNumber=None, Street=None, City=None, Postcode=None, Note=None):
        return self._client.service.AccountInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ValidTo": ValidTo, "ID_Bank": ID_Bank, "IsMain": IsMain, "DisplayName": DisplayName, "Unit": Unit, "Bank": Bank, "AccountPrefix": AccountPrefix, "AccountNumber": AccountNumber, "Street": Street, "City": City, "Postcode": Postcode, "Note": Note})

    # Upravit účet
    def AccountUpdate(self, ID_Login, ID, ID_Unit, ValidTo, ID_Bank, IsMain, DisplayName=None, Unit=None, Bank=None, AccountPrefix=None, AccountNumber=None, Street=None, City=None, Postcode=None, Note=None):
        return self._client.service.AccountUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ValidTo": ValidTo, "ID_Bank": ID_Bank, "IsMain": IsMain, "DisplayName": DisplayName, "Unit": Unit, "Bank": Bank, "AccountPrefix": AccountPrefix, "AccountNumber": AccountNumber, "Street": Street, "City": City, "Postcode": Postcode, "Note": Note})

    # Načíst seznam náborových kategorií
    def AdvertisingCategoryAll(self, ID_Login, ID_Application, ID_Unit, ID_MeetingDate, ID_Sex=None):
        return self._client.service.AdvertisingCategoryAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ID_MeetingDate": ID_MeetingDate, "ID_Sex": ID_Sex})

    # Smazat náborovou kategorii
    def AdvertisingCategoryDelete(self, ID_Login, ID):
        return self._client.service.AdvertisingCategoryDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail náborové kategorie
    def AdvertisingCategoryDetail(self, ID_Login, ID):
        return self._client.service.AdvertisingCategoryDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit náborovou kategorii
    def AdvertisingCategoryInsert(self, ID_Login, ID, ID_Unit, AgeFrom, AgeTo, ID_MeetingDate, Unit=None, ID_Sex=None, Sex=None, MeetingDate=None, Note=None):
        return self._client.service.AdvertisingCategoryInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "AgeFrom": AgeFrom, "AgeTo": AgeTo, "ID_MeetingDate": ID_MeetingDate, "Unit": Unit, "ID_Sex": ID_Sex, "Sex": Sex, "MeetingDate": MeetingDate, "Note": Note})

    # Upravit náborovou kategorii
    def AdvertisingCategoryUpdate(self, ID_Login, ID, ID_Unit, AgeFrom, AgeTo, ID_MeetingDate, Unit=None, ID_Sex=None, Sex=None, MeetingDate=None, Note=None):
        return self._client.service.AdvertisingCategoryUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "AgeFrom": AgeFrom, "AgeTo": AgeTo, "ID_MeetingDate": ID_MeetingDate, "Unit": Unit, "ID_Sex": ID_Sex, "Sex": Sex, "MeetingDate": MeetingDate, "Note": Note})

    # Načíst náborové informace
    def AdvertisingDetail(self, ID_Login, ID_Application, ID_Unit):
        return self._client.service.AdvertisingDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit})

    # Velká přehledová tabulka náborových údajů
    def AdvertisingSummary(self, ID_Login, ID_Application, ID_Unit, IncludeChildUnits, ID_Realty, Distance, GpsLatitude, GpsLongitude):
        return self._client.service.AdvertisingSummary({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "IncludeChildUnits": IncludeChildUnits, "ID_Realty": ID_Realty, "Distance": Distance, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude})

    # Upravit náborové informace
    def AdvertisingUpdate(self, ID_Login, ID, ID_Unit, IsWater, Unit=None, RegistrationNumber=None, ID_UnitType=None, UnitType=None, Note=None):
        return self._client.service.AdvertisingUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "IsWater": IsWater, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Note": Note})

    # Načíst seznam zaměření
    def AlignmentAll(self, ID_Login, ID_Application, ID_Unit, ID_AlignmentType, ShowHistory, IsValid):
        return self._client.service.AlignmentAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Unit": ID_Unit, "ID_AlignmentType": ID_AlignmentType, "ShowHistory": ShowHistory, "IsValid": IsValid})

    # Načíst detail zaměření
    def AlignmentDetail(self, ID_Login, ID):
        return self._client.service.AlignmentDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit zaměření
    def AlignmentInsert(self, ID_Login, ID, ID_Unit, ValidFrom, ValidTo, ID_AlignmentType, Unit=None, AlignmentType=None, ColorMargin=None, ColorCenter=None):
        return self._client.service.AlignmentInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_AlignmentType": ID_AlignmentType, "Unit": Unit, "AlignmentType": AlignmentType, "ColorMargin": ColorMargin, "ColorCenter": ColorCenter})

    # Načíst seznam zaměření
    def AlignmentTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.AlignmentTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit zaměření
    def AlignmentUpdate(self, ID_Login, ID, ID_Unit, ValidFrom, ValidTo, ID_AlignmentType, Unit=None, AlignmentType=None, ColorMargin=None, ColorCenter=None):
        return self._client.service.AlignmentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_AlignmentType": ID_AlignmentType, "Unit": Unit, "AlignmentType": AlignmentType, "ColorMargin": ColorMargin, "ColorCenter": ColorCenter})

    # Načíst seznam zdravotních pojišťoven
    def AssuranceAll(self, ID_Login, ID_Application, DisplayName=None):
        return self._client.service.AssuranceAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "DisplayName": DisplayName})

    # Načíst seznam bank
    def BankAll(self, ID_Login, DisplayName=None, Code=None):
        return self._client.service.BankAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "Code": Code})

    # Ověření, zda má osoba nárok na časopis zdarma
    def PersonDetailCanHaveFreeJournal(self, ID_Login, ID):
        return self._client.service.PersonDetailCanHaveFreeJournal({"ID_Login": ID_Login, "ID": ID})

    # Načíst informace pro dashboard
    def PersonDetailDashboard(self, ID_Login):
        return self._client.service.PersonDetailDashboard({"ID_Login": ID_Login})

    # Načtení počtu přijatých a nepřečtených zpráv osoby
    def PersonDetailMessageCount(self, ID_Login):
        return self._client.service.PersonDetailMessageCount({"ID_Login": ID_Login})

    # Ověření, zda je osoba členem organizace
    def PersonDetailMembership(self, ID_Login, ID_Application, IdentificationCode=None):
        return self._client.service.PersonDetailMembership({"ID_Login": ID_Login, "ID_Application": ID_Application, "IdentificationCode": IdentificationCode})

    # Načíst seznam zákonných zástupce osoby
    def PersonParentAll(self, ID_Login, ID_Application, ID_Person, ID, ID_PersonParent, ID_ParentType=None):
        return self._client.service.PersonParentAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Person": ID_Person, "ID": ID, "ID_PersonParent": ID_PersonParent, "ID_ParentType": ID_ParentType})

    # Smazat zákonného zástupce osoby
    def PersonParentDelete(self, ID_Login, ID):
        return self._client.service.PersonParentDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail zákonného zástupce osoby
    def PersonParentDetail(self, ID_Login, ID):
        return self._client.service.PersonParentDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit zákonného zástupce osoby
    def PersonParentInsert(self, ID_Login, ID, ID_Person, ID_PersonParent, ParentHasAccount, Person=None, Parent=None, ID_ParentType=None, ParentType=None, FirstName=None, LastName=None, Phone=None, Email=None, Note=None, ParentNote=None, ParentCode=None):
        return self._client.service.PersonParentInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_PersonParent": ID_PersonParent, "ParentHasAccount": ParentHasAccount, "Person": Person, "Parent": Parent, "ID_ParentType": ID_ParentType, "ParentType": ParentType, "FirstName": FirstName, "LastName": LastName, "Phone": Phone, "Email": Email, "Note": Note, "ParentNote": ParentNote, "ParentCode": ParentCode})

    # Upravit zákonného zástupce osoby
    def PersonParentUpdate(self, ID_Login, ID, ID_Person, ID_PersonParent, ParentHasAccount, Person=None, Parent=None, ID_ParentType=None, ParentType=None, FirstName=None, LastName=None, Phone=None, Email=None, Note=None, ParentNote=None, ParentCode=None):
        return self._client.service.PersonParentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_PersonParent": ID_PersonParent, "ParentHasAccount": ParentHasAccount, "Person": Person, "Parent": Parent, "ID_ParentType": ID_ParentType, "ParentType": ParentType, "FirstName": FirstName, "LastName": LastName, "Phone": Phone, "Email": Email, "Note": Note, "ParentNote": ParentNote, "ParentCode": ParentCode})

    # Načíst detail potvrzení o studiu pro osobu
    def PersonSchoolDetailPerson(self, ID_Login, ID_Person):
        return self._client.service.PersonSchoolDetailPerson({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Upravit údaje k potvrzení o studiu
    def PersonSchoolUpdateSchool(self, ID_Login, ID, ID_Person, DateCreate, ID_TempFile, ID_PersonSchoolTempFile, ID_DocumentPhoto, ID_DocumentScan, Person=None, DisplayName=None, City=None, Extension=None, Scan=None, PhotoExtension=None, Photo=None):
        return self._client.service.PersonSchoolUpdateSchool({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "DateCreate": DateCreate, "ID_TempFile": ID_TempFile, "ID_PersonSchoolTempFile": ID_PersonSchoolTempFile, "ID_DocumentPhoto": ID_DocumentPhoto, "ID_DocumentScan": ID_DocumentScan, "Person": Person, "DisplayName": DisplayName, "City": City, "Extension": Extension, "Scan": Scan, "PhotoExtension": PhotoExtension, "Photo": Photo})

    # Editace osoby
    def PersonDeletePhoto(self, ID_Login, ID):
        return self._client.service.PersonDeletePhoto({"ID_Login": ID_Login, "ID": ID})

    # Změna údajů osoby
    def PersonUpdatePersonChange(self, ID_Login, ID_Application, Code, Birthday, BirthdayYear, IsForeign, YearFrom, ID_User, OnlyValidate, IsPostalAuthenticated, IsAddressAuthenticated, RejectDataStorage, IdentificationCodeForce, GenerateSecurityCode, ID_TempFile, ID_PersonPhotoBig, ID_PersonPhotoMedium, ID_PersonPhotoNormal, ID_PersonPhotoSmall, IdentificationCode=None, FirstName=None, LastName=None, NickName=None, Address=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalAddress=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Note=None, ID_Sex=None, RegistrationNumber=None, PhotoExtension=None, PhotoContent=None, MaidenName=None, AddressDistrict=None, PostalDistrict=None, UnitEnrollExtension=None, UnitEnroll=None):
        return self._client.service.PersonUpdatePersonChange({"ID_Login": ID_Login, "ID_Application": ID_Application, "Code": Code, "Birthday": Birthday, "BirthdayYear": BirthdayYear, "IsForeign": IsForeign, "YearFrom": YearFrom, "ID_User": ID_User, "OnlyValidate": OnlyValidate, "IsPostalAuthenticated": IsPostalAuthenticated, "IsAddressAuthenticated": IsAddressAuthenticated, "RejectDataStorage": RejectDataStorage, "IdentificationCodeForce": IdentificationCodeForce, "GenerateSecurityCode": GenerateSecurityCode, "ID_TempFile": ID_TempFile, "ID_PersonPhotoBig": ID_PersonPhotoBig, "ID_PersonPhotoMedium": ID_PersonPhotoMedium, "ID_PersonPhotoNormal": ID_PersonPhotoNormal, "ID_PersonPhotoSmall": ID_PersonPhotoSmall, "IdentificationCode": IdentificationCode, "FirstName": FirstName, "LastName": LastName, "NickName": NickName, "Address": Address, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalAddress": PostalAddress, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Note": Note, "ID_Sex": ID_Sex, "RegistrationNumber": RegistrationNumber, "PhotoExtension": PhotoExtension, "PhotoContent": PhotoContent, "MaidenName": MaidenName, "AddressDistrict": AddressDistrict, "PostalDistrict": PostalDistrict, "UnitEnrollExtension": UnitEnrollExtension, "UnitEnroll": UnitEnroll})

    # Načíst seznam nových kvalifikací v daném období
    def QualificationAllNew(self, ID_Login, From, To, ID_QualificationTypeList=None):
        return self._client.service.QualificationAllNew({"ID_Login": ID_Login, "From": From, "To": To, "ID_QualificationTypeList": ID_QualificationTypeList})

    # Načíst názvy typů kvalifikace ze zadaného seznamu
    def QualificationTypeAllList(self, ID_Login, ID_QualificationTypeList=None):
        return self._client.service.QualificationTypeAllList({"ID_Login": ID_Login, "ID_QualificationTypeList": ID_QualificationTypeList})

    # Načíst seznam nemovitostí pro soubor nemovitostí
    def RealtyAllRealtyTypeCountPublic(self, ID_Login, ID_Application):
        return self._client.service.RealtyAllRealtyTypeCountPublic({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Přepočet blízkých bodů
    def RealtyCollectionGroupByPosition(self, ID_Login):
        return self._client.service.RealtyCollectionGroupByPosition({"ID_Login": ID_Login})

    # Načíst seznam půjčitelných nemovitostí/souboru nemovitostí
    def RealtyCollectionAllBorrowable(self, ID_Application, ID_Login, GpsLatitude, GpsLongitude, Distance, Price, Date, Capacity, BorrowableForeign, DisplayName=None, RegionList=None, DistrictList=None, City=None, Unit=None, OwnerTypeList=None, RealtyTypeList=None, OccupationEquipmentList=None, RealtyCollectionLocationList=None, PriceType=None, OccupationLanguageList=None, OccupationTagList=None):
        return self._client.service.RealtyCollectionAllBorrowable({"ID_Application": ID_Application, "ID_Login": ID_Login, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "Distance": Distance, "Price": Price, "Date": Date, "Capacity": Capacity, "BorrowableForeign": BorrowableForeign, "DisplayName": DisplayName, "RegionList": RegionList, "DistrictList": DistrictList, "City": City, "Unit": Unit, "OwnerTypeList": OwnerTypeList, "RealtyTypeList": RealtyTypeList, "OccupationEquipmentList": OccupationEquipmentList, "RealtyCollectionLocationList": RealtyCollectionLocationList, "PriceType": PriceType, "OccupationLanguageList": OccupationLanguageList, "OccupationTagList": OccupationTagList})

    # Načíst seznam souborů nemovitostí
    def RealtyCollectionAll(self, ID_Login, ID_Unit, ID, ID_User, DisplayName=None):
        return self._client.service.RealtyCollectionAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_User": ID_User, "DisplayName": DisplayName})

    # Načíst detail půjčitelné nemovitosti/souboru nemovitostí
    def RealtyCollectionDetailBorrowable(self, ID_Application, ID, ID_Login):
        return self._client.service.RealtyCollectionDetailBorrowable({"ID_Application": ID_Application, "ID": ID, "ID_Login": ID_Login})

    # Načíst detail souboru nemovitostí
    def RealtyCollectionDetailPhoto(self, ID_TempFilePhoto, ID_Login, ID, ID_Unit, ID_User, IsActive, GpsLatitude, GpsLongitude, HasAddress, ID_Region, ID_Document, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, Unit=None, UnitRegistrationNumber=None, Owner=None, DisplayName=None, Description=None, Web=None, Street=None, City=None, Postcode=None, District=None, TransportationMethods=None, TransportationMethodsText=None, TransportDescription=None, Locations=None, LocationsText=None, PointsOfInterest=None, Note=None, Region=None, Storage=None):
        return self._client.service.RealtyCollectionDetailPhoto({"ID_TempFilePhoto": ID_TempFilePhoto, "ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_User": ID_User, "IsActive": IsActive, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "HasAddress": HasAddress, "ID_Region": ID_Region, "ID_Document": ID_Document, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber, "Owner": Owner, "DisplayName": DisplayName, "Description": Description, "Web": Web, "Street": Street, "City": City, "Postcode": Postcode, "District": District, "TransportationMethods": TransportationMethods, "TransportationMethodsText": TransportationMethodsText, "TransportDescription": TransportDescription, "Locations": Locations, "LocationsText": LocationsText, "PointsOfInterest": PointsOfInterest, "Note": Note, "Region": Region, "Storage": Storage})

    # Založit soubor nemovitostí
    def RealtyCollectionInsert(self, ID_TempFilePhoto, RealtyIsPower, ID_RealtyTempFilePhoto, ID_Login, ID_Unit, ID_User, HasAddress, GpsLatitude, GpsLongitude, LVNumber, Acreage, FotogalleryUrl=None, RealtyDisplayName=None, RealtyDescription=None, RealtyFotogalleryUrl=None, ID_RealtyOwnerType=None, RealtyOwnerTypeNote=None, RealtyNote=None, ID_RealtyRegisterType=None, DisplayName=None, Description=None, Web=None, Street=None, City=None, Postcode=None, District=None, TransportationMethods=None, TransportDescription=None, PointsOfInterest=None, Locations=None, Note=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None):
        return self._client.service.RealtyCollectionInsert({"ID_TempFilePhoto": ID_TempFilePhoto, "RealtyIsPower": RealtyIsPower, "ID_RealtyTempFilePhoto": ID_RealtyTempFilePhoto, "ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_User": ID_User, "HasAddress": HasAddress, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "LVNumber": LVNumber, "Acreage": Acreage, "FotogalleryUrl": FotogalleryUrl, "RealtyDisplayName": RealtyDisplayName, "RealtyDescription": RealtyDescription, "RealtyFotogalleryUrl": RealtyFotogalleryUrl, "ID_RealtyOwnerType": ID_RealtyOwnerType, "RealtyOwnerTypeNote": RealtyOwnerTypeNote, "RealtyNote": RealtyNote, "ID_RealtyRegisterType": ID_RealtyRegisterType, "DisplayName": DisplayName, "Description": Description, "Web": Web, "Street": Street, "City": City, "Postcode": Postcode, "District": District, "TransportationMethods": TransportationMethods, "TransportDescription": TransportDescription, "PointsOfInterest": PointsOfInterest, "Locations": Locations, "Note": Note, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType})

    # Načíst detail nemovitosti
    def RealtyDetailPhoto(self, ID_Login, ID, ID_RealtyType, GpsLatitude, GpsLongitude, ID_RealtyCollection, IsPower, ValidTo, IsActive, ID_TempFilePhoto, IsAddressAuthenticated, ID_Document, LVNumber, Acreage, RealtyGpsLatitude, RealtyGpsLongitude, CoordinateX, CoordinateY, DisplayName=None, RealtyType=None, Street=None, City=None, Postcode=None, Description=None, Note=None, RealtyCollection=None, ID_OwnerType=None, OwnerType=None, OwnerTypeNote=None, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, District=None, Storage=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None, Unit=None, UnitRegistrationNumber=None):
        return self._client.service.RealtyDetailPhoto({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ValidTo": ValidTo, "IsActive": IsActive, "ID_TempFilePhoto": ID_TempFilePhoto, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_Document": ID_Document, "LVNumber": LVNumber, "Acreage": Acreage, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "CoordinateX": CoordinateX, "CoordinateY": CoordinateY, "DisplayName": DisplayName, "RealtyType": RealtyType, "Street": Street, "City": City, "Postcode": Postcode, "Description": Description, "Note": Note, "RealtyCollection": RealtyCollection, "ID_OwnerType": ID_OwnerType, "OwnerType": OwnerType, "OwnerTypeNote": OwnerTypeNote, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "District": District, "Storage": Storage, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber})

    # Smazat dokument
    def RealtyDocumentDelete(self, ID_Login, ID):
        return self._client.service.RealtyDocumentDelete({"ID_Login": ID_Login, "ID": ID})

    # No documentation
    def RealtyDocumentDetail(self, ID_Login, ID):
        return self._client.service.RealtyDocumentDetail({"ID_Login": ID_Login, "ID": ID})

    # Stáhnout dokument
    def RealtyDocumentDownload(self, ID_Login, ID):
        return self._client.service.RealtyDocumentDownload({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam členských karet
    def MemberCardAllMemberCardInvoice(self, ID_Login, ID_MemberCardInvoice):
        return self._client.service.MemberCardAllMemberCardInvoice({"ID_Login": ID_Login, "ID_MemberCardInvoice": ID_MemberCardInvoice})

    # Načíst seznam členských karet pro jednotku
    def MemberCardAllUnit(self, ID_Login, ID_Unit, ID, IncludeChild, DisplayName=None, ID_MemberCardType=None, OnlyValid=None, PersonWithoutMeberCard=None, ValidTo=None, OnlyInvalid=None):
        return self._client.service.MemberCardAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "IncludeChild": IncludeChild, "DisplayName": DisplayName, "ID_MemberCardType": ID_MemberCardType, "OnlyValid": OnlyValid, "PersonWithoutMeberCard": PersonWithoutMeberCard, "ValidTo": ValidTo, "OnlyInvalid": OnlyInvalid})

    # Načíst všechny faktury za členské karty
    def MemberCardInvoiceAll(self, ID_Login, ID_Unit, ID, ID_MemberCardInvoiceGenerate, DateGeneratingFrom, DateGeneratingTo, DisplayName=None, ID_MemberCardInvoiceState=None):
        return self._client.service.MemberCardInvoiceAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_MemberCardInvoiceGenerate": ID_MemberCardInvoiceGenerate, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "DisplayName": DisplayName, "ID_MemberCardInvoiceState": ID_MemberCardInvoiceState})

    # Načíst detail faktury za členské karty
    def MemberCardInvoiceDetail(self, ID_Login, ID):
        return self._client.service.MemberCardInvoiceDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam generování faktur za členské karty
    def MemberCardInvoiceGenerateAll(self, ID_Login, ID, ID_Person, ID_Error, ID_MemberCardInvoiceGenerateState=None):
        return self._client.service.MemberCardInvoiceGenerateAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Error": ID_Error, "ID_MemberCardInvoiceGenerateState": ID_MemberCardInvoiceGenerateState})

    # Založit generování faktur za členské karty
    def MemberCardInvoiceGenerateInsert(self, ID_Login, ID, DateGenerating, ID_Person, ID_Error, Person=None, ID_MemberCardInvoiceGenerateState=None, MemberCardInvoiceGenerateState=None, Error=None):
        return self._client.service.MemberCardInvoiceGenerateInsert({"ID_Login": ID_Login, "ID": ID, "DateGenerating": DateGenerating, "ID_Person": ID_Person, "ID_Error": ID_Error, "Person": Person, "ID_MemberCardInvoiceGenerateState": ID_MemberCardInvoiceGenerateState, "MemberCardInvoiceGenerateState": MemberCardInvoiceGenerateState, "Error": Error})

    # Upravit generování faktur za členské karty
    def MemberCardInvoiceGenerateUpdate(self, ID_Login, ID, DateGenerating, ID_Person, ID_Error, Person=None, ID_MemberCardInvoiceGenerateState=None, MemberCardInvoiceGenerateState=None, Error=None):
        return self._client.service.MemberCardInvoiceGenerateUpdate({"ID_Login": ID_Login, "ID": ID, "DateGenerating": DateGenerating, "ID_Person": ID_Person, "ID_Error": ID_Error, "Person": Person, "ID_MemberCardInvoiceGenerateState": ID_MemberCardInvoiceGenerateState, "MemberCardInvoiceGenerateState": MemberCardInvoiceGenerateState, "Error": Error})

    # Vygenerovat faktury
    def MemberCardInvoiceGenerateUpdateGenerate(self, ID_Login, ID, DateGenerating, ID_Person, ID_Error, Person=None, ID_MemberCardInvoiceGenerateState=None, MemberCardInvoiceGenerateState=None, Error=None):
        return self._client.service.MemberCardInvoiceGenerateUpdateGenerate({"ID_Login": ID_Login, "ID": ID, "DateGenerating": DateGenerating, "ID_Person": ID_Person, "ID_Error": ID_Error, "Person": Person, "ID_MemberCardInvoiceGenerateState": ID_MemberCardInvoiceGenerateState, "MemberCardInvoiceGenerateState": MemberCardInvoiceGenerateState, "Error": Error})

    # Načíst seznam stavů faktury za členské karty
    def MemberCardInvoiceStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.MemberCardInvoiceStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Aktivuje karty podkladů pro tisk karet
    def MemberCardPrintActivate(self, ID_Login, ID, ValidFrom):
        return self._client.service.MemberCardPrintActivate({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom})

    # Přidá karty do podkladu pro tisk karet
    def MemberCardPrintAddCards(self, ID_Login, ID):
        return self._client.service.MemberCardPrintAddCards({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail podkladu pro tisk karty
    def MemberCardPrintDetail(self, ID_Login, ID):
        return self._client.service.MemberCardPrintDetail({"ID_Login": ID_Login, "ID": ID})

    # Generování souboru s podklady pro tisk karet
    def MemberCardPrintUpdateGenerating(self, ID_Login, ID):
        return self._client.service.MemberCardPrintUpdateGenerating({"ID_Login": ID_Login, "ID": ID})

    # Ukončit platnost prošlých karet
    def MemberCardUpdateExpired(self, ID_Login):
        return self._client.service.MemberCardUpdateExpired({"ID_Login": ID_Login})

    # Načíst seznam členství osob v jednotce pro zařazení do google skupiny
    def MembershipAllGoogleGroup(self, ID_Login, ID_GoogleGroup, OnlyDirectMember, Person=None):
        return self._client.service.MembershipAllGoogleGroup({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "OnlyDirectMember": OnlyDirectMember, "Person": Person})

    # Načíst seznam užívání nemovitosti
    def OccupationAllRealtyCollection(self, ID_Login, ID_RealtyCollection, IsActive, IsBorrowable, ID_Application):
        return self._client.service.OccupationAllRealtyCollection({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "IsActive": IsActive, "IsBorrowable": IsBorrowable, "ID_Application": ID_Application})

    # Načíst seznam majetkových vztahů
    def OwnerTypeAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.OwnerTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst osoby podle mailů členů google skupiny
    def PersonAllGoogleGroup(self, ID_Login, ID_GoogleGroup):
        return self._client.service.PersonAllGoogleGroup({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup})

    # Vrátí 
    def PersonAllJournalRover(self, ID_Login, Unit_ID):
        return self._client.service.PersonAllJournalRover({"ID_Login": ID_Login, "Unit_ID": Unit_ID})

    # Načíst počet vydaných karet za jednotlivé roky
    def MemberCardAllSummary(self, ID_Login):
        return self._client.service.MemberCardAllSummary({"ID_Login": ID_Login})

    # Zneplatnit email osoby nebo jednotky
    def ContactUpdateInvalid(self, ID_Login, Mail=None):
        return self._client.service.ContactUpdateInvalid({"ID_Login": ID_Login, "Mail": Mail})

    # Načíst seznam podkladů pro tisk karet
    def MemberCardPrintAll(self, ID_Login, ID, ID_MemberCardPrintState=None):
        return self._client.service.MemberCardPrintAll({"ID_Login": ID_Login, "ID": ID, "ID_MemberCardPrintState": ID_MemberCardPrintState})

    # Stáhnout soubor s podklady pro tisk karet
    def MemberCardPrintDetailDownload(self, ID_Login, ID):
        return self._client.service.MemberCardPrintDetailDownload({"ID_Login": ID_Login, "ID": ID})

    # Založit podklad pro tisk karet
    def MemberCardPrintInsert(self, ID_Login, ID, DateCreate, DateGenerated, Count, ID_MemberCardPrintState=None, MemberCardPrintState=None, Error=None):
        return self._client.service.MemberCardPrintInsert({"ID_Login": ID_Login, "ID": ID, "DateCreate": DateCreate, "DateGenerated": DateGenerated, "Count": Count, "ID_MemberCardPrintState": ID_MemberCardPrintState, "MemberCardPrintState": MemberCardPrintState, "Error": Error})

    # Pozadavek na opetovne vygenerovani souboru s podklady pro tisk
    def MemberCardPrintUpdateGenerate(self, ID_Login, ID, ValidFrom, ValidTo):
        return self._client.service.MemberCardPrintUpdateGenerate({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo})

    # Definitivni smazani docasne oznacenych osob
    def PersonDeleteInactive(self, ID_Login):
        return self._client.service.PersonDeleteInactive({"ID_Login": ID_Login})

    # Načtení informací o osobě
    def PersonDetailHomepage(self, ID_Login, ID):
        return self._client.service.PersonDetailHomepage({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail přihlášku osoby
    def PersonOtherDetailUnitEnroll(self, ID_Login, ID, LoadUnitEnroll):
        return self._client.service.PersonOtherDetailUnitEnroll({"ID_Login": ID_Login, "ID": ID, "LoadUnitEnroll": LoadUnitEnroll})

    # Smazat citlivé údaje
    def PersonOtherUpdateClear(self, ID_Login):
        return self._client.service.PersonOtherUpdateClear({"ID_Login": ID_Login})

    # Upravit odvolání souhlasů z přihlášky osoby
    def PersonOtherUpdateReject(self, ID_Login, ID, ID_Person, ID_DistrictBirth, ID_Assurance, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, DateChangeSocialNetwork, DateChangeMarketing, DateChangeDataStorage, DateChangeAudiovisual, IsRPS, IsEPS, IsEduParticipantExt, OnlyValidate, ID_EventCongress, ID_TempFileHealth, ID_DocumentHealth, IdCardValidTo, IsAdult, IsNonMemberWithGoogleServicesAccess, PromiseChild, PromiseScout, PromiseOfficial, BirthCity=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, Person=None, MaidenName=None, DistrictBirth=None, Assurance=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Note=None, ParentNote=None, IdCardNumber=None, TrailProgress=None):
        return self._client.service.PersonOtherUpdateReject({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_DistrictBirth": ID_DistrictBirth, "ID_Assurance": ID_Assurance, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "DateChangeSocialNetwork": DateChangeSocialNetwork, "DateChangeMarketing": DateChangeMarketing, "DateChangeDataStorage": DateChangeDataStorage, "DateChangeAudiovisual": DateChangeAudiovisual, "IsRPS": IsRPS, "IsEPS": IsEPS, "IsEduParticipantExt": IsEduParticipantExt, "OnlyValidate": OnlyValidate, "ID_EventCongress": ID_EventCongress, "ID_TempFileHealth": ID_TempFileHealth, "ID_DocumentHealth": ID_DocumentHealth, "IdCardValidTo": IdCardValidTo, "IsAdult": IsAdult, "IsNonMemberWithGoogleServicesAccess": IsNonMemberWithGoogleServicesAccess, "PromiseChild": PromiseChild, "PromiseScout": PromiseScout, "PromiseOfficial": PromiseOfficial, "BirthCity": BirthCity, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "Person": Person, "MaidenName": MaidenName, "DistrictBirth": DistrictBirth, "Assurance": Assurance, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Note": Note, "ParentNote": ParentNote, "IdCardNumber": IdCardNumber, "TrailProgress": TrailProgress})

    # Upravit přihlášku osoby
    def PersonOtherUpdateUnitEnroll(self, ID_Login, ID, ID_UnitEnrollTempFile, UnitEnrollExtension=None):
        return self._client.service.PersonOtherUpdateUnitEnroll({"ID_Login": ID_Login, "ID": ID, "ID_UnitEnrollTempFile": ID_UnitEnrollTempFile, "UnitEnrollExtension": UnitEnrollExtension})

    # Potvrdit přihlášku osoby
    def PersonOtherUpdateUnitEnrollCondition(self, ID_Login, ID, ID_Person, ID_DistrictBirth, ID_Assurance, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, DateChangeSocialNetwork, DateChangeMarketing, DateChangeDataStorage, DateChangeAudiovisual, IsRPS, IsEPS, IsEduParticipantExt, OnlyValidate, ID_EventCongress, ID_TempFileHealth, ID_DocumentHealth, IdCardValidTo, IsAdult, IsNonMemberWithGoogleServicesAccess, PromiseChild, PromiseScout, PromiseOfficial, BirthCity=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, Person=None, MaidenName=None, DistrictBirth=None, Assurance=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Note=None, ParentNote=None, IdCardNumber=None, TrailProgress=None):
        return self._client.service.PersonOtherUpdateUnitEnrollCondition({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_DistrictBirth": ID_DistrictBirth, "ID_Assurance": ID_Assurance, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "DateChangeSocialNetwork": DateChangeSocialNetwork, "DateChangeMarketing": DateChangeMarketing, "DateChangeDataStorage": DateChangeDataStorage, "DateChangeAudiovisual": DateChangeAudiovisual, "IsRPS": IsRPS, "IsEPS": IsEPS, "IsEduParticipantExt": IsEduParticipantExt, "OnlyValidate": OnlyValidate, "ID_EventCongress": ID_EventCongress, "ID_TempFileHealth": ID_TempFileHealth, "ID_DocumentHealth": ID_DocumentHealth, "IdCardValidTo": IdCardValidTo, "IsAdult": IsAdult, "IsNonMemberWithGoogleServicesAccess": IsNonMemberWithGoogleServicesAccess, "PromiseChild": PromiseChild, "PromiseScout": PromiseScout, "PromiseOfficial": PromiseOfficial, "BirthCity": BirthCity, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "Person": Person, "MaidenName": MaidenName, "DistrictBirth": DistrictBirth, "Assurance": Assurance, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Note": Note, "ParentNote": ParentNote, "IdCardNumber": IdCardNumber, "TrailProgress": TrailProgress})

    # Stáhnout dekret kvalifikace
    def PersonQualificationLetterDownload(self, ID_Login, ID_Qualification):
        return self._client.service.PersonQualificationLetterDownload({"ID_Login": ID_Login, "ID_Qualification": ID_Qualification})

    # Editace výřezu fotografie osoby
    def PersonUpdatePhotoSize(self, ID_Login, ID, PhotoX, PhotoY, PhotoSize):
        return self._client.service.PersonUpdatePhotoSize({"ID_Login": ID_Login, "ID": ID, "PhotoX": PhotoX, "PhotoY": PhotoY, "PhotoSize": PhotoSize})

    # Načíst seznam členských karet
    def MemberCardAllRequestCount(self, ID_Login):
        return self._client.service.MemberCardAllRequestCount({"ID_Login": ID_Login})

    # Načíst seznam členských karet připravených k vydání
    def MemberCardAllRequest(self, ID_Login, ID_MemberCardPrint):
        return self._client.service.MemberCardAllRequest({"ID_Login": ID_Login, "ID_MemberCardPrint": ID_MemberCardPrint})

    # Načíst platnost členské karty dle jejího čísla
    def MemberCardDetailValid(self, ID_Login, ID_Application, BitOutput, DisplayName=None):
        return self._client.service.MemberCardDetailValid({"ID_Login": ID_Login, "ID_Application": ID_Application, "BitOutput": BitOutput, "DisplayName": DisplayName})

    # Zneplatnit kartu
    def MemberCardUpdateInvalid(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardUpdateInvalid({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Stáhnout dekret kvalifikace
    def QualificationDownload(self, ID_Login, ID):
        return self._client.service.QualificationDownload({"ID_Login": ID_Login, "ID": ID})

    # Založit chybu kvalifikace
    def QualificationMistakeInsert(self, ID_Login, ID, ID_Qualification, ID_PersonCreated, DateCreated, PersonCreated=None, Description=None):
        return self._client.service.QualificationMistakeInsert({"ID_Login": ID_Login, "ID": ID, "ID_Qualification": ID_Qualification, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "PersonCreated": PersonCreated, "Description": Description})

    # Načíst seznam žádostí o kvalifikaci
    def QualificationRequestAll(self, ID_Login, ID_Person, ID, ID_QualificationType, ID_QualificationRequestState=None):
        return self._client.service.QualificationRequestAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID": ID, "ID_QualificationType": ID_QualificationType, "ID_QualificationRequestState": ID_QualificationRequestState})

    # Načíst detail žádosti o kvalifikaci
    def QualificationRequestDetail(self, ID_Login, ID):
        return self._client.service.QualificationRequestDetail({"ID_Login": ID_Login, "ID": ID})

    # Stáhnout sken s dekretem
    def QualificationRequestDetailDownloadLetter(self, ID_Login, ID):
        return self._client.service.QualificationRequestDetailDownloadLetter({"ID_Login": ID_Login, "ID": ID})

    # Založit žádost o kvalifikaci
    def QualificationRequestInsert(self, ID_Login, ID, ID_Person, ID_PersonCreated, ID_QualificationType, ValidFrom, ValidTo, DateCreate, ID_PersonDecision, ID_TempFileScan, ID_Document, Person=None, PersonCreated=None, QualificationType=None, LetterNumber=None, LetterExtension=None, ID_QualificationRequestState=None, QualificationRequestState=None, Course=None, Decision=None, PersonDecision=None):
        return self._client.service.QualificationRequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_PersonCreated": ID_PersonCreated, "ID_QualificationType": ID_QualificationType, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "DateCreate": DateCreate, "ID_PersonDecision": ID_PersonDecision, "ID_TempFileScan": ID_TempFileScan, "ID_Document": ID_Document, "Person": Person, "PersonCreated": PersonCreated, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "LetterExtension": LetterExtension, "ID_QualificationRequestState": ID_QualificationRequestState, "QualificationRequestState": QualificationRequestState, "Course": Course, "Decision": Decision, "PersonDecision": PersonDecision})

    # Načíst seznam stavů žádosti o kvalifikace
    def QualificationRequestStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.QualificationRequestStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit žádost o kvalifikaci
    def QualificationRequestUpdate(self, ID_Login, ID, ID_Person, ID_PersonCreated, ID_QualificationType, ValidFrom, ValidTo, DateCreate, ID_PersonDecision, ID_TempFileScan, ID_Document, Person=None, PersonCreated=None, QualificationType=None, LetterNumber=None, LetterExtension=None, ID_QualificationRequestState=None, QualificationRequestState=None, Course=None, Decision=None, PersonDecision=None):
        return self._client.service.QualificationRequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_PersonCreated": ID_PersonCreated, "ID_QualificationType": ID_QualificationType, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "DateCreate": DateCreate, "ID_PersonDecision": ID_PersonDecision, "ID_TempFileScan": ID_TempFileScan, "ID_Document": ID_Document, "Person": Person, "PersonCreated": PersonCreated, "QualificationType": QualificationType, "LetterNumber": LetterNumber, "LetterExtension": LetterExtension, "ID_QualificationRequestState": ID_QualificationRequestState, "QualificationRequestState": QualificationRequestState, "Course": Course, "Decision": Decision, "PersonDecision": PersonDecision})

    # Načíst detail typu kvalfikace
    def QualificationTypeDetail(self, ID_Login, ID):
        return self._client.service.QualificationTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Rozeslat varování o konci platnosti a možnosti prodloužení
    def QualificationUpdateSendWarning(self, ID_Login):
        return self._client.service.QualificationUpdateSendWarning({"ID_Login": ID_Login})

    # Upravit kvalifikaci
    def QualificationUpload(self, ID_Login, ID, ID_TempFile, LetterExtension=None):
        return self._client.service.QualificationUpload({"ID_Login": ID_Login, "ID": ID, "ID_TempFile": ID_TempFile, "LetterExtension": LetterExtension})

    # Načíst seznam nemovitostí pro soubor nemovitostí
    def RealtyAllRealtyCollection(self, ID_Login, ID_RealtyCollection, IsActive):
        return self._client.service.RealtyAllRealtyCollection({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "IsActive": IsActive})

    # Načíst seznam správců souboru nemovitostí
    def RealtyCollectionAdminAll(self, ID_Login, ID_RealtyCollection, ID, ID_Person):
        return self._client.service.RealtyCollectionAdminAll({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "ID": ID, "ID_Person": ID_Person})

    # Smazat 
    def RealtyCollectionAdminDelete(self, ID_Login, ID):
        return self._client.service.RealtyCollectionAdminDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit 
    def RealtyCollectionAdminInsert(self, ID_Login, ID, ID_RealtyCollection, ID_Person, RealtyCollection=None, Person=None):
        return self._client.service.RealtyCollectionAdminInsert({"ID_Login": ID_Login, "ID": ID, "ID_RealtyCollection": ID_RealtyCollection, "ID_Person": ID_Person, "RealtyCollection": RealtyCollection, "Person": Person})

    # Smazat soubor nemovitostí
    def RealtyCollectionDelete(self, ID_Login, ID, Note=None):
        return self._client.service.RealtyCollectionDelete({"ID_Login": ID_Login, "ID": ID, "Note": Note})

    # Načíst detail souboru nemovitostí
    def RealtyCollectionDetail(self, ID_Login, ID, IsActive):
        return self._client.service.RealtyCollectionDetail({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive})

    # Načíst seznam umístění souboru nemovitostí
    def RealtyCollectionLocationAll(self, ID_Login, ID_RealtyCollection, ID, ID_RealtyLocation=None):
        return self._client.service.RealtyCollectionLocationAll({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "ID": ID, "ID_RealtyLocation": ID_RealtyLocation})

    # Smazat umístění souboru nemovitostí
    def RealtyCollectionLocationDeleteRealtyCollection(self, ID_Login, ID_RealtyCollection):
        return self._client.service.RealtyCollectionLocationDeleteRealtyCollection({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection})

    # Založit umístění souboru nemovitostí
    def RealtyCollectionLocationInsert(self, ID_Login, ID, ID_RealtyCollection, RealtyCollection=None, ID_RealtyLocation=None, RealtyLocation=None):
        return self._client.service.RealtyCollectionLocationInsert({"ID_Login": ID_Login, "ID": ID, "ID_RealtyCollection": ID_RealtyCollection, "RealtyCollection": RealtyCollection, "ID_RealtyLocation": ID_RealtyLocation, "RealtyLocation": RealtyLocation})

    # Načíst seznam způsobů dopravy k souboru nemovitostí
    def RealtyCollectionTransportAll(self, ID_Login, ID_RealtyCollection, ID, ID_RealtyTransport=None):
        return self._client.service.RealtyCollectionTransportAll({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "ID": ID, "ID_RealtyTransport": ID_RealtyTransport})

    # Smazat způsoby dopravy k souboru nemovitostí
    def RealtyCollectionTransportDeleteRealtyCollection(self, ID_Login, ID_RealtyCollection):
        return self._client.service.RealtyCollectionTransportDeleteRealtyCollection({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection})

    # Založit způsoby dopravy k souboru nemovitostí
    def RealtyCollectionTransportInsert(self, ID_Login, ID, ID_RealtyCollection, RealtyCollection=None, ID_RealtyTransport=None, RealtyTransport=None):
        return self._client.service.RealtyCollectionTransportInsert({"ID_Login": ID_Login, "ID": ID, "ID_RealtyCollection": ID_RealtyCollection, "RealtyCollection": RealtyCollection, "ID_RealtyTransport": ID_RealtyTransport, "RealtyTransport": RealtyTransport})

    # Upravit soubor nemovitostí
    def RealtyCollectionUpdate(self, ID_TempFilePhoto, ID_Login, ID, ID_Unit, ID_User, IsActive, GpsLatitude, GpsLongitude, HasAddress, ID_Region, ID_Document, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, Unit=None, UnitRegistrationNumber=None, Owner=None, DisplayName=None, Description=None, Web=None, Street=None, City=None, Postcode=None, District=None, TransportationMethods=None, TransportationMethodsText=None, TransportDescription=None, Locations=None, LocationsText=None, PointsOfInterest=None, Note=None, Region=None, Storage=None):
        return self._client.service.RealtyCollectionUpdate({"ID_TempFilePhoto": ID_TempFilePhoto, "ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_User": ID_User, "IsActive": IsActive, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "HasAddress": HasAddress, "ID_Region": ID_Region, "ID_Document": ID_Document, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber, "Owner": Owner, "DisplayName": DisplayName, "Description": Description, "Web": Web, "Street": Street, "City": City, "Postcode": Postcode, "District": District, "TransportationMethods": TransportationMethods, "TransportationMethodsText": TransportationMethodsText, "TransportDescription": TransportDescription, "Locations": Locations, "LocationsText": LocationsText, "PointsOfInterest": PointsOfInterest, "Note": Note, "Region": Region, "Storage": Storage})

    # Smazat nemovitost
    def RealtyDelete(self, ID_Login, ID, Note=None):
        return self._client.service.RealtyDelete({"ID_Login": ID_Login, "ID": ID, "Note": Note})

    # Načíst seznam dokumentů
    def RealtyDocumentAllOccupation(self, ID_Login, ID, ID_User, ID_Occupation, Location=None):
        return self._client.service.RealtyDocumentAllOccupation({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Occupation": ID_Occupation, "Location": Location})

    # Načíst seznam dokumentů
    def RealtyDocumentAllRealty(self, ID_Login, ID_Realty, ID, ID_User, Location=None):
        return self._client.service.RealtyDocumentAllRealty({"ID_Login": ID_Login, "ID_Realty": ID_Realty, "ID": ID, "ID_User": ID_User, "Location": Location})

    # Založit dokument
    def RealtyDocumentInsert(self, ID_Login, ID, ID_User, Saved, IsPublic, Size, ID_Realty, ID_Occupation, ID_TempFileDocument, ID_Document, DisplayName=None, Location=None, Origin=None, DownloadName=None, Note=None, Hash=None, Realty=None, Extension=None):
        return self._client.service.RealtyDocumentInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "Saved": Saved, "IsPublic": IsPublic, "Size": Size, "ID_Realty": ID_Realty, "ID_Occupation": ID_Occupation, "ID_TempFileDocument": ID_TempFileDocument, "ID_Document": ID_Document, "DisplayName": DisplayName, "Location": Location, "Origin": Origin, "DownloadName": DownloadName, "Note": Note, "Hash": Hash, "Realty": Realty, "Extension": Extension})

    # Úprava vazeb dokumentu na ostatní tabulky
    def RealtyDocumentUpdateBinding(self, ID_Login, ID, ID_User, Saved, IsPublic, Size, ID_Realty, ID_Occupation, ID_TempFileDocument, ID_Document, DisplayName=None, Location=None, Origin=None, DownloadName=None, Note=None, Hash=None, Realty=None, Extension=None):
        return self._client.service.RealtyDocumentUpdateBinding({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "Saved": Saved, "IsPublic": IsPublic, "Size": Size, "ID_Realty": ID_Realty, "ID_Occupation": ID_Occupation, "ID_TempFileDocument": ID_TempFileDocument, "ID_Document": ID_Document, "DisplayName": DisplayName, "Location": Location, "Origin": Origin, "DownloadName": DownloadName, "Note": Note, "Hash": Hash, "Realty": Realty, "Extension": Extension})

    # Založit nemovitost do souboru nemovitostí
    def RealtyInsertRealtyCollection(self, ID_Login, ID_RealtyCollection, IsPower, ID_TempFilePhoto, LVNumber, Acreage, GpsLatitude, GpsLongitude, RealtyGpsLatitude, RealtyGpsLongitude, DisplayName=None, ID_OwnerType=None, OwnerTypeNote=None, Description=None, Note=None, ID_RegisterType=None, RegisterCode=None, FotogalleryUrl=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None):
        return self._client.service.RealtyInsertRealtyCollection({"ID_Login": ID_Login, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ID_TempFilePhoto": ID_TempFilePhoto, "LVNumber": LVNumber, "Acreage": Acreage, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "DisplayName": DisplayName, "ID_OwnerType": ID_OwnerType, "OwnerTypeNote": OwnerTypeNote, "Description": Description, "Note": Note, "ID_RegisterType": ID_RegisterType, "RegisterCode": RegisterCode, "FotogalleryUrl": FotogalleryUrl, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType})

    # Načíst seznam umístění
    def RealtyLocationAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.RealtyLocationAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů dopravy
    def RealtyTransportAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.RealtyTransportAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail typu nemovitosti
    def RealtyTypeDetail(self, ID_Login, ID):
        return self._client.service.RealtyTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Nastavit přiřazení nemovitosti do skautské energie
    def RealtyUpdateIsPower(self, ID_Login, ID, ID_RealtyType, GpsLatitude, GpsLongitude, ID_RealtyCollection, IsPower, ValidTo, IsActive, ID_TempFilePhoto, IsAddressAuthenticated, ID_Document, LVNumber, Acreage, RealtyGpsLatitude, RealtyGpsLongitude, CoordinateX, CoordinateY, DisplayName=None, RealtyType=None, Street=None, City=None, Postcode=None, Description=None, Note=None, RealtyCollection=None, ID_OwnerType=None, OwnerType=None, OwnerTypeNote=None, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, District=None, Storage=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None, Unit=None, UnitRegistrationNumber=None):
        return self._client.service.RealtyUpdateIsPower({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ValidTo": ValidTo, "IsActive": IsActive, "ID_TempFilePhoto": ID_TempFilePhoto, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_Document": ID_Document, "LVNumber": LVNumber, "Acreage": Acreage, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "CoordinateX": CoordinateX, "CoordinateY": CoordinateY, "DisplayName": DisplayName, "RealtyType": RealtyType, "Street": Street, "City": City, "Postcode": Postcode, "Description": Description, "Note": Note, "RealtyCollection": RealtyCollection, "ID_OwnerType": ID_OwnerType, "OwnerType": OwnerType, "OwnerTypeNote": OwnerTypeNote, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "District": District, "Storage": Storage, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber})

    # Upravit nemovitost
    def RealtyUpdateRemoveFromCollection(self, ID_Login, ID, ID_RealtyType, GpsLatitude, GpsLongitude, ID_RealtyCollection, IsPower, ValidTo, IsActive, ID_TempFilePhoto, IsAddressAuthenticated, ID_Document, LVNumber, Acreage, RealtyGpsLatitude, RealtyGpsLongitude, CoordinateX, CoordinateY, DisplayName=None, RealtyType=None, Street=None, City=None, Postcode=None, Description=None, Note=None, RealtyCollection=None, ID_OwnerType=None, OwnerType=None, OwnerTypeNote=None, PhotoExtension=None, PhotoFileContent=None, FotogalleryUrl=None, District=None, Storage=None, ParcelNumber=None, RegisterCity=None, CadastralArea=None, ParcelType=None, LandType=None, Unit=None, UnitRegistrationNumber=None):
        return self._client.service.RealtyUpdateRemoveFromCollection({"ID_Login": ID_Login, "ID": ID, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_RealtyCollection": ID_RealtyCollection, "IsPower": IsPower, "ValidTo": ValidTo, "IsActive": IsActive, "ID_TempFilePhoto": ID_TempFilePhoto, "IsAddressAuthenticated": IsAddressAuthenticated, "ID_Document": ID_Document, "LVNumber": LVNumber, "Acreage": Acreage, "RealtyGpsLatitude": RealtyGpsLatitude, "RealtyGpsLongitude": RealtyGpsLongitude, "CoordinateX": CoordinateX, "CoordinateY": CoordinateY, "DisplayName": DisplayName, "RealtyType": RealtyType, "Street": Street, "City": City, "Postcode": Postcode, "Description": Description, "Note": Note, "RealtyCollection": RealtyCollection, "ID_OwnerType": ID_OwnerType, "OwnerType": OwnerType, "OwnerTypeNote": OwnerTypeNote, "PhotoExtension": PhotoExtension, "PhotoFileContent": PhotoFileContent, "FotogalleryUrl": FotogalleryUrl, "District": District, "Storage": Storage, "ParcelNumber": ParcelNumber, "RegisterCity": RegisterCity, "CadastralArea": CadastralArea, "ParcelType": ParcelType, "LandType": LandType, "Unit": Unit, "UnitRegistrationNumber": UnitRegistrationNumber})

    # Načíst seznam typů záznamu v katastru
    def RegisterTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.RegisterTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit komentář registrační vady osoby
    def PersonMistakeReportUpdatePerson(self, ID_Login, ID, ID_Person, ID_Unit, ID_UnitRegistration, ID_Mistake, Person=None, UnitRegistrationNumber=None, Unit=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.PersonMistakeReportUpdatePerson({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_UnitRegistration": ID_UnitRegistration, "ID_Mistake": ID_Mistake, "Person": Person, "UnitRegistrationNumber": UnitRegistrationNumber, "Unit": Unit, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Upravit komentář registrační vady jednotky
    def UnitMistakeReportUpdateUnit(self, ID_Login, ID, ID_Unit, ID_Mistake, Unit=None, RegistrationNumber=None, Mistake=None, DisplayName=None, ParentComment=None):
        return self._client.service.UnitMistakeReportUpdateUnit({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Mistake": ID_Mistake, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Mistake": Mistake, "DisplayName": DisplayName, "ParentComment": ParentComment})

    # Načtení statistiky dle věku registrací podřízených jednotek (datatable)
    def UnitRegistrationAllSubStatsAgeTable(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsAgeTable({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle typu jednotky registrací podřízených jednotek (datatable)
    def UnitRegistrationAllSubStatsTypeTable(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsTypeTable({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle typu oddílu registrací podřízených oddílů (datatable)
    def UnitRegistrationAllSubStatsTroopTable(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsTroopTable({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle typu oddílu registrací podřízených oddílů
    def UnitRegistrationAllSubStatsTroop(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsTroop({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle typu jednotky registrací podřízených jednotek
    def UnitRegistrationAllSubStatsType(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsType({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle věku registrací podřízených jednotek
    def UnitRegistrationAllSubStatsAge(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllSubStatsAge({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle věku registrací zadané jednotky (datatable)
    def UnitRegistrationAllStatsAgeTable(self, ID_Login, ID_Unit, IsExpanded, LastNYears):
        return self._client.service.UnitRegistrationAllStatsAgeTable({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears})

    # Načtení statistiky dle věku registrací zadané jednotky
    def UnitRegistrationAllStatsAge(self, ID_Login, ID_Unit, IsExpanded, LastNYears, PrepareInvertedDatatable):
        return self._client.service.UnitRegistrationAllStatsAge({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsExpanded": IsExpanded, "LastNYears": LastNYears, "PrepareInvertedDatatable": PrepareInvertedDatatable})

    # Načtení statistiky dle kategorie registrací zadané jednotky (datatable)
    def UnitRegistrationAllStatsCategoryTable(self, ID_Login, ID_Unit, LastNYears, IsExpanded):
        return self._client.service.UnitRegistrationAllStatsCategoryTable({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "LastNYears": LastNYears, "IsExpanded": IsExpanded})

    # Načtení statistiky dle kategorie registrací zadané jednotky
    def UnitRegistrationAllStatsCategory(self, ID_Login, ID_Unit, LastNYears, IsExpanded):
        return self._client.service.UnitRegistrationAllStatsCategory({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "LastNYears": LastNYears, "IsExpanded": IsExpanded})

    # Načíst statistiku registrací jednotky
    def UnitRegistrationAllStats(self, ID_Login, ID_Unit):
        return self._client.service.UnitRegistrationAllStats({"ID_Login": ID_Login, "ID_Unit": ID_Unit})

    # Upravit pokyny k registraci
    def UnitRegistrationUpdateInstructions(self, ID_Login, ID, ID_Unit, Year, DateChecked, DateConfirmed, IsDelivered, IsAccepted, ShowServices, ID_UnitRegistrationParent, ParentIsDelivered, ParentIsAccepted, ParentHasCreated, ParentShowServices, DisplayName=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Instructions=None, UnitRegistrationParent=None, InstructionsParent=None):
        return self._client.service.UnitRegistrationUpdateInstructions({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Year": Year, "DateChecked": DateChecked, "DateConfirmed": DateConfirmed, "IsDelivered": IsDelivered, "IsAccepted": IsAccepted, "ShowServices": ShowServices, "ID_UnitRegistrationParent": ID_UnitRegistrationParent, "ParentIsDelivered": ParentIsDelivered, "ParentIsAccepted": ParentIsAccepted, "ParentHasCreated": ParentHasCreated, "ParentShowServices": ParentShowServices, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Instructions": Instructions, "UnitRegistrationParent": UnitRegistrationParent, "InstructionsParent": InstructionsParent})

    # Přepočítání statistiky členů a jednotek v registraci
    def UnitRegistrationRebuildMembers(self, ID_Login, ID, Year):
        return self._client.service.UnitRegistrationRebuildMembers({"ID_Login": ID_Login, "ID": ID, "Year": Year})

    # Přehled registračních komentářů podřízených jednotek
    def UnitRegistrationReportChild(self, ID_Login, ID, ShowChildUnit, UnitType=None, RegistrationNumber=None):
        return self._client.service.UnitRegistrationReportChild({"ID_Login": ID_Login, "ID": ID, "ShowChildUnit": ShowChildUnit, "UnitType": UnitType, "RegistrationNumber": RegistrationNumber})

    # Načtení seznamu roku registraci ustredi
    def UnitRegistrationAllYearUstredi(self, ID_Login, ExportFilter):
        return self._client.service.UnitRegistrationAllYearUstredi({"ID_Login": ID_Login, "ExportFilter": ExportFilter})

    # Načíst detail požadavku pro průvodní dopis
    def RegistryDetailExport(self, ID_Login, ID):
        return self._client.service.RegistryDetailExport({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam účtů tábora
    def AccountAllEventCamp(self, ID_Login, ID_Application, ID_EventCamp):
        return self._client.service.AccountAllEventCamp({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_EventCamp": ID_EventCamp})

    # Načíst detail zobrazení osoby v adresáři
    def CatalogDisplayDetail(self, ID_Login, ID_Person):
        return self._client.service.CatalogDisplayDetail({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Upravit zobrazení osoby v adresáři
    def CatalogDisplayUpdate(self, ID_Login, ID, ID_Person, Birthday, YearFrom, Adress, PostalAdress, School, Function, Qualification, EducationSeminary, Offer, Education, Membership, Person=None):
        return self._client.service.CatalogDisplayUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "YearFrom": YearFrom, "Adress": Adress, "PostalAdress": PostalAdress, "School": School, "Function": Function, "Qualification": Qualification, "EducationSeminary": EducationSeminary, "Offer": Offer, "Education": Education, "Membership": Membership, "Person": Person})

    # Načíst detail limitu pro vyhledávání osob v adresáři
    def CatalogLimitDetail(self, ID_Login, ID_Person):
        return self._client.service.CatalogLimitDetail({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Upravit limit pro vyhledávání osob v adresáři
    def CatalogLimitUpdate(self, ID_Login, ID_Person, OnlyWeek):
        return self._client.service.CatalogLimitUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "OnlyWeek": OnlyWeek})

    # Načíst seznam fakturačních jednotek
    def InvoiceGroupAll(self, ID_Login, ID, ID_TelephonyUnit, DisplayName=None):
        return self._client.service.InvoiceGroupAll({"ID_Login": ID_Login, "ID": ID, "ID_TelephonyUnit": ID_TelephonyUnit, "DisplayName": DisplayName})

    # Načíst výchozí fakturační jednotku
    def InvoiceGroupDetailDefault(self, ID_Login):
        return self._client.service.InvoiceGroupDetailDefault({"ID_Login": ID_Login})

    # Zrušit objednání ztracené karty
    def MemberCardUpdateCancelRerequest(self, ID_Login, ID, ID_Person, Birthday, Year, DateCreate, Price, IsAuthorized, IsPaid, ValidFrom, ValidTo, ID_PersonSchool, ID_PersonRegistration, ID_DocumentPersonSchool, ID_DocumentMediumPhoto, ID_MemberCardState=None, MemberCardState=None, DisplayName=None, Person=None, ID_MemberCardType=None, MemberCardType=None, PersonSchool=None, PersonSchoolCity=None, UnitStredisko=None, LeaderContact=None, StorageMediumPhoto=None):
        return self._client.service.MemberCardUpdateCancelRerequest({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "Birthday": Birthday, "Year": Year, "DateCreate": DateCreate, "Price": Price, "IsAuthorized": IsAuthorized, "IsPaid": IsPaid, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_PersonSchool": ID_PersonSchool, "ID_PersonRegistration": ID_PersonRegistration, "ID_DocumentPersonSchool": ID_DocumentPersonSchool, "ID_DocumentMediumPhoto": ID_DocumentMediumPhoto, "ID_MemberCardState": ID_MemberCardState, "MemberCardState": MemberCardState, "DisplayName": DisplayName, "Person": Person, "ID_MemberCardType": ID_MemberCardType, "MemberCardType": MemberCardType, "PersonSchool": PersonSchool, "PersonSchoolCity": PersonSchoolCity, "UnitStredisko": UnitStredisko, "LeaderContact": LeaderContact, "StorageMediumPhoto": StorageMediumPhoto})

    # Detail osoby jako účastníka sněmu
    def PersonDetailEventCongressParticipant(self, ID_Login, ID_EventCongress, ID_Participant):
        return self._client.service.PersonDetailEventCongressParticipant({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Participant": ID_Participant})

    # Odeslat email o vyzvednutí kódu pro vstup do STS
    def PersonOtherTelephonyEnroll(self, ID_Login, ID_Person):
        return self._client.service.PersonOtherTelephonyEnroll({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načíst seznam typů účastí
    def ParticipationTypeAll(self, ID_Application, ID_Login, ID=None, DisplayName=None):
        return self._client.service.ParticipationTypeAll({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Editace účastníka sněmu
    def PersonUpdateEventCongressParticipant(self, ID_Login, ID_Participant, IdCardValidTo, IsAddressAuthenticated, Email=None, Phone=None, Street=None, City=None, Postcode=None, State=None, IdCardNumber=None):
        return self._client.service.PersonUpdateEventCongressParticipant({"ID_Login": ID_Login, "ID_Participant": ID_Participant, "IdCardValidTo": IdCardValidTo, "IsAddressAuthenticated": IsAddressAuthenticated, "Email": Email, "Phone": Phone, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "IdCardNumber": IdCardNumber})

    # Načtení míst působení
    def UnitLocations(self, ID_Login, ID_Application, Top, SearchQuery=None):
        return self._client.service.UnitLocations({"ID_Login": ID_Login, "ID_Application": ID_Application, "Top": Top, "SearchQuery": SearchQuery})

    # Načíst seznam dokumentů užití nemovitosti
    def OccupationPhotoAll(self, ID_Login, ID_Occupation, ID, ID_Document):
        return self._client.service.OccupationPhotoAll({"ID_Login": ID_Login, "ID_Occupation": ID_Occupation, "ID": ID, "ID_Document": ID_Document})

    # Smazat dokument užití nemovitosti
    def OccupationPhotoDelete(self, ID_Login, ID):
        return self._client.service.OccupationPhotoDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit dokument užití nemovitosti
    def OccupationPhotoInsert(self, ID_Login, ID, ID_Occupation, ID_Document, ID_TempFile, Description=None):
        return self._client.service.OccupationPhotoInsert({"ID_Login": ID_Login, "ID": ID, "ID_Occupation": ID_Occupation, "ID_Document": ID_Document, "ID_TempFile": ID_TempFile, "Description": Description})

    # Načíst detail půjčitelné nemovitosti pro kalendář
    def OccupationRentDetailCalendar(self, ID_Login, ID_Application, ID):
        return self._client.service.OccupationRentDetailCalendar({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst seznam půjčitelných nemovitostí pro kalendář
    def OccupationRentAllCalendarAll(self, ID_Login, ID_Application, IsInstant):
        return self._client.service.OccupationRentAllCalendarAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "IsInstant": IsInstant})

    # Načíst seznam půjčitelných jednotek pro API
    def OccupationRentAllPublicApi(self, ID_Login, ID_Application):
        return self._client.service.OccupationRentAllPublicApi({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Načíst seznam půjčitelných jednotek s detailnímí informacemi pro API
    def OccupationRentAllPublicApiDetail(self, ID_Login, ID_Application, ID_RealtyType, Capacity, ID_Items=None, ID_OccupationEquipment=None, ID_RealtyLocations=None):
        return self._client.service.OccupationRentAllPublicApiDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_RealtyType": ID_RealtyType, "Capacity": Capacity, "ID_Items": ID_Items, "ID_OccupationEquipment": ID_OccupationEquipment, "ID_RealtyLocations": ID_RealtyLocations})

    # Načíst detail půjčitelné jednotky pro API
    def OccupationRentDetailPublicApi(self, ID_Login, ID_Application, ID):
        return self._client.service.OccupationRentDetailPublicApi({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst seznam cen za pronájem
    def OccupationRentPriceAllOccupationRent(self, ID_Login, ID_Application, ID_OccupationRent):
        return self._client.service.OccupationRentPriceAllOccupationRent({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_OccupationRent": ID_OccupationRent})

    # Změnit data kalendářů půjčitelné jednotky
    def OccupationRentUpdateCalendarFile(self, ID_Login, ID_Application, ID, ID_TempFile, ID_TempFileAdmin):
        return self._client.service.OccupationRentUpdateCalendarFile({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_TempFile": ID_TempFile, "ID_TempFileAdmin": ID_TempFileAdmin})

    # Nastavit datum generování kalendáře
    def OccupationRentUpdateRegenerateCalendar(self, ID_Login, ID_Application, ID, Reset):
        return self._client.service.OccupationRentUpdateRegenerateCalendar({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "Reset": Reset})

    # Načíst seznam osob týmu vzdělávací akce
    def PersonAllEventEducationTeam(self, ID_Login, ID_EventEducation, DisplayName=None):
        return self._client.service.PersonAllEventEducationTeam({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "DisplayName": DisplayName})

    # Založit změnu u osoby zákonným zástupcem
    def PersonChangeInsertPersonParent(self, ID_Login, ID_Person):
        return self._client.service.PersonChangeInsertPersonParent({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načtení informací o dětech osoby
    def PersonDetailChildren(self, ID_Login, ID):
        return self._client.service.PersonDetailChildren({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam potomků osoby
    def PersonParentAllPersonChildren(self, ID_Login, ID_Application, ID_Person, ID, ID_PersonParent, ID_ParentType=None):
        return self._client.service.PersonParentAllPersonChildren({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Person": ID_Person, "ID": ID, "ID_PersonParent": ID_PersonParent, "ID_ParentType": ID_ParentType})

    # Načíst seznam žádostí ke zpracování o kvalifikaci osoby
    def QualificationRequestAllPerson(self, ID_Login, ID_Person):
        return self._client.service.QualificationRequestAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načtení zjednodušených informací o jednotce
    def UnitDetailSimple(self, ID_Login, ID_Application, ID):
        return self._client.service.UnitDetailSimple({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst seznam náborových kategorií
    def AdvertisingCategoryAllOccupation(self, ID_Login, ID_Application, ID_Occupation, ID_MeetingDate, ID_Sex=None):
        return self._client.service.AdvertisingCategoryAllOccupation({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Occupation": ID_Occupation, "ID_MeetingDate": ID_MeetingDate, "ID_Sex": ID_Sex})

    # Načíst seznam položek kontroly
    def AuditRegisterItemAll(self, ID_Login, ID_UnitAuditRegister, ID, ID_Person, ID_AuditRegisterItemType=None):
        return self._client.service.AuditRegisterItemAll({"ID_Login": ID_Login, "ID_UnitAuditRegister": ID_UnitAuditRegister, "ID": ID, "ID_Person": ID_Person, "ID_AuditRegisterItemType": ID_AuditRegisterItemType})

    # Smazat položku kontroly
    def AuditRegisterItemDelete(self, ID_Login, ID, ID_UnitAuditRegister, Done, ID_Person, IsDone, ID_AuditRegisterItemType=None, AuditRegisterItemType=None, AuditRegisterItemTypeHelp=None, AuditRegisterItemTypeCustom=None, Person=None, Comment=None, HelpCustom=None, DoneText=None):
        return self._client.service.AuditRegisterItemDelete({"ID_Login": ID_Login, "ID": ID, "ID_UnitAuditRegister": ID_UnitAuditRegister, "Done": Done, "ID_Person": ID_Person, "IsDone": IsDone, "ID_AuditRegisterItemType": ID_AuditRegisterItemType, "AuditRegisterItemType": AuditRegisterItemType, "AuditRegisterItemTypeHelp": AuditRegisterItemTypeHelp, "AuditRegisterItemTypeCustom": AuditRegisterItemTypeCustom, "Person": Person, "Comment": Comment, "HelpCustom": HelpCustom, "DoneText": DoneText})

    # Založit položku kontroly
    def AuditRegisterItemInsert(self, ID_Login, ID, ID_UnitAuditRegister, Done, ID_Person, IsDone, ID_AuditRegisterItemType=None, AuditRegisterItemType=None, AuditRegisterItemTypeHelp=None, AuditRegisterItemTypeCustom=None, Person=None, Comment=None, HelpCustom=None, DoneText=None):
        return self._client.service.AuditRegisterItemInsert({"ID_Login": ID_Login, "ID": ID, "ID_UnitAuditRegister": ID_UnitAuditRegister, "Done": Done, "ID_Person": ID_Person, "IsDone": IsDone, "ID_AuditRegisterItemType": ID_AuditRegisterItemType, "AuditRegisterItemType": AuditRegisterItemType, "AuditRegisterItemTypeHelp": AuditRegisterItemTypeHelp, "AuditRegisterItemTypeCustom": AuditRegisterItemTypeCustom, "Person": Person, "Comment": Comment, "HelpCustom": HelpCustom, "DoneText": DoneText})

    # Upravit položku kontroly
    def AuditRegisterItemUpdate(self, ID_Login, ID, ID_UnitAuditRegister, Done, ID_Person, IsDone, ID_AuditRegisterItemType=None, AuditRegisterItemType=None, AuditRegisterItemTypeHelp=None, AuditRegisterItemTypeCustom=None, Person=None, Comment=None, HelpCustom=None, DoneText=None):
        return self._client.service.AuditRegisterItemUpdate({"ID_Login": ID_Login, "ID": ID, "ID_UnitAuditRegister": ID_UnitAuditRegister, "Done": Done, "ID_Person": ID_Person, "IsDone": IsDone, "ID_AuditRegisterItemType": ID_AuditRegisterItemType, "AuditRegisterItemType": AuditRegisterItemType, "AuditRegisterItemTypeHelp": AuditRegisterItemTypeHelp, "AuditRegisterItemTypeCustom": AuditRegisterItemTypeCustom, "Person": Person, "Comment": Comment, "HelpCustom": HelpCustom, "DoneText": DoneText})

    # Načíst seznam státních občanství
    def CitizenshipAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.CitizenshipAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů změny kontaktu
    def ContactRequestTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.ContactRequestTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit semináře účastníkům vzdělavací akci
    def EducatationSeminaryInsertEventEducation(self, ID_Login, ID_EventEducation):
        return self._client.service.EducatationSeminaryInsertEventEducation({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation})

    # Načíst detail souhlasu se zápisem do spolkového rejstříku
    def FunctionDetailAgreementDownload(self, ID_Login, ID):
        return self._client.service.FunctionDetailAgreementDownload({"ID_Login": ID_Login, "ID": ID})

    # Načtení informací o osobě pro souhlas se zápisem do spolkového rejstříku
    def FunctionDetailAgreementTemplate(self, ID_Login, ID, ID_FunctionType, CityText=None):
        return self._client.service.FunctionDetailAgreementTemplate({"ID_Login": ID_Login, "ID": ID, "ID_FunctionType": ID_FunctionType, "CityText": CityText})

    # Načíst seznam typů funkcí pro Google synchronizaci
    def FunctionTypeAllGoogleGroupSync(self, ID_Login, ID_GoogleGroup, IsDirect):
        return self._client.service.FunctionTypeAllGoogleGroupSync({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup, "IsDirect": IsDirect})

    # Potvrzení souhlasu se zápisem do spolkového rejstříku
    def FunctionUpdateAgreementConfirm(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionUpdateAgreementConfirm({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Nahrát souhlas se zápisem do spolkového rejstříku
    def FunctionUpdateAgreement(self, ID_Login, ID, ValidFrom, ValidTo, ID_Person, ID_Unit, ID_FunctionType, ID_Role, IsDeleteRole, AgreementConfirmed, ID_TempFile, AgreementNeeded, AgreementCanUpload, AgreementCanConfirm, AgreementCanView, ID_FunctionReason=None, Specification=None, AgreementExtension=None, Code=None, Number=None):
        return self._client.service.FunctionUpdateAgreement({"ID_Login": ID_Login, "ID": ID, "ValidFrom": ValidFrom, "ValidTo": ValidTo, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_FunctionType": ID_FunctionType, "ID_Role": ID_Role, "IsDeleteRole": IsDeleteRole, "AgreementConfirmed": AgreementConfirmed, "ID_TempFile": ID_TempFile, "AgreementNeeded": AgreementNeeded, "AgreementCanUpload": AgreementCanUpload, "AgreementCanConfirm": AgreementCanConfirm, "AgreementCanView": AgreementCanView, "ID_FunctionReason": ID_FunctionReason, "Specification": Specification, "AgreementExtension": AgreementExtension, "Code": Code, "Number": Number})

    # Načíst seznam fakturovaných časopisů
    def MemberCardAllMemberCardInvoiceSummaryVat(self, ID_Login, ID_MemberCardInvoice):
        return self._client.service.MemberCardAllMemberCardInvoiceSummaryVat({"ID_Login": ID_Login, "ID_MemberCardInvoice": ID_MemberCardInvoice})

    # Načíst faktury za členské karty jednoty
    def MemberCardInvoiceAllUnit(self, ID_Login, ID_Unit, ID, DateGeneratingFrom, DateGeneratingTo, DisplayName=None, ID_MemberCardInvoiceState=None):
        return self._client.service.MemberCardInvoiceAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "DisplayName": DisplayName, "ID_MemberCardInvoiceState": ID_MemberCardInvoiceState})

    # Načíst seznam faktur za členské karty v xml
    def MemberCardInvoiceAllXml(self, ID_Login, ID_Unit, ID, ID_MemberCardInvoiceGenerate, DateGeneratingFrom, DateGeneratingTo, DisplayName=None, ID_MemberCardInvoiceState=None):
        return self._client.service.MemberCardInvoiceAllXml({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID": ID, "ID_MemberCardInvoiceGenerate": ID_MemberCardInvoiceGenerate, "DateGeneratingFrom": DateGeneratingFrom, "DateGeneratingTo": DateGeneratingTo, "DisplayName": DisplayName, "ID_MemberCardInvoiceState": ID_MemberCardInvoiceState})

    # Načíst detail faktury za členské karty
    def MemberCardInvoiceDetailDownloadPdf(self, ID_Login, ID):
        return self._client.service.MemberCardInvoiceDetailDownloadPdf({"ID_Login": ID_Login, "ID": ID})

    # Upravit fakturu za členské karty
    def MemberCardInvoiceUpdate(self, ID_Login, ID, ID_Unit, Sequence, Maturity, DateGenerating, TotalPrice, TotalPriceWithVat, Price, PriceBase, PriceFirst, PriceSecond, VatBase, VatFirst, VatSecond, ID_MemberCardInvoiceGenerate, ID_InvoiceGroup, DateTaxableSupply, Unit=None, RegistrationNumber=None, Street=None, City=None, Postcode=None, State=None, StateCode=None, IC=None, DIC=None, DisplayName=None, ID_MemberCardInvoiceState=None, MemberCardInvoiceState=None, InvoiceGroupContractorIC=None, InvoiceGroupContractorDIC=None, InvoiceGroupContractorPhone=None, InvoiceGroupContractorEmail=None, InvoiceGroupWeb=None, InvoiceGroupFileReference=None, InvoiceGroupBankAccount=None, InvoiceGroupBankCode=None, InvoiceGroupBank=None, PaymentType=None, QRCodeString=None, InvoiceGroupContractor=None, InvoiceGroupContractorAddress=None, InvoiceBankAccount=None):
        return self._client.service.MemberCardInvoiceUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Sequence": Sequence, "Maturity": Maturity, "DateGenerating": DateGenerating, "TotalPrice": TotalPrice, "TotalPriceWithVat": TotalPriceWithVat, "Price": Price, "PriceBase": PriceBase, "PriceFirst": PriceFirst, "PriceSecond": PriceSecond, "VatBase": VatBase, "VatFirst": VatFirst, "VatSecond": VatSecond, "ID_MemberCardInvoiceGenerate": ID_MemberCardInvoiceGenerate, "ID_InvoiceGroup": ID_InvoiceGroup, "DateTaxableSupply": DateTaxableSupply, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "StateCode": StateCode, "IC": IC, "DIC": DIC, "DisplayName": DisplayName, "ID_MemberCardInvoiceState": ID_MemberCardInvoiceState, "MemberCardInvoiceState": MemberCardInvoiceState, "InvoiceGroupContractorIC": InvoiceGroupContractorIC, "InvoiceGroupContractorDIC": InvoiceGroupContractorDIC, "InvoiceGroupContractorPhone": InvoiceGroupContractorPhone, "InvoiceGroupContractorEmail": InvoiceGroupContractorEmail, "InvoiceGroupWeb": InvoiceGroupWeb, "InvoiceGroupFileReference": InvoiceGroupFileReference, "InvoiceGroupBankAccount": InvoiceGroupBankAccount, "InvoiceGroupBankCode": InvoiceGroupBankCode, "InvoiceGroupBank": InvoiceGroupBank, "PaymentType": PaymentType, "QRCodeString": QRCodeString, "InvoiceGroupContractor": InvoiceGroupContractor, "InvoiceGroupContractorAddress": InvoiceGroupContractorAddress, "InvoiceBankAccount": InvoiceBankAccount})

    # Odeslat fakturu za členské karty
    def MemberCardInvoiceUpdateSend(self, ID_Login, ID, ID_Unit, Sequence, Maturity, DateGenerating, TotalPrice, TotalPriceWithVat, Price, PriceBase, PriceFirst, PriceSecond, VatBase, VatFirst, VatSecond, ID_MemberCardInvoiceGenerate, ID_InvoiceGroup, DateTaxableSupply, Unit=None, RegistrationNumber=None, Street=None, City=None, Postcode=None, State=None, StateCode=None, IC=None, DIC=None, DisplayName=None, ID_MemberCardInvoiceState=None, MemberCardInvoiceState=None, InvoiceGroupContractorIC=None, InvoiceGroupContractorDIC=None, InvoiceGroupContractorPhone=None, InvoiceGroupContractorEmail=None, InvoiceGroupWeb=None, InvoiceGroupFileReference=None, InvoiceGroupBankAccount=None, InvoiceGroupBankCode=None, InvoiceGroupBank=None, PaymentType=None, QRCodeString=None, InvoiceGroupContractor=None, InvoiceGroupContractorAddress=None, InvoiceBankAccount=None):
        return self._client.service.MemberCardInvoiceUpdateSend({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Sequence": Sequence, "Maturity": Maturity, "DateGenerating": DateGenerating, "TotalPrice": TotalPrice, "TotalPriceWithVat": TotalPriceWithVat, "Price": Price, "PriceBase": PriceBase, "PriceFirst": PriceFirst, "PriceSecond": PriceSecond, "VatBase": VatBase, "VatFirst": VatFirst, "VatSecond": VatSecond, "ID_MemberCardInvoiceGenerate": ID_MemberCardInvoiceGenerate, "ID_InvoiceGroup": ID_InvoiceGroup, "DateTaxableSupply": DateTaxableSupply, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "StateCode": StateCode, "IC": IC, "DIC": DIC, "DisplayName": DisplayName, "ID_MemberCardInvoiceState": ID_MemberCardInvoiceState, "MemberCardInvoiceState": MemberCardInvoiceState, "InvoiceGroupContractorIC": InvoiceGroupContractorIC, "InvoiceGroupContractorDIC": InvoiceGroupContractorDIC, "InvoiceGroupContractorPhone": InvoiceGroupContractorPhone, "InvoiceGroupContractorEmail": InvoiceGroupContractorEmail, "InvoiceGroupWeb": InvoiceGroupWeb, "InvoiceGroupFileReference": InvoiceGroupFileReference, "InvoiceGroupBankAccount": InvoiceGroupBankAccount, "InvoiceGroupBankCode": InvoiceGroupBankCode, "InvoiceGroupBank": InvoiceGroupBank, "PaymentType": PaymentType, "QRCodeString": QRCodeString, "InvoiceGroupContractor": InvoiceGroupContractor, "InvoiceGroupContractorAddress": InvoiceGroupContractorAddress, "InvoiceBankAccount": InvoiceBankAccount})

    # Načíst seznam typů členské karty
    def MemberCardTypeAll(self, ID_Login, ID_Person, FilterByAge, ID=None, DisplayName=None):
        return self._client.service.MemberCardTypeAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "FilterByAge": FilterByAge, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam členství osob v jednotce
    def MembershipAll(self, ID_Login, ID_Unit, ID_Person, OnlyDirectMember, IsSts, ShowHistory, IsValid, ID_MembershipType=None, ID_MembershipCategory=None, LastName=None, IdentificationCode=None, ShowLowerUnits=None):
        return self._client.service.MembershipAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "OnlyDirectMember": OnlyDirectMember, "IsSts": IsSts, "ShowHistory": ShowHistory, "IsValid": IsValid, "ID_MembershipType": ID_MembershipType, "ID_MembershipCategory": ID_MembershipCategory, "LastName": LastName, "IdentificationCode": IdentificationCode, "ShowLowerUnits": ShowLowerUnits})

    # Načíst seznam členství osob v jednotce
    def MembershipDetailPersonData(self, ID_Login, ID_Person):
        return self._client.service.MembershipDetailPersonData({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načíst zjednodušený seznam členství osoby
    def MembershipAllPersonList(self, ID_Login, ID_Person):
        return self._client.service.MembershipAllPersonList({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Načíst seznam přihlášek bez souboru přihlášky
    def MembershipApplicationAllEmptyEnroll(self, ID_Login):
        return self._client.service.MembershipApplicationAllEmptyEnroll({"ID_Login": ID_Login})

    # Načíst seznam přihlášek
    def MembershipApplicationAll(self, ID_Login, ID, ID_Unit, ID_Person, ID_MembershipApplicationState=None, MembershipApplicationStates=None):
        return self._client.service.MembershipApplicationAll({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ID_MembershipApplicationState": ID_MembershipApplicationState, "MembershipApplicationStates": MembershipApplicationStates})

    # Načíst detail přihlášky pro sestavu
    def MembershipApplicationDetailReport(self, ID_Login, ID):
        return self._client.service.MembershipApplicationDetailReport({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail přihlášky
    def MembershipApplicationDetailAccessKey(self, ID_Login, ID_Application, AccessKey):
        return self._client.service.MembershipApplicationDetailAccessKey({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey})

    # Načíst detail přihlášky
    def MembershipApplicationDetail(self, ID_Login, ID):
        return self._client.service.MembershipApplicationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit přihlášku
    def MembershipApplicationInsert(self, ID_Login, ID, ID_Unit, ID_Person, ValidTo, AccessKey, IsValid, DateCreate, LastOpened, IsAdult, DateFilled, DateFinished, Birthday, DateState, IsForeign, ID_DistrictBirth, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, ID_Assurance, Unit=None, UnitTitle=None, LogoExtension=None, RegistrationNumber=None, ID_MembershipApplicationState=None, MembershipApplicationState=None, FirstName=None, LastName=None, FirstNameParent=None, LastNameParent=None, NoteParent=None, ParentNote=None, ParentType=None, ParentTypeCustom=None, FirstNameParent2=None, LastNameParent2=None, NoteParent2=None, Parent2Note=None, ParentType2=None, ParentTypeCustom2=None, Person=None, IdentificationCode=None, PhoneMainHelp=None, PhoneMainPlaceholder=None, EmailMainHelp=None, EmailMainPlaceholder=None, Reason=None, ID_Sex=None, Sex=None, MaidenName=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, BirthCity=None, DistrictBirth=None, Degrees=None, ID_DegreeType1=None, ID_DegreeType2=None, ID_DegreeType3=None, Street=None, City=None, PostalFirstLine=None, State=None, Postcode=None, PostalStreet=None, PostalState=None, PostalPostcode=None, PostalCity=None, PhoneParent=None, EmailParent=None, PhoneParent2=None, EmailParent2=None, Phone=None, Email=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Assurance=None):
        return self._client.service.MembershipApplicationInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ValidTo": ValidTo, "AccessKey": AccessKey, "IsValid": IsValid, "DateCreate": DateCreate, "LastOpened": LastOpened, "IsAdult": IsAdult, "DateFilled": DateFilled, "DateFinished": DateFinished, "Birthday": Birthday, "DateState": DateState, "IsForeign": IsForeign, "ID_DistrictBirth": ID_DistrictBirth, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "ID_Assurance": ID_Assurance, "Unit": Unit, "UnitTitle": UnitTitle, "LogoExtension": LogoExtension, "RegistrationNumber": RegistrationNumber, "ID_MembershipApplicationState": ID_MembershipApplicationState, "MembershipApplicationState": MembershipApplicationState, "FirstName": FirstName, "LastName": LastName, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "NoteParent": NoteParent, "ParentNote": ParentNote, "ParentType": ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "NoteParent2": NoteParent2, "Parent2Note": Parent2Note, "ParentType2": ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "Person": Person, "IdentificationCode": IdentificationCode, "PhoneMainHelp": PhoneMainHelp, "PhoneMainPlaceholder": PhoneMainPlaceholder, "EmailMainHelp": EmailMainHelp, "EmailMainPlaceholder": EmailMainPlaceholder, "Reason": Reason, "ID_Sex": ID_Sex, "Sex": Sex, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "DistrictBirth": DistrictBirth, "Degrees": Degrees, "ID_DegreeType1": ID_DegreeType1, "ID_DegreeType2": ID_DegreeType2, "ID_DegreeType3": ID_DegreeType3, "Street": Street, "City": City, "PostalFirstLine": PostalFirstLine, "State": State, "Postcode": Postcode, "PostalStreet": PostalStreet, "PostalState": PostalState, "PostalPostcode": PostalPostcode, "PostalCity": PostalCity, "PhoneParent": PhoneParent, "EmailParent": EmailParent, "PhoneParent2": PhoneParent2, "EmailParent2": EmailParent2, "Phone": Phone, "Email": Email, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Assurance": Assurance})

    # Načíst seznam stavů přihlášky
    def MembershipApplicationStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.MembershipApplicationStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Generovat PDF e-přihlášky
    def MembershipApplicationOtherGenerateEnroll(self, ID_Login, ID=None):
        return self._client.service.MembershipApplicationOtherGenerateEnroll({"ID_Login": ID_Login, "ID": ID})

    # Upravit přihlášku
    def MembershipApplicationUpdateAccessKey(self, ID_Login, ID_Application, AccessKey, OnlyValidate, Birthday, IsForeign, ID_DegreeType1, ID_DegreeType2, ID_DegreeType3, ID_DistrictBirth, ID_PersonPersonParent, ID_PersonPersonParent2, ID_Assurance, CheckInfo, CheckAllowDataStorage, CheckAllowAudiovisual, CheckAllowSocialNetwork, CheckAllowMarketing, CheckCorrect, IsPostalSame, FirstName=None, LastName=None, ID_Sex=None, IdentificationCode=None, Address=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalAddress=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Phone=None, Email=None, Note=None, MaidenName=None, ID_Citizenship=None, CitizenshipCustom=None, BirthCity=None, ID_ParentType=None, ParentTypeCustom=None, FirstNameParent=None, LastNameParent=None, EmailParent=None, PhoneParent=None, NoteParent=None, ID_ParentType2=None, ParentTypeCustom2=None, FirstNameParent2=None, LastNameParent2=None, EmailParent2=None, PhoneParent2=None, NoteParent2=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, ParentNote=None):
        return self._client.service.MembershipApplicationUpdateAccessKey({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "OnlyValidate": OnlyValidate, "Birthday": Birthday, "IsForeign": IsForeign, "ID_DegreeType1": ID_DegreeType1, "ID_DegreeType2": ID_DegreeType2, "ID_DegreeType3": ID_DegreeType3, "ID_DistrictBirth": ID_DistrictBirth, "ID_PersonPersonParent": ID_PersonPersonParent, "ID_PersonPersonParent2": ID_PersonPersonParent2, "ID_Assurance": ID_Assurance, "CheckInfo": CheckInfo, "CheckAllowDataStorage": CheckAllowDataStorage, "CheckAllowAudiovisual": CheckAllowAudiovisual, "CheckAllowSocialNetwork": CheckAllowSocialNetwork, "CheckAllowMarketing": CheckAllowMarketing, "CheckCorrect": CheckCorrect, "IsPostalSame": IsPostalSame, "FirstName": FirstName, "LastName": LastName, "ID_Sex": ID_Sex, "IdentificationCode": IdentificationCode, "Address": Address, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalAddress": PostalAddress, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Phone": Phone, "Email": Email, "Note": Note, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "ID_ParentType": ID_ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "EmailParent": EmailParent, "PhoneParent": PhoneParent, "NoteParent": NoteParent, "ID_ParentType2": ID_ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "EmailParent2": EmailParent2, "PhoneParent2": PhoneParent2, "NoteParent2": NoteParent2, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "ParentNote": ParentNote})

    # Dokončit přihlášku
    def MembershipApplicationUpdateFinish(self, ID_Login, ID, ID_Unit, ID_Person, ValidTo, AccessKey, IsValid, DateCreate, LastOpened, IsAdult, DateFilled, DateFinished, Birthday, DateState, IsForeign, ID_DistrictBirth, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, ID_Assurance, Unit=None, UnitTitle=None, LogoExtension=None, RegistrationNumber=None, ID_MembershipApplicationState=None, MembershipApplicationState=None, FirstName=None, LastName=None, FirstNameParent=None, LastNameParent=None, NoteParent=None, ParentNote=None, ParentType=None, ParentTypeCustom=None, FirstNameParent2=None, LastNameParent2=None, NoteParent2=None, Parent2Note=None, ParentType2=None, ParentTypeCustom2=None, Person=None, IdentificationCode=None, PhoneMainHelp=None, PhoneMainPlaceholder=None, EmailMainHelp=None, EmailMainPlaceholder=None, Reason=None, ID_Sex=None, Sex=None, MaidenName=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, BirthCity=None, DistrictBirth=None, Degrees=None, ID_DegreeType1=None, ID_DegreeType2=None, ID_DegreeType3=None, Street=None, City=None, PostalFirstLine=None, State=None, Postcode=None, PostalStreet=None, PostalState=None, PostalPostcode=None, PostalCity=None, PhoneParent=None, EmailParent=None, PhoneParent2=None, EmailParent2=None, Phone=None, Email=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Assurance=None):
        return self._client.service.MembershipApplicationUpdateFinish({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ValidTo": ValidTo, "AccessKey": AccessKey, "IsValid": IsValid, "DateCreate": DateCreate, "LastOpened": LastOpened, "IsAdult": IsAdult, "DateFilled": DateFilled, "DateFinished": DateFinished, "Birthday": Birthday, "DateState": DateState, "IsForeign": IsForeign, "ID_DistrictBirth": ID_DistrictBirth, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "ID_Assurance": ID_Assurance, "Unit": Unit, "UnitTitle": UnitTitle, "LogoExtension": LogoExtension, "RegistrationNumber": RegistrationNumber, "ID_MembershipApplicationState": ID_MembershipApplicationState, "MembershipApplicationState": MembershipApplicationState, "FirstName": FirstName, "LastName": LastName, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "NoteParent": NoteParent, "ParentNote": ParentNote, "ParentType": ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "NoteParent2": NoteParent2, "Parent2Note": Parent2Note, "ParentType2": ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "Person": Person, "IdentificationCode": IdentificationCode, "PhoneMainHelp": PhoneMainHelp, "PhoneMainPlaceholder": PhoneMainPlaceholder, "EmailMainHelp": EmailMainHelp, "EmailMainPlaceholder": EmailMainPlaceholder, "Reason": Reason, "ID_Sex": ID_Sex, "Sex": Sex, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "DistrictBirth": DistrictBirth, "Degrees": Degrees, "ID_DegreeType1": ID_DegreeType1, "ID_DegreeType2": ID_DegreeType2, "ID_DegreeType3": ID_DegreeType3, "Street": Street, "City": City, "PostalFirstLine": PostalFirstLine, "State": State, "Postcode": Postcode, "PostalStreet": PostalStreet, "PostalState": PostalState, "PostalPostcode": PostalPostcode, "PostalCity": PostalCity, "PhoneParent": PhoneParent, "EmailParent": EmailParent, "PhoneParent2": PhoneParent2, "EmailParent2": EmailParent2, "Phone": Phone, "Email": Email, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Assurance": Assurance})

    # Odmítnout přihlášku
    def MembershipApplicationUpdateDeny(self, ID_Login, ID, ID_Unit, ID_Person, ValidTo, AccessKey, IsValid, DateCreate, LastOpened, IsAdult, DateFilled, DateFinished, Birthday, DateState, IsForeign, ID_DistrictBirth, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, ID_Assurance, Unit=None, UnitTitle=None, LogoExtension=None, RegistrationNumber=None, ID_MembershipApplicationState=None, MembershipApplicationState=None, FirstName=None, LastName=None, FirstNameParent=None, LastNameParent=None, NoteParent=None, ParentNote=None, ParentType=None, ParentTypeCustom=None, FirstNameParent2=None, LastNameParent2=None, NoteParent2=None, Parent2Note=None, ParentType2=None, ParentTypeCustom2=None, Person=None, IdentificationCode=None, PhoneMainHelp=None, PhoneMainPlaceholder=None, EmailMainHelp=None, EmailMainPlaceholder=None, Reason=None, ID_Sex=None, Sex=None, MaidenName=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, BirthCity=None, DistrictBirth=None, Degrees=None, ID_DegreeType1=None, ID_DegreeType2=None, ID_DegreeType3=None, Street=None, City=None, PostalFirstLine=None, State=None, Postcode=None, PostalStreet=None, PostalState=None, PostalPostcode=None, PostalCity=None, PhoneParent=None, EmailParent=None, PhoneParent2=None, EmailParent2=None, Phone=None, Email=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Assurance=None):
        return self._client.service.MembershipApplicationUpdateDeny({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ValidTo": ValidTo, "AccessKey": AccessKey, "IsValid": IsValid, "DateCreate": DateCreate, "LastOpened": LastOpened, "IsAdult": IsAdult, "DateFilled": DateFilled, "DateFinished": DateFinished, "Birthday": Birthday, "DateState": DateState, "IsForeign": IsForeign, "ID_DistrictBirth": ID_DistrictBirth, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "ID_Assurance": ID_Assurance, "Unit": Unit, "UnitTitle": UnitTitle, "LogoExtension": LogoExtension, "RegistrationNumber": RegistrationNumber, "ID_MembershipApplicationState": ID_MembershipApplicationState, "MembershipApplicationState": MembershipApplicationState, "FirstName": FirstName, "LastName": LastName, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "NoteParent": NoteParent, "ParentNote": ParentNote, "ParentType": ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "NoteParent2": NoteParent2, "Parent2Note": Parent2Note, "ParentType2": ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "Person": Person, "IdentificationCode": IdentificationCode, "PhoneMainHelp": PhoneMainHelp, "PhoneMainPlaceholder": PhoneMainPlaceholder, "EmailMainHelp": EmailMainHelp, "EmailMainPlaceholder": EmailMainPlaceholder, "Reason": Reason, "ID_Sex": ID_Sex, "Sex": Sex, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "DistrictBirth": DistrictBirth, "Degrees": Degrees, "ID_DegreeType1": ID_DegreeType1, "ID_DegreeType2": ID_DegreeType2, "ID_DegreeType3": ID_DegreeType3, "Street": Street, "City": City, "PostalFirstLine": PostalFirstLine, "State": State, "Postcode": Postcode, "PostalStreet": PostalStreet, "PostalState": PostalState, "PostalPostcode": PostalPostcode, "PostalCity": PostalCity, "PhoneParent": PhoneParent, "EmailParent": EmailParent, "PhoneParent2": PhoneParent2, "EmailParent2": EmailParent2, "Phone": Phone, "Email": Email, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Assurance": Assurance})

    # Upravit přihlášku
    def MembershipApplicationUpdate(self, ID_Login, ID, ID_Unit, ID_Person, ValidTo, AccessKey, IsValid, DateCreate, LastOpened, IsAdult, DateFilled, DateFinished, Birthday, DateState, IsForeign, ID_DistrictBirth, AllowDataStorage, AllowAudiovisual, AllowSocialNetwork, AllowMarketing, ID_Assurance, Unit=None, UnitTitle=None, LogoExtension=None, RegistrationNumber=None, ID_MembershipApplicationState=None, MembershipApplicationState=None, FirstName=None, LastName=None, FirstNameParent=None, LastNameParent=None, NoteParent=None, ParentNote=None, ParentType=None, ParentTypeCustom=None, FirstNameParent2=None, LastNameParent2=None, NoteParent2=None, Parent2Note=None, ParentType2=None, ParentTypeCustom2=None, Person=None, IdentificationCode=None, PhoneMainHelp=None, PhoneMainPlaceholder=None, EmailMainHelp=None, EmailMainPlaceholder=None, Reason=None, ID_Sex=None, Sex=None, MaidenName=None, ID_Citizenship=None, Citizenship=None, CitizenshipCustom=None, BirthCity=None, DistrictBirth=None, Degrees=None, ID_DegreeType1=None, ID_DegreeType2=None, ID_DegreeType3=None, Street=None, City=None, PostalFirstLine=None, State=None, Postcode=None, PostalStreet=None, PostalState=None, PostalPostcode=None, PostalCity=None, PhoneParent=None, EmailParent=None, PhoneParent2=None, EmailParent2=None, Phone=None, Email=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None, Assurance=None):
        return self._client.service.MembershipApplicationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Person": ID_Person, "ValidTo": ValidTo, "AccessKey": AccessKey, "IsValid": IsValid, "DateCreate": DateCreate, "LastOpened": LastOpened, "IsAdult": IsAdult, "DateFilled": DateFilled, "DateFinished": DateFinished, "Birthday": Birthday, "DateState": DateState, "IsForeign": IsForeign, "ID_DistrictBirth": ID_DistrictBirth, "AllowDataStorage": AllowDataStorage, "AllowAudiovisual": AllowAudiovisual, "AllowSocialNetwork": AllowSocialNetwork, "AllowMarketing": AllowMarketing, "ID_Assurance": ID_Assurance, "Unit": Unit, "UnitTitle": UnitTitle, "LogoExtension": LogoExtension, "RegistrationNumber": RegistrationNumber, "ID_MembershipApplicationState": ID_MembershipApplicationState, "MembershipApplicationState": MembershipApplicationState, "FirstName": FirstName, "LastName": LastName, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "NoteParent": NoteParent, "ParentNote": ParentNote, "ParentType": ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "NoteParent2": NoteParent2, "Parent2Note": Parent2Note, "ParentType2": ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "Person": Person, "IdentificationCode": IdentificationCode, "PhoneMainHelp": PhoneMainHelp, "PhoneMainPlaceholder": PhoneMainPlaceholder, "EmailMainHelp": EmailMainHelp, "EmailMainPlaceholder": EmailMainPlaceholder, "Reason": Reason, "ID_Sex": ID_Sex, "Sex": Sex, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "Citizenship": Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "DistrictBirth": DistrictBirth, "Degrees": Degrees, "ID_DegreeType1": ID_DegreeType1, "ID_DegreeType2": ID_DegreeType2, "ID_DegreeType3": ID_DegreeType3, "Street": Street, "City": City, "PostalFirstLine": PostalFirstLine, "State": State, "Postcode": Postcode, "PostalStreet": PostalStreet, "PostalState": PostalState, "PostalPostcode": PostalPostcode, "PostalCity": PostalCity, "PhoneParent": PhoneParent, "EmailParent": EmailParent, "PhoneParent2": PhoneParent2, "EmailParent2": EmailParent2, "Phone": Phone, "Email": Email, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School, "Assurance": Assurance})

    # Načíst pozice užívání nemovistostí v dane oblasti
    def OccupationAllPositions(self, ID_Login, ID_Application, GpsLatitudeStart, GpsLongitudeStart, GpsLatitudeEnd, GpsLongitudeEnd, ID_Unit, IncludeChildUnits, Publish, ID_RealtyType, GpsLatitude, GpsLongitude, Distance, AdvertisingCategories=None):
        return self._client.service.OccupationAllPositions({"ID_Login": ID_Login, "ID_Application": ID_Application, "GpsLatitudeStart": GpsLatitudeStart, "GpsLongitudeStart": GpsLongitudeStart, "GpsLatitudeEnd": GpsLatitudeEnd, "GpsLongitudeEnd": GpsLongitudeEnd, "ID_Unit": ID_Unit, "IncludeChildUnits": IncludeChildUnits, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "Distance": Distance, "AdvertisingCategories": AdvertisingCategories})

    # Načíst seznam užívání nemovitosti
    def OccupationAllUnit(self, ID_Login, ID_Unit, IsActive):
        return self._client.service.OccupationAllUnit({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsActive": IsActive})

    # Smazat užívání nemovitosti
    def OccupationDeleteRealty(self, ID_Login, ID):
        return self._client.service.OccupationDeleteRealty({"ID_Login": ID_Login, "ID": ID})

    # Načíst užívání nemovistostí ze sloučené oblasti
    def OccupationAllGrouped(self, ID, ID_Unit, IncludeChildUnits, Publish, ID_RealtyType, GpsLatitude, GpsLongitude, Distance, ID_Login, ID_Application, AdvertisingCategories=None):
        return self._client.service.OccupationAllGrouped({"ID": ID, "ID_Unit": ID_Unit, "IncludeChildUnits": IncludeChildUnits, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "Distance": Distance, "ID_Login": ID_Login, "ID_Application": ID_Application, "AdvertisingCategories": AdvertisingCategories})

    # Načíst detail užívání nemovitosti
    def OccupationDetailRealtyDownload(self, ID_Login, ID, ID_Unit, ID_Realty, Publish, ID_RealtyType, Note=None, RealtyType=None):
        return self._client.service.OccupationDetailRealtyDownload({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Realty": ID_Realty, "Publish": Publish, "ID_RealtyType": ID_RealtyType, "Note": Note, "RealtyType": RealtyType})

    # Načíst detail užívání nemovitosti
    def OccupationDetailRealty(self, ID_Login, ID, ID_Application):
        return self._client.service.OccupationDetailRealty({"ID_Login": ID_Login, "ID": ID, "ID_Application": ID_Application})

    # Načíst seznam vybavení
    def OccupationEquipmentAll(self, ID_Login, ID_Application, ID, ID_RealtyType, DisplayName=None):
        return self._client.service.OccupationEquipmentAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_RealtyType": ID_RealtyType, "DisplayName": DisplayName})

    # Načíst seznam uživatelem spravovaných půjčitelných jednotek
    def OccupationRentAllBorrowable(self, ID_Login):
        return self._client.service.OccupationRentAllBorrowable({"ID_Login": ID_Login})

    # Načíst seznam půjčitelných jednotek
    def OccupationRentAllPublic(self, ID_Application, ID_Login, BasePrice, ScoutPrice, ChildPrice, ID_Occupation, OccupationLanguageList=None, PriceTypeList=None):
        return self._client.service.OccupationRentAllPublic({"ID_Application": ID_Application, "ID_Login": ID_Login, "BasePrice": BasePrice, "ScoutPrice": ScoutPrice, "ChildPrice": ChildPrice, "ID_Occupation": ID_Occupation, "OccupationLanguageList": OccupationLanguageList, "PriceTypeList": PriceTypeList})

    # Načíst detail půjčitelné jednotky
    def OccupationRentDetailPublic(self, ID_Application, ID, ID_Login):
        return self._client.service.OccupationRentDetailPublic({"ID_Application": ID_Application, "ID": ID, "ID_Login": ID_Login})

    # Načíst seznam rezervací půjčitelné jednotky pro kalendář
    def OccupationRentReservationAllCalendar(self, ID_Login, ID_Application, ID, ShowAdminView, CalendarName=None, CalendarDescription=None):
        return self._client.service.OccupationRentReservationAllCalendar({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ShowAdminView": ShowAdminView, "CalendarName": CalendarName, "CalendarDescription": CalendarDescription})

    # Načíst seznam rezervací
    def OccupationRentReservationAllOverview(self, ID_Login, ID_OccupationRent, ID, ID_User, ID_OccupationRentReservationState=None):
        return self._client.service.OccupationRentReservationAllOverview({"ID_Login": ID_Login, "ID_OccupationRent": ID_OccupationRent, "ID": ID, "ID_User": ID_User, "ID_OccupationRentReservationState": ID_OccupationRentReservationState})

    # Načíst seznam rezervací půjčitelné jednotky
    def OccupationRentReservationAll(self, ID_Login, ID_OccupationRent, ID, ID_User, ID_OccupationRentReservationState=None):
        return self._client.service.OccupationRentReservationAll({"ID_Login": ID_Login, "ID_OccupationRent": ID_OccupationRent, "ID": ID, "ID_User": ID_User, "ID_OccupationRentReservationState": ID_OccupationRentReservationState})

    # Smazat rezervaci půjčitelné jednotky
    def OccupationRentReservationDelete(self, ID_Login, ID):
        return self._client.service.OccupationRentReservationDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail rezervace půjčitelné jednotky
    def OccupationRentReservationDetail(self, ID_Application, ID_Login, ID):
        return self._client.service.OccupationRentReservationDetail({"ID_Application": ID_Application, "ID_Login": ID_Login, "ID": ID})

    # Založit rezervaci půjčitelné jednotky
    def OccupationRentReservationInsert(self, ID_Login, ID, ID_User, ID_Occupation, ID_OccupationRent, ID_Unit, EstimatedStart, EstimatedEnd, RealStart, RealEnd, EstimatedPersonCount, LastUpdate, Created, ID_OccupationRentReservationState=None, OccupationRentReservationState=None, OccupationRent=None, Unit=None, RegistrationNumber=None, Contact=None, ContactPerson=None, ContactPhone=None, ContactMail=None, RejectionReason=None, Note=None):
        return self._client.service.OccupationRentReservationInsert({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Occupation": ID_Occupation, "ID_OccupationRent": ID_OccupationRent, "ID_Unit": ID_Unit, "EstimatedStart": EstimatedStart, "EstimatedEnd": EstimatedEnd, "RealStart": RealStart, "RealEnd": RealEnd, "EstimatedPersonCount": EstimatedPersonCount, "LastUpdate": LastUpdate, "Created": Created, "ID_OccupationRentReservationState": ID_OccupationRentReservationState, "OccupationRentReservationState": OccupationRentReservationState, "OccupationRent": OccupationRent, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Contact": Contact, "ContactPerson": ContactPerson, "ContactPhone": ContactPhone, "ContactMail": ContactMail, "RejectionReason": RejectionReason, "Note": Note})

    # Upravit rezervaci půjčitelné jednotky
    def OccupationRentReservationUpdate(self, ID_Login, ID, ID_User, ID_Occupation, ID_OccupationRent, ID_Unit, EstimatedStart, EstimatedEnd, RealStart, RealEnd, EstimatedPersonCount, LastUpdate, Created, ID_OccupationRentReservationState=None, OccupationRentReservationState=None, OccupationRent=None, Unit=None, RegistrationNumber=None, Contact=None, ContactPerson=None, ContactPhone=None, ContactMail=None, RejectionReason=None, Note=None):
        return self._client.service.OccupationRentReservationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_User": ID_User, "ID_Occupation": ID_Occupation, "ID_OccupationRent": ID_OccupationRent, "ID_Unit": ID_Unit, "EstimatedStart": EstimatedStart, "EstimatedEnd": EstimatedEnd, "RealStart": RealStart, "RealEnd": RealEnd, "EstimatedPersonCount": EstimatedPersonCount, "LastUpdate": LastUpdate, "Created": Created, "ID_OccupationRentReservationState": ID_OccupationRentReservationState, "OccupationRentReservationState": OccupationRentReservationState, "OccupationRent": OccupationRent, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Contact": Contact, "ContactPerson": ContactPerson, "ContactPhone": ContactPhone, "ContactMail": ContactMail, "RejectionReason": RejectionReason, "Note": Note})

    # Potvrdit rezervaci půjčitelné jednotky
    def OccupationRentReservationUpdateConfirm(self, ID_Login, ID):
        return self._client.service.OccupationRentReservationUpdateConfirm({"ID_Login": ID_Login, "ID": ID})

    # Zrušit rezervaci půjčitelné jednotky
    def OccupationRentReservationUpdateReject(self, ID_Login, ID, RejectionReason=None):
        return self._client.service.OccupationRentReservationUpdateReject({"ID_Login": ID_Login, "ID": ID, "RejectionReason": RejectionReason})

    # Upravit užívání nemovitosti
    def OccupationUpdateRealty(self, ID, ID_Login, Publish, IsBorrowable, Capacity, BorrowableForeign, IsBookable, ID_TempFilePhotoExtension, ID_TempFileRequirementExtension, Note=None, DisplayName=None, Person=None, Email=None, Phone=None, Web=None, Fotogallery=None, ContactNote=None, Requirements=None, CapacityNote=None, AccommodationNote=None, BookUrl=None, Tags=None, Equipment=None, Languages=None):
        return self._client.service.OccupationUpdateRealty({"ID": ID, "ID_Login": ID_Login, "Publish": Publish, "IsBorrowable": IsBorrowable, "Capacity": Capacity, "BorrowableForeign": BorrowableForeign, "IsBookable": IsBookable, "ID_TempFilePhotoExtension": ID_TempFilePhotoExtension, "ID_TempFileRequirementExtension": ID_TempFileRequirementExtension, "Note": Note, "DisplayName": DisplayName, "Person": Person, "Email": Email, "Phone": Phone, "Web": Web, "Fotogallery": Fotogallery, "ContactNote": ContactNote, "Requirements": Requirements, "CapacityNote": CapacityNote, "AccommodationNote": AccommodationNote, "BookUrl": BookUrl, "Tags": Tags, "Equipment": Equipment, "Languages": Languages})

    # Založit užívání nemovitosti
    def OccupationInsertRealty(self, ID_Login, ID_Unit, ID_Realty, ID_RealtyType, Publish, IsBorrowable, Capacity, BorrowableForeign, IsBookable, ID_TempFilePhotoExtension, ID_TempFileRequirementExtension, BasePrice, ScoutPrice, ChildPrice, Note=None, DisplayName=None, Person=None, Email=None, Phone=None, Web=None, Fotogallery=None, ContactNote=None, Requirements=None, CapacityNote=None, AccommodationNote=None, Tags=None, Equipment=None, Languages=None, ID_OccupationRentPriceType=None, PriceNote=None):
        return self._client.service.OccupationInsertRealty({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Realty": ID_Realty, "ID_RealtyType": ID_RealtyType, "Publish": Publish, "IsBorrowable": IsBorrowable, "Capacity": Capacity, "BorrowableForeign": BorrowableForeign, "IsBookable": IsBookable, "ID_TempFilePhotoExtension": ID_TempFilePhotoExtension, "ID_TempFileRequirementExtension": ID_TempFileRequirementExtension, "BasePrice": BasePrice, "ScoutPrice": ScoutPrice, "ChildPrice": ChildPrice, "Note": Note, "DisplayName": DisplayName, "Person": Person, "Email": Email, "Phone": Phone, "Web": Web, "Fotogallery": Fotogallery, "ContactNote": ContactNote, "Requirements": Requirements, "CapacityNote": CapacityNote, "AccommodationNote": AccommodationNote, "Tags": Tags, "Equipment": Equipment, "Languages": Languages, "ID_OccupationRentPriceType": ID_OccupationRentPriceType, "PriceNote": PriceNote})

    # Načíst seznam jazyků
    def OccupationLanguageAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.OccupationLanguageAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam půjčitelných jednotek
    def OccupationRentAll(self, ID_Login, ID_Application, ID_Occupation, ID, DisplayName=None):
        return self._client.service.OccupationRentAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Occupation": ID_Occupation, "ID": ID, "DisplayName": DisplayName})

    # Načíst detail půjčitelné jednotky
    def OccupationRentDetail(self, ID_Login, ID):
        return self._client.service.OccupationRentDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam vybavení
    def OccupationRentEquipmentAll(self, ID_Login, ID_Application, ID_Occupation, ID, ID_OccupationEquipment):
        return self._client.service.OccupationRentEquipmentAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Occupation": ID_Occupation, "ID": ID, "ID_OccupationEquipment": ID_OccupationEquipment})

    # Založit půjčitelnou jednotku
    def OccupationRentInsert(self, ID_Login, ID, ID_Occupation, IsActive, ID_TempFilePhotoExtension, ID_TempFileRequirementExtension, Capacity, BorrowableForeign, IsBookable, LastUpdate, ID_DocumentRequirement, ID_DocumentPhoto, DisplayName=None, Email=None, Phone=None, Web=None, PhotoExtension=None, Fotogallery=None, ContactNote=None, RequirementExtension=None, Requirements=None, CapacityNote=None, AccommodationNote=None, Person=None, Equipment=None, Tags=None, Languages=None):
        return self._client.service.OccupationRentInsert({"ID_Login": ID_Login, "ID": ID, "ID_Occupation": ID_Occupation, "IsActive": IsActive, "ID_TempFilePhotoExtension": ID_TempFilePhotoExtension, "ID_TempFileRequirementExtension": ID_TempFileRequirementExtension, "Capacity": Capacity, "BorrowableForeign": BorrowableForeign, "IsBookable": IsBookable, "LastUpdate": LastUpdate, "ID_DocumentRequirement": ID_DocumentRequirement, "ID_DocumentPhoto": ID_DocumentPhoto, "DisplayName": DisplayName, "Email": Email, "Phone": Phone, "Web": Web, "PhotoExtension": PhotoExtension, "Fotogallery": Fotogallery, "ContactNote": ContactNote, "RequirementExtension": RequirementExtension, "Requirements": Requirements, "CapacityNote": CapacityNote, "AccommodationNote": AccommodationNote, "Person": Person, "Equipment": Equipment, "Tags": Tags, "Languages": Languages})

    # Načíst seznam jazyků
    def OccupationRentLanguageAll(self, ID_Login, ID_Application, ID_Occupation, ID, ID_OccupationLanguage=None):
        return self._client.service.OccupationRentLanguageAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Occupation": ID_Occupation, "ID": ID, "ID_OccupationLanguage": ID_OccupationLanguage})

    # Načíst seznam cen za pronájem
    def OccupationRentPriceAll(self, ID_Login, ID_Occupation, ID, ID_OccupationRentPriceType=None):
        return self._client.service.OccupationRentPriceAll({"ID_Login": ID_Login, "ID_Occupation": ID_Occupation, "ID": ID, "ID_OccupationRentPriceType": ID_OccupationRentPriceType})

    # Smazat cenu za pronájem
    def OccupationRentPriceDelete(self, ID_Login, ID):
        return self._client.service.OccupationRentPriceDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail ceny za pronájem
    def OccupationRentPriceDetail(self, ID_Login, ID):
        return self._client.service.OccupationRentPriceDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit cenu za pronájem
    def OccupationRentPriceInsert(self, ID_Login, ID, ID_Occupation, ID_OccupationRent, BasePrice, ScoutPrice, ChildPrice, OccupationRent=None, ID_OccupationRentPriceType=None, OccupationRentPriceType=None, PriceNote=None):
        return self._client.service.OccupationRentPriceInsert({"ID_Login": ID_Login, "ID": ID, "ID_Occupation": ID_Occupation, "ID_OccupationRent": ID_OccupationRent, "BasePrice": BasePrice, "ScoutPrice": ScoutPrice, "ChildPrice": ChildPrice, "OccupationRent": OccupationRent, "ID_OccupationRentPriceType": ID_OccupationRentPriceType, "OccupationRentPriceType": OccupationRentPriceType, "PriceNote": PriceNote})

    # Načíst seznam typů ceny
    def OccupationRentPriceTypeAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.OccupationRentPriceTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Upravit cenu za pronájem
    def OccupationRentPriceUpdate(self, ID_Login, ID, ID_Occupation, ID_OccupationRent, BasePrice, ScoutPrice, ChildPrice, OccupationRent=None, ID_OccupationRentPriceType=None, OccupationRentPriceType=None, PriceNote=None):
        return self._client.service.OccupationRentPriceUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Occupation": ID_Occupation, "ID_OccupationRent": ID_OccupationRent, "BasePrice": BasePrice, "ScoutPrice": ScoutPrice, "ChildPrice": ChildPrice, "OccupationRent": OccupationRent, "ID_OccupationRentPriceType": ID_OccupationRentPriceType, "OccupationRentPriceType": OccupationRentPriceType, "PriceNote": PriceNote})

    # Načíst seznam tagů pronajímatelné jednotky
    def OccupationRentTagAll(self, ID_Login, ID_Occupation, ID, ID_OccupationTag):
        return self._client.service.OccupationRentTagAll({"ID_Login": ID_Login, "ID_Occupation": ID_Occupation, "ID": ID, "ID_OccupationTag": ID_OccupationTag})

    # Upravit půjčitelnou jednotku
    def OccupationRentUpdate(self, ID_Login, ID, ID_Occupation, IsActive, ID_TempFilePhotoExtension, ID_TempFileRequirementExtension, Capacity, BorrowableForeign, IsBookable, LastUpdate, ID_DocumentRequirement, ID_DocumentPhoto, DisplayName=None, Email=None, Phone=None, Web=None, PhotoExtension=None, Fotogallery=None, ContactNote=None, RequirementExtension=None, Requirements=None, CapacityNote=None, AccommodationNote=None, Person=None, Equipment=None, Tags=None, Languages=None):
        return self._client.service.OccupationRentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Occupation": ID_Occupation, "IsActive": IsActive, "ID_TempFilePhotoExtension": ID_TempFilePhotoExtension, "ID_TempFileRequirementExtension": ID_TempFileRequirementExtension, "Capacity": Capacity, "BorrowableForeign": BorrowableForeign, "IsBookable": IsBookable, "LastUpdate": LastUpdate, "ID_DocumentRequirement": ID_DocumentRequirement, "ID_DocumentPhoto": ID_DocumentPhoto, "DisplayName": DisplayName, "Email": Email, "Phone": Phone, "Web": Web, "PhotoExtension": PhotoExtension, "Fotogallery": Fotogallery, "ContactNote": ContactNote, "RequirementExtension": RequirementExtension, "Requirements": Requirements, "CapacityNote": CapacityNote, "AccommodationNote": AccommodationNote, "Person": Person, "Equipment": Equipment, "Tags": Tags, "Languages": Languages})

    # Načíst seznam tagů
    def OccupationTagAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.OccupationTagAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typůtypu zákonného zástupce
    def ParentTypeAll(self, ID_Login, ID_Application, ID=None, DisplayName=None):
        return self._client.service.ParentTypeAll({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam osob vzdělávací akce
    def PersonAllEventEducationApi(self, ID_Login, ID_Application, ID_EventEducation):
        return self._client.service.PersonAllEventEducationApi({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_EventEducation": ID_EventEducation})

    # Načíst seznam osob
    def PersonAllGlobalSearch(self, ID_Login, ID_Application, UseParentCode, IdentificationCode=None, FirstName=None, LastName=None, Name=None):
        return self._client.service.PersonAllGlobalSearch({"ID_Login": ID_Login, "ID_Application": ID_Application, "UseParentCode": UseParentCode, "IdentificationCode": IdentificationCode, "FirstName": FirstName, "LastName": LastName, "Name": Name})

    # Načíst seznam osob podle jména
    def PersonAllExternal(self, ID_Login, ID_Application, ID, ID_User, Top, DisplayName=None):
        return self._client.service.PersonAllExternal({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "ID_User": ID_User, "Top": Top, "DisplayName": DisplayName})

    # Načíst osoby k synchronizace google skupiny
    def PersonAllGoogleGroupSync(self, ID_Login, ID_GoogleGroup):
        return self._client.service.PersonAllGoogleGroupSync({"ID_Login": ID_Login, "ID_GoogleGroup": ID_GoogleGroup})

    # Načíst seznam osob
    def PersonAllMemberCardPrint(self, ID_Login, ID_MemberCardPrint):
        return self._client.service.PersonAllMemberCardPrint({"ID_Login": ID_Login, "ID_MemberCardPrint": ID_MemberCardPrint})

    # Načíst osoby ke změně
    def PersonChangeAllPersonChangeRequest(self, ID_Login, ID_PersonChangeRequest):
        return self._client.service.PersonChangeAllPersonChangeRequest({"ID_Login": ID_Login, "ID_PersonChangeRequest": ID_PersonChangeRequest})

    # Načíst detail nových dat u změny u osoby
    def PersonChangeDetailChanges(self, ID_Login, ID_Application, AccessKey, ID):
        return self._client.service.PersonChangeDetailChanges({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "ID": ID})

    # Načíst detail změny u osoby
    def PersonChangeDetail(self, ID_Login, ID_Application, AccessKey, ID):
        return self._client.service.PersonChangeDetail({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "ID": ID})

    # Založit změnu u osoby podle žádosti o změnu
    def PersonChangeInsertPersonChangeRequestPerson(self, ID_Login, ID_PersonChangeRequestPerson, SendMessage):
        return self._client.service.PersonChangeInsertPersonChangeRequestPerson({"ID_Login": ID_Login, "ID_PersonChangeRequestPerson": ID_PersonChangeRequestPerson, "SendMessage": SendMessage})

    # Ověření kódu pro změnu údajů osoby
    def PersonChangeOtherVerify(self, ID_Login, ID_Application, AccessKey, BirthDate, IsForeign, LastName=None, IdentificationCodeEnd=None, BirthCity=None):
        return self._client.service.PersonChangeOtherVerify({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "BirthDate": BirthDate, "IsForeign": IsForeign, "LastName": LastName, "IdentificationCodeEnd": IdentificationCodeEnd, "BirthCity": BirthCity})

    # Načíst detail žádosti změn u osoby
    def PersonChangeRequestDetail(self, ID_Login, ID):
        return self._client.service.PersonChangeRequestDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit žádost změn u osoby
    def PersonChangeRequestInsert(self, ID_Login, ID, ID_Unit, Created, Sent, Text=None, Persons=None):
        return self._client.service.PersonChangeRequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Created": Created, "Sent": Sent, "Text": Text, "Persons": Persons})

    # Odeslat žádosti změn u osoby
    def PersonChangeRequestUpdate(self, ID_Login, ID, ID_Unit, Created, Sent, Text=None, Persons=None):
        return self._client.service.PersonChangeRequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "Created": Created, "Sent": Sent, "Text": Text, "Persons": Persons})

    # Dokončit změny u osoby
    def PersonChangeUpdateFinish(self, ID_Login, ID):
        return self._client.service.PersonChangeUpdateFinish({"ID_Login": ID_Login, "ID": ID})

    # Změnit stav u změny u osoby
    def PersonChangeUpdateState(self, ID_Login, ID, ID_PersonChangeState=None):
        return self._client.service.PersonChangeUpdateState({"ID_Login": ID_Login, "ID": ID, "ID_PersonChangeState": ID_PersonChangeState})

    # Upravit změnu u osoby
    def PersonChangeUpdate(self, ID_Login, ID_Application, AccessKey, OnlyValidate, Birthday, IsForeign, ID_DistrictBirth, ID_PersonParentPerson, ID_PersonParent, DeleteParent, ID_PersonParentPerson2, ID_PersonParent2, DeleteParent2, ID_Assurance, CheckCorrect, IsPostalSame, FirstName=None, LastName=None, ID_Sex=None, IdentificationCode=None, Address=None, Street=None, City=None, Postcode=None, State=None, PostalFirstLine=None, PostalAddress=None, PostalStreet=None, PostalCity=None, PostalPostcode=None, PostalState=None, Phone=None, Email=None, Note=None, MaidenName=None, ID_Citizenship=None, CitizenshipCustom=None, BirthCity=None, ID_ParentType=None, ParentType=None, ParentTypeCustom=None, FirstNameParent=None, LastNameParent=None, EmailParent=None, PhoneParent=None, NoteParent=None, ParentNote=None, ID_ParentType2=None, ParentType2=None, ParentTypeCustom2=None, FirstNameParent2=None, LastNameParent2=None, EmailParent2=None, PhoneParent2=None, NoteParent2=None, Parent2Note=None, InsuranceNumber=None, Allergy=None, FoodRestrictions=None, Drugs=None, SpecialRequirements=None, HealthLimitation=None, BodySkills=None, School=None):
        return self._client.service.PersonChangeUpdate({"ID_Login": ID_Login, "ID_Application": ID_Application, "AccessKey": AccessKey, "OnlyValidate": OnlyValidate, "Birthday": Birthday, "IsForeign": IsForeign, "ID_DistrictBirth": ID_DistrictBirth, "ID_PersonParentPerson": ID_PersonParentPerson, "ID_PersonParent": ID_PersonParent, "DeleteParent": DeleteParent, "ID_PersonParentPerson2": ID_PersonParentPerson2, "ID_PersonParent2": ID_PersonParent2, "DeleteParent2": DeleteParent2, "ID_Assurance": ID_Assurance, "CheckCorrect": CheckCorrect, "IsPostalSame": IsPostalSame, "FirstName": FirstName, "LastName": LastName, "ID_Sex": ID_Sex, "IdentificationCode": IdentificationCode, "Address": Address, "Street": Street, "City": City, "Postcode": Postcode, "State": State, "PostalFirstLine": PostalFirstLine, "PostalAddress": PostalAddress, "PostalStreet": PostalStreet, "PostalCity": PostalCity, "PostalPostcode": PostalPostcode, "PostalState": PostalState, "Phone": Phone, "Email": Email, "Note": Note, "MaidenName": MaidenName, "ID_Citizenship": ID_Citizenship, "CitizenshipCustom": CitizenshipCustom, "BirthCity": BirthCity, "ID_ParentType": ID_ParentType, "ParentType": ParentType, "ParentTypeCustom": ParentTypeCustom, "FirstNameParent": FirstNameParent, "LastNameParent": LastNameParent, "EmailParent": EmailParent, "PhoneParent": PhoneParent, "NoteParent": NoteParent, "ParentNote": ParentNote, "ID_ParentType2": ID_ParentType2, "ParentType2": ParentType2, "ParentTypeCustom2": ParentTypeCustom2, "FirstNameParent2": FirstNameParent2, "LastNameParent2": LastNameParent2, "EmailParent2": EmailParent2, "PhoneParent2": PhoneParent2, "NoteParent2": NoteParent2, "Parent2Note": Parent2Note, "InsuranceNumber": InsuranceNumber, "Allergy": Allergy, "FoodRestrictions": FoodRestrictions, "Drugs": Drugs, "SpecialRequirements": SpecialRequirements, "HealthLimitation": HealthLimitation, "BodySkills": BodySkills, "School": School})

    # Načíst seznam kontaktů rodičů osoby
    def PersonContactAllParent(self, ID_Login, ID_Person):
        return self._client.service.PersonContactAllParent({"ID_Login": ID_Login, "ID_Person": ID_Person})

    # Detail změny kontaktu
    def PersonContactRequestDetail(self, ID_Login, ID):
        return self._client.service.PersonContactRequestDetail({"ID_Login": ID_Login, "ID": ID})

    # Detail změnu kontaktu podle kódu
    def PersonContactRequestDetailCode(self, ID_Login, Code):
        return self._client.service.PersonContactRequestDetailCode({"ID_Login": ID_Login, "Code": Code})

    # Upravit změnu kontaktu
    def PersonContactRequestUpdate(self, ID_Login, ID, ID_PersonContact, ValidTo, Created, ID_User, Completed, Code, ID_Person, IsCatalog, IsGa, ID_ContactRequestType=None, ContactRequestType=None, Person=None, ID_ContactType=None, ContactType=None, Value=None, Note=None):
        return self._client.service.PersonContactRequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_PersonContact": ID_PersonContact, "ValidTo": ValidTo, "Created": Created, "ID_User": ID_User, "Completed": Completed, "Code": Code, "ID_Person": ID_Person, "IsCatalog": IsCatalog, "IsGa": IsGa, "ID_ContactRequestType": ID_ContactRequestType, "ContactRequestType": ContactRequestType, "Person": Person, "ID_ContactType": ID_ContactType, "ContactType": ContactType, "Value": Value, "Note": Note})

    # Nastavit viditelnost kontaktu
    def PersonContactUpdateHide(self, ID_Login, ID, IsHidden):
        return self._client.service.PersonContactUpdateHide({"ID_Login": ID_Login, "ID": ID, "IsHidden": IsHidden})

    # Načtení informací o datech pro změnu
    def PersonDetailPersonChange(self, ID_Login, ID_Application, Code):
        return self._client.service.PersonDetailPersonChange({"ID_Login": ID_Login, "ID_Application": ID_Application, "Code": Code})

