# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s akcemi (sněmy apod.)
class Events(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Events.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Events.asmx?wsdl')

    # Načíst seznam táborů
    def EventCampAll(self, IsFuture, IsRelation, IsChildDirect, IsChildUnit, ID_Login, ID_Unit, Started, Year, ForEvaluation, DisplayName=None, ID_EventCampState=None, RegistrationNumber=None, Location=None):
        return self._client.service.EventCampAll({"IsFuture": IsFuture, "IsRelation": IsRelation, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "ID_Login": ID_Login, "ID_Unit": ID_Unit, "Started": Started, "Year": Year, "ForEvaluation": ForEvaluation, "DisplayName": DisplayName, "ID_EventCampState": ID_EventCampState, "RegistrationNumber": RegistrationNumber, "Location": Location})

    # Načíst detail tábora
    def EventCampDetail(self, ID_Login, ID):
        return self._client.service.EventCampDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit tábor
    def EventCampInsert(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampInsert({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Načíst seznam položek rozpočtu tábora
    def EventCampStatementAll(self, ID_Login, ID_EventCamp, IsEstimate, IsRevenue):
        return self._client.service.EventCampStatementAll({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "IsEstimate": IsEstimate, "IsRevenue": IsRevenue})

    # Smazat položku rozpočtu tábora
    def EventCampStatementDelete(self, ID_Login, ID, ID_EventCamp, IsRevenue, ID_EventCampStatementType, Ammount, IsEstimate, EventCampStatementType=None):
        return self._client.service.EventCampStatementDelete({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "IsRevenue": IsRevenue, "ID_EventCampStatementType": ID_EventCampStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventCampStatementType": EventCampStatementType})

    # Založit položku rozpočtu tábora
    def EventCampStatementInsert(self, ID_Login, ID, ID_EventCamp, IsRevenue, ID_EventCampStatementType, Ammount, IsEstimate, EventCampStatementType=None):
        return self._client.service.EventCampStatementInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "IsRevenue": IsRevenue, "ID_EventCampStatementType": ID_EventCampStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventCampStatementType": EventCampStatementType})

    # Upravit položku rozpočtu tábora
    def EventCampStatementUpdate(self, ID_Login, ID, ID_EventCamp, IsRevenue, ID_EventCampStatementType, Ammount, IsEstimate, EventCampStatementType=None):
        return self._client.service.EventCampStatementUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "IsRevenue": IsRevenue, "ID_EventCampStatementType": ID_EventCampStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventCampStatementType": EventCampStatementType})

    # Upravit počet účastníků v kategoriích
    def EventCampStatisticUpdate(self, ID_Login, ID, ID_EventCamp, IsEstimate, Benjaminci, Vlce, Svetluska, Skaut, Skautka, Rover, Ranger, AdultFemale, AdultMale):
        return self._client.service.EventCampStatisticUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "IsEstimate": IsEstimate, "Benjaminci": Benjaminci, "Vlce": Vlce, "Svetluska": Svetluska, "Skaut": Skaut, "Skautka": Skautka, "Rover": Rover, "Ranger": Ranger, "AdultFemale": AdultFemale, "AdultMale": AdultMale})

    # Načíst seznam přiřazení oddílů k táboru
    def EventCampUnitAll(self, ID_Login, ID_EventCamp, ID_Unit):
        return self._client.service.EventCampUnitAll({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "ID_Unit": ID_Unit})

    # Upravit tábor
    def EventCampUpdate(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Načíst vedení tábora
    def EventFunctionAllCamp(self, ID_Login, ID_EventCamp, ID_Person, ID_EventFunctionType):
        return self._client.service.EventFunctionAllCamp({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType})

    # Upravit funkci na akci
    def EventFunctionUpdate(self, ID_Login, ID, ID_Person, ID_EventFunctionType, Note=None):
        return self._client.service.EventFunctionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType, "Note": Note})

    # Načíst seznam účastníků tábora
    def ParticipantCampAll(self, ID_Login, ID_EventCamp, Estimate, Real):
        return self._client.service.ParticipantCampAll({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "Estimate": Estimate, "Real": Real})

    # Smazat účastníka tábora
    def ParticipantCampDelete(self, ID_Login, ID, DeletePerson):
        return self._client.service.ParticipantCampDelete({"ID_Login": ID_Login, "ID": ID, "DeletePerson": DeletePerson})

    # Načíst detail účastníka tábora
    def ParticipantCampDetail(self, ID_Login, ID):
        return self._client.service.ParticipantCampDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit účastníka tábora
    def ParticipantCampInsert(self, ID_Login, ID_EventCamp, ID_Person, Person=None):
        return self._client.service.ParticipantCampInsert({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "ID_Person": ID_Person, "Person": Person})

    # Načíst seznam delegátů z mé jednotky
    def DelegateAllPreference(self, ID_Login, ID_EventCongress):
        return self._client.service.DelegateAllPreference({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress})

    # Načíst seznam stavů delegátů
    def DelegateStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.DelegateStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam akcí osoby
    def EventAllPerson(self, ID_Login, ID_Person, ID_Unit, ID_EventType=None, DisplayName=None):
        return self._client.service.EventAllPerson({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_Unit": ID_Unit, "ID_EventType": ID_EventType, "DisplayName": DisplayName})

    # Odeslat zprávu delegátům
    def EventCongressMessageInsert(self, ID_Login, ID_EventCongress, ID_DelegateStateArray=None, Subject=None, Body=None, FileName=None, Content=None):
        return self._client.service.EventCongressMessageInsert({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_DelegateStateArray": ID_DelegateStateArray, "Subject": Subject, "Body": Body, "FileName": FileName, "Content": Content})

    # Vygenerování tiskové sestavy 'Všichni účastníci sněmu' ve formátu CSV
    def EventCongressReportParticipant(self, ID_Login, ID):
        return self._client.service.EventCongressReportParticipant({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail akce
    def EventDetail(self, ID_Login, ID):
        return self._client.service.EventDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam typů jídel
    def FoodAll(self, ID_Login, ID_EventCongress, DisplayName=None):
        return self._client.service.FoodAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "DisplayName": DisplayName})

    # Smazat typ jídla
    def FoodDelete(self, ID_Login, ID):
        return self._client.service.FoodDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail typu jídla
    def FoodDetail(self, ID_Login, ID):
        return self._client.service.FoodDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit typ jídla
    def FoodInsert(self, ID_Login, ID, ID_EventCongress, Day, DisplayName=None):
        return self._client.service.FoodInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "Day": Day, "DisplayName": DisplayName})

    # Načíst seznam jídel
    def FoodMenuAll(self, ID_Login, ID_Food, ID_PersonFree, DisplayName=None):
        return self._client.service.FoodMenuAll({"ID_Login": ID_Login, "ID_Food": ID_Food, "ID_PersonFree": ID_PersonFree, "DisplayName": DisplayName})

    # Smazat jídlo
    def FoodMenuDelete(self, ID_Login, ID):
        return self._client.service.FoodMenuDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit jídlo
    def FoodMenuInsert(self, ID_Login, ID, ID_Food, Capacity, DisplayName=None):
        return self._client.service.FoodMenuInsert({"ID_Login": ID_Login, "ID": ID, "ID_Food": ID_Food, "Capacity": Capacity, "DisplayName": DisplayName})

    # Upravit jídlo
    def FoodMenuUpdate(self, ID_Login, ID, ID_Food, Capacity, DisplayName=None):
        return self._client.service.FoodMenuUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Food": ID_Food, "Capacity": Capacity, "DisplayName": DisplayName})

    # Upravit typ jídla
    def FoodUpdate(self, ID_Login, ID, ID_EventCongress, Day, DisplayName=None):
        return self._client.service.FoodUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "Day": Day, "DisplayName": DisplayName})

    # Smazat účastníka VSJ
    def ParticipantDeleteUstredi(self, ID_Login, ID, DeletePerson):
        return self._client.service.ParticipantDeleteUstredi({"ID_Login": ID_Login, "ID": ID, "DeletePerson": DeletePerson})

    # Načíst detail účastníka VSJ
    def ParticipantDetailUstredi(self, ID_Login, ID):
        return self._client.service.ParticipantDetailUstredi({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam krajů
    def RegionAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.RegionAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam účastníků VSJ
    def ParticipantAllUstredi(self, ID_Login, ID_EventCongress, HasPreference, ID_ParticipantType=None, Person=None):
        return self._client.service.ParticipantAllUstredi({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "HasPreference": HasPreference, "ID_ParticipantType": ID_ParticipantType, "Person": Person})

    # Založit účastníka VSJ
    def ParticipantInsertUstredi(self, ID_Login, ID_EventCongress, ID_Person, ID_ParticipantType=None, Person=None, Note=None):
        return self._client.service.ParticipantInsertUstredi({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "ID_ParticipantType": ID_ParticipantType, "Person": Person, "Note": Note})

    # Načíst poplatek účastníka akce
    def ParticipantFee(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.ParticipantFee({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Načíst seznam ubytování osoby
    def PersonAccommodationAll(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.PersonAccommodationAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Upravit ubytování osoby
    def PersonAccommodationUpdate(self, ID_Login, ID_EventCongress, ID_Person, Day, ID_Accommodation, Note=None):
        return self._client.service.PersonAccommodationUpdate({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "Day": Day, "ID_Accommodation": ID_Accommodation, "Note": Note})

    # Nevyplněné údaje účastníka sněmu
    def ParticipantPreference(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.ParticipantPreference({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Načíst seznam jídel osoby
    def PersonFoodAll(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.PersonFoodAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Upravit jídlo osoby
    def PersonFoodUpdate(self, ID_Login, ID_EventCongress, ID_Person, ID_Food, ID_FoodMenu, Note=None):
        return self._client.service.PersonFoodUpdate({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "ID_Food": ID_Food, "ID_FoodMenu": ID_FoodMenu, "Note": Note})

    # Číselník možných příjezdů a odjezdů
    def PersonPreferenceDateList(self, ID_Login, ID_EventCongress, IsArrive):
        return self._client.service.PersonPreferenceDateList({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "IsArrive": IsArrive})

    # Načíst preference osoby pro odjezd
    def PersonPreferenceDetailDeparture(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.PersonPreferenceDetailDeparture({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Upravit preference osoby pro odjezd
    def PersonPreferenceUpdateDeparture(self, ID_Login, ID_EventCongress, ID_Person, Departure, NoDeparture, EventCongress=None, Person=None, DisplayName=None):
        return self._client.service.PersonPreferenceUpdateDeparture({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "Departure": Departure, "NoDeparture": NoDeparture, "EventCongress": EventCongress, "Person": Person, "DisplayName": DisplayName})

    # Upravit preference osoby pro příjezd
    def PersonPreferenceUpdateArrive(self, ID_Login, ID_EventCongress, ID_Person, Arrive, NoArrive, EventCongress=None, Person=None, DisplayName=None):
        return self._client.service.PersonPreferenceUpdateArrive({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "Arrive": Arrive, "NoArrive": NoArrive, "EventCongress": EventCongress, "Person": Person, "DisplayName": DisplayName})

    # Načíst preference osoby pro příjezd
    def PersonPreferenceDetailArrive(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.PersonPreferenceDetailArrive({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Načíst seznam osob, které zúčastní sněmu
    def ParticipantAllPerson(self, ID_Login, ID_EventCongress, ID, DisplayName=None):
        return self._client.service.ParticipantAllPerson({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam typů účastníků
    def ParticipantTypeAll(self, ID_Login, IsManual, DisplayName=None, ID_EventType=None):
        return self._client.service.ParticipantTypeAll({"ID_Login": ID_Login, "IsManual": IsManual, "DisplayName": DisplayName, "ID_EventType": ID_EventType})

    # Načíst preference osoby pro dopravu
    def PersonPreferenceDetailTransport(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.PersonPreferenceDetailTransport({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Upravit preference osoby pro dopravu
    def PersonPreferenceUpdateTransport(self, ID_Login, ID_EventCongress, ID_Person, ID_Transport, NoTransport, Transport=None, EventCongress=None, Person=None):
        return self._client.service.PersonPreferenceUpdateTransport({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "ID_Transport": ID_Transport, "NoTransport": NoTransport, "Transport": Transport, "EventCongress": EventCongress, "Person": Person})

    # Načíst seznam dopravních prostředků
    def TransportAll(self, ID_Login, DisplayName=None):
        return self._client.service.TransportAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam kandidátů na pozici
    def CandidateAll(self, ID_Login, ID_EventCongress, ID_Person, ID_CandidateWith, ID_EventCongressFunction, IsAudit, IsOther, IsDelegate, ID_CandidateState=None):
        return self._client.service.CandidateAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "ID_CandidateWith": ID_CandidateWith, "ID_EventCongressFunction": ID_EventCongressFunction, "IsAudit": IsAudit, "IsOther": IsOther, "IsDelegate": IsDelegate, "ID_CandidateState": ID_CandidateState})

    # Načíst seznam kontaktů kandidáta
    def CandidateContactAll(self, ID_Login, ID_Candidate, ID_PersonContact):
        return self._client.service.CandidateContactAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "ID_PersonContact": ID_PersonContact})

    # Smazat kandidáta na pozici
    def CandidateDelete(self, ID_Login, ID):
        return self._client.service.CandidateDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail kandidáta na pozici
    def CandidateDetail(self, ID_Login, ID, ConvertToRtf):
        return self._client.service.CandidateDetail({"ID_Login": ID_Login, "ID": ID, "ConvertToRtf": ConvertToRtf})

    # Načíst seznam vzdělávacích akcí kandidáta
    def CandidateEducationSeminaryAll(self, ID_Login, ID_Candidate, ID_EducationSeminary):
        return self._client.service.CandidateEducationSeminaryAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "ID_EducationSeminary": ID_EducationSeminary})

    # Načíst seznam funkcí kandidáta
    def CandidateFunctionAll(self, ID_Login, ID_Candidate, ID_Function):
        return self._client.service.CandidateFunctionAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "ID_Function": ID_Function})

    # Založit kandidáta na pozici
    def CandidateInsert(self, ID_Login, ID, ID_EventCongress, ID_UserCreate, ID_PersonCreate, DateCreate, ID_Person, ID_CandidateWith, ID_EventCongressFunction, IsCandidateWith, VotesCount, Order, IsElected, AttachmentContent=None, DisplayName=None, EventCongress=None, ID_CandidateState=None, CandidateState=None, StateDecision=None, PersonCreate=None, Person=None, PersonWith=None, EventCongressFunction=None, FunctionType=None, AttachmentExtension=None, Career=None, SuggesterName=None, SuggesterFunction=None, SuggesterDescription=None, Presentation=None, Success=None, Agenda=None, Problems=None, MainTask=None, Unit=None, ID_UnitType=None, Contacts=None, EducationSeminars=None, Functions=None, Qualifications=None, Recommendations=None, Members=None):
        return self._client.service.CandidateInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_UserCreate": ID_UserCreate, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_Person": ID_Person, "ID_CandidateWith": ID_CandidateWith, "ID_EventCongressFunction": ID_EventCongressFunction, "IsCandidateWith": IsCandidateWith, "VotesCount": VotesCount, "Order": Order, "IsElected": IsElected, "AttachmentContent": AttachmentContent, "DisplayName": DisplayName, "EventCongress": EventCongress, "ID_CandidateState": ID_CandidateState, "CandidateState": CandidateState, "StateDecision": StateDecision, "PersonCreate": PersonCreate, "Person": Person, "PersonWith": PersonWith, "EventCongressFunction": EventCongressFunction, "FunctionType": FunctionType, "AttachmentExtension": AttachmentExtension, "Career": Career, "SuggesterName": SuggesterName, "SuggesterFunction": SuggesterFunction, "SuggesterDescription": SuggesterDescription, "Presentation": Presentation, "Success": Success, "Agenda": Agenda, "Problems": Problems, "MainTask": MainTask, "Unit": Unit, "ID_UnitType": ID_UnitType, "Contacts": Contacts, "EducationSeminars": EducationSeminars, "Functions": Functions, "Qualifications": Qualifications, "Recommendations": Recommendations, "Members": Members})

    # Načíst seznam členství v politických stranách a dalších organizacích
    def CandidateMemberAll(self, ID_Login, ID_Candidate, DisplayName=None):
        return self._client.service.CandidateMemberAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "DisplayName": DisplayName})

    # Načíst seznam kvalifikací kandidáta
    def CandidateQualificationAll(self, ID_Login, ID_Candidate, ID_Qualification):
        return self._client.service.CandidateQualificationAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "ID_Qualification": ID_Qualification})

    # Načíst seznam doporučení kandidáta
    def CandidateRecommendationAll(self, ID_Login, ID_Candidate, DisplayName=None):
        return self._client.service.CandidateRecommendationAll({"ID_Login": ID_Login, "ID_Candidate": ID_Candidate, "DisplayName": DisplayName})

    # Upravit kandidáta na pozici
    def CandidateUpdate(self, ID_Login, ID, ID_EventCongress, ID_UserCreate, ID_PersonCreate, DateCreate, ID_Person, ID_CandidateWith, ID_EventCongressFunction, IsCandidateWith, VotesCount, Order, IsElected, AttachmentContent=None, DisplayName=None, EventCongress=None, ID_CandidateState=None, CandidateState=None, StateDecision=None, PersonCreate=None, Person=None, PersonWith=None, EventCongressFunction=None, FunctionType=None, AttachmentExtension=None, Career=None, SuggesterName=None, SuggesterFunction=None, SuggesterDescription=None, Presentation=None, Success=None, Agenda=None, Problems=None, MainTask=None, Unit=None, ID_UnitType=None, Contacts=None, EducationSeminars=None, Functions=None, Qualifications=None, Recommendations=None, Members=None):
        return self._client.service.CandidateUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_UserCreate": ID_UserCreate, "ID_PersonCreate": ID_PersonCreate, "DateCreate": DateCreate, "ID_Person": ID_Person, "ID_CandidateWith": ID_CandidateWith, "ID_EventCongressFunction": ID_EventCongressFunction, "IsCandidateWith": IsCandidateWith, "VotesCount": VotesCount, "Order": Order, "IsElected": IsElected, "AttachmentContent": AttachmentContent, "DisplayName": DisplayName, "EventCongress": EventCongress, "ID_CandidateState": ID_CandidateState, "CandidateState": CandidateState, "StateDecision": StateDecision, "PersonCreate": PersonCreate, "Person": Person, "PersonWith": PersonWith, "EventCongressFunction": EventCongressFunction, "FunctionType": FunctionType, "AttachmentExtension": AttachmentExtension, "Career": Career, "SuggesterName": SuggesterName, "SuggesterFunction": SuggesterFunction, "SuggesterDescription": SuggesterDescription, "Presentation": Presentation, "Success": Success, "Agenda": Agenda, "Problems": Problems, "MainTask": MainTask, "Unit": Unit, "ID_UnitType": ID_UnitType, "Contacts": Contacts, "EducationSeminars": EducationSeminars, "Functions": Functions, "Qualifications": Qualifications, "Recommendations": Recommendations, "Members": Members})

    # Stáhne program kandidáta
    def CandidateAttachmentDownload(self, ID_Login, ID):
        return self._client.service.CandidateAttachmentDownload({"ID_Login": ID_Login, "ID": ID})

    # Načíst informace o kandidující osobě
    def CandidateDetailPerson(self, ID):
        return self._client.service.CandidateDetailPerson(ID=ID)

    # Načíst informace o osobě při založení/editaci kandidatury
    def CandidateDetailEditPerson(self, ID_Login, ID, ID_EventCongressFunction, ID_Person):
        return self._client.service.CandidateDetailEditPerson({"ID_Login": ID_Login, "ID": ID, "ID_EventCongressFunction": ID_EventCongressFunction, "ID_Person": ID_Person})

    # Označit kandidáta jako předsedu revizní komise
    def CandidateUpdateAuditLeader(self, ID_Login, ID):
        return self._client.service.CandidateUpdateAuditLeader({"ID_Login": ID_Login, "ID": ID})

    # Nastavit kvótu pro výpočet delegátů
    def EventCongressUpdateQuota(self, ID_Login, ID, DelegateQuota):
        return self._client.service.EventCongressUpdateQuota({"ID_Login": ID_Login, "ID": ID, "DelegateQuota": DelegateQuota})

    # Načíst detail delegáta
    def DelegateDetail(self, ID_Login, ID):
        return self._client.service.DelegateDetail({"ID_Login": ID_Login, "ID": ID})

    # Odhlášení delegáta
    def DelegateUpdate(self, ID_Login, ID, ID_Participant, ID_Candidate, ID_Person, ID_EventCongress, ID_DelegateState=None, DelegateState=None, CancelDescription=None, Person=None, EventCongress=None):
        return self._client.service.DelegateUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Participant": ID_Participant, "ID_Candidate": ID_Candidate, "ID_Person": ID_Person, "ID_EventCongress": ID_EventCongress, "ID_DelegateState": ID_DelegateState, "DelegateState": DelegateState, "CancelDescription": CancelDescription, "Person": Person, "EventCongress": EventCongress})

    # Načíst seznam sněmů
    def EventCongressAllChild(self, ID_Login, ID):
        return self._client.service.EventCongressAllChild({"ID_Login": ID_Login, "ID": ID})

    # Změnit stav sněmu
    def EventCongressUpdateState(self, ID_Login, ID, ID_EventCongressState=None):
        return self._client.service.EventCongressUpdateState({"ID_Login": ID_Login, "ID": ID, "ID_EventCongressState": ID_EventCongressState})

    # Načíst seznam delegátů
    def DelegateAll(self, ID_Login, ID_EventCongress, ID_Participant, ID_Candidate, IsCandidate, ID_DelegateState=None, Person=None, RegistrationNumber=None):
        return self._client.service.DelegateAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Participant": ID_Participant, "ID_Candidate": ID_Candidate, "IsCandidate": IsCandidate, "ID_DelegateState": ID_DelegateState, "Person": Person, "RegistrationNumber": RegistrationNumber})

    # Zaslat upomínky informující o chybějící kandidátní komisi
    def EventCongressCommissionReminder(self, ID_Login):
        return self._client.service.EventCongressCommissionReminder({"ID_Login": ID_Login})

    # Načíst počet delegátů sněmu
    def EventCongressDetailDelegate(self, ID_Login, ID):
        return self._client.service.EventCongressDetailDelegate({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam typů funkcí, na které lze kandidovat
    def EventCongressFunctionALLType(self, ID_Login, ID_Unit, ID_EventCongress, ID_FunctionType):
        return self._client.service.EventCongressFunctionALLType({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_EventCongress": ID_EventCongress, "ID_FunctionType": ID_FunctionType})

    # Upravit kandidáta na pozici
    def CandidateUpdateState(self, ID_Login, ID, ID_CandidateState=None, StateDecision=None):
        return self._client.service.CandidateUpdateState({"ID_Login": ID_Login, "ID": ID, "ID_CandidateState": ID_CandidateState, "StateDecision": StateDecision})

    # Zadat výsledek volby
    def CandidateUpdateVote(self, ID_Login, ID, VotesCount, IsElected, OrderIncrease):
        return self._client.service.CandidateUpdateVote({"ID_Login": ID_Login, "ID": ID, "VotesCount": VotesCount, "IsElected": IsElected, "OrderIncrease": OrderIncrease})

    # Načíst seznam kandidátů na pozici
    def CandidateAllStatutory(self, ID_Login, ID_EventCongress):
        return self._client.service.CandidateAllStatutory({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress})

    # Načíst seznam schválených kandidátů sněmu
    def CandidateAllApproved(self, ID_Login, ID_EventCongress):
        return self._client.service.CandidateAllApproved({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress})

    # Načíst seznam možných spolukandidátů
    def CandidateAllName(self, ID_Login, ID_EventCongressFunction, ID_Candidate):
        return self._client.service.CandidateAllName({"ID_Login": ID_Login, "ID_EventCongressFunction": ID_EventCongressFunction, "ID_Candidate": ID_Candidate})

    # Načíst počty členů kandidátní komise
    def EventCongressCommissionCount(self, ID_Login, ID):
        return self._client.service.EventCongressCommissionCount({"ID_Login": ID_Login, "ID": ID})

    # Vytvořit zvolené funkce
    def EventCongressCreateFunctions(self, ID_Login, ID):
        return self._client.service.EventCongressCreateFunctions({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam funkcí, na které lze kandidovat
    def EventCongressFunctionAllCandidate(self, ID_Login, OnlyMyUnit):
        return self._client.service.EventCongressFunctionAllCandidate({"ID_Login": ID_Login, "OnlyMyUnit": OnlyMyUnit})

    # Načíst detail volené funkce
    def EventCongressFunctionDetail(self, ID_Login, ID):
        return self._client.service.EventCongressFunctionDetail({"ID_Login": ID_Login, "ID": ID})

    # Vložit zápis ze sněmu
    def EventCongressProtocolUpload(self, ID_Login, ID, ProtocolExtension=None, ProtocolContent=None):
        return self._client.service.EventCongressProtocolUpload({"ID_Login": ID_Login, "ID": ID, "ProtocolExtension": ProtocolExtension, "ProtocolContent": ProtocolContent})

    # Načte balík šablon dokumentů sněmu
    def EventCongressDocumentTemplates(self, ID_Login, ID):
        return self._client.service.EventCongressDocumentTemplates({"ID_Login": ID_Login, "ID": ID})

    # Stáhne zápis ze sněmu
    def EventCongressProtocolDownload(self, ID_Login, ID):
        return self._client.service.EventCongressProtocolDownload({"ID_Login": ID_Login, "ID": ID})

    # Rozeslat oznámení o sestavení komise
    def EventCongressSendComissionMessage(self, ID_Login, ID):
        return self._client.service.EventCongressSendComissionMessage({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam členů kandidátní komise
    def EventCongressCommissionAll(self, ID_Login, ID_EventCongress, ID_Person):
        return self._client.service.EventCongressCommissionAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person})

    # Smazat člena kandidátní komise
    def EventCongressCommissionDelete(self, ID_Login, ID):
        return self._client.service.EventCongressCommissionDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit člena kandidátní komise
    def EventCongressCommissionInsert(self, ID_Login, ID, ID_EventCongress, ID_Person, IsLeader):
        return self._client.service.EventCongressCommissionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "IsLeader": IsLeader})

    # Upravit člena kandidátní komise
    def EventCongressCommissionUpdate(self, ID_Login, ID, ID_EventCongress, ID_Person, IsLeader):
        return self._client.service.EventCongressCommissionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "IsLeader": IsLeader})

    # Načíst seznam sněmů
    def EventCongressAll(self, ID_Login, ID_Unit, IsFuture, IsParticipant, IsUnit, IsChildDirect, IsChildUnit, DisplayName=None, ID_EventCongressType=None, ID_UnitType=None, ID_EventCongressState=None):
        return self._client.service.EventCongressAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "IsFuture": IsFuture, "IsParticipant": IsParticipant, "IsUnit": IsUnit, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "DisplayName": DisplayName, "ID_EventCongressType": ID_EventCongressType, "ID_UnitType": ID_UnitType, "ID_EventCongressState": ID_EventCongressState})

    # Načíst detail sněmu
    def EventCongressDetail(self, ID_Login, ID):
        return self._client.service.EventCongressDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam volených funkcí
    def EventCongressFunctionAll(self, ID_Login, ID, ID_EventCongress, ID_FunctionType):
        return self._client.service.EventCongressFunctionAll({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_FunctionType": ID_FunctionType})

    # Založit volenou funkci
    def EventCongressFunctionInsert(self, ID_Login, ID, ID_EventCongress, ID_FunctionType, ID_Unit, IsCandidateWith, HasPassed, DisplayName=None, EventCongress=None, ID_UnitType=None, FunctionType=None, ID_EventCongressState=None):
        return self._client.service.EventCongressFunctionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "ID_FunctionType": ID_FunctionType, "ID_Unit": ID_Unit, "IsCandidateWith": IsCandidateWith, "HasPassed": HasPassed, "DisplayName": DisplayName, "EventCongress": EventCongress, "ID_UnitType": ID_UnitType, "FunctionType": FunctionType, "ID_EventCongressState": ID_EventCongressState})

    # Založit sněm
    def EventCongressInsert(self, ID_Login, ID, ID_Event, ID_UnitRegistration, PromulgationDeadline, CommissionDeadline, CandidateDeadline, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, AlternateStartDate, AlternateEndDate, AlternateGpsLatitude, AlternateGpsLongitude, CandidateAfterDeadline, ArriveDeadline, DepartureDeadline, TransportDeadline, AccommodationDeadline, FoodDeadline, ParticipantFee, ID_TempFileSimplifiedEntryExtension, Event=None, UnitRegistration=None, ID_EventCongressType=None, EventCongressType=None, ID_EventCongressState=None, EventCongressState=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Location=None, AlternateLocation=None, Note=None, ProtocolExtension=None, ProtocolContent=None, FunctionAgreementExtension=None, SimplifiedEntryExtension=None, SimplifiedEntryTemplateExtension=None):
        return self._client.service.EventCongressInsert({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_UnitRegistration": ID_UnitRegistration, "PromulgationDeadline": PromulgationDeadline, "CommissionDeadline": CommissionDeadline, "CandidateDeadline": CandidateDeadline, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "AlternateStartDate": AlternateStartDate, "AlternateEndDate": AlternateEndDate, "AlternateGpsLatitude": AlternateGpsLatitude, "AlternateGpsLongitude": AlternateGpsLongitude, "CandidateAfterDeadline": CandidateAfterDeadline, "ArriveDeadline": ArriveDeadline, "DepartureDeadline": DepartureDeadline, "TransportDeadline": TransportDeadline, "AccommodationDeadline": AccommodationDeadline, "FoodDeadline": FoodDeadline, "ParticipantFee": ParticipantFee, "ID_TempFileSimplifiedEntryExtension": ID_TempFileSimplifiedEntryExtension, "Event": Event, "UnitRegistration": UnitRegistration, "ID_EventCongressType": ID_EventCongressType, "EventCongressType": EventCongressType, "ID_EventCongressState": ID_EventCongressState, "EventCongressState": EventCongressState, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Location": Location, "AlternateLocation": AlternateLocation, "Note": Note, "ProtocolExtension": ProtocolExtension, "ProtocolContent": ProtocolContent, "FunctionAgreementExtension": FunctionAgreementExtension, "SimplifiedEntryExtension": SimplifiedEntryExtension, "SimplifiedEntryTemplateExtension": SimplifiedEntryTemplateExtension})

    # Načíst seznam typů sněmu
    def EventCongressTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventCongressTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit sněm
    def EventCongressUpdate(self, ID_Login, ID, ID_Event, ID_UnitRegistration, PromulgationDeadline, CommissionDeadline, CandidateDeadline, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, AlternateStartDate, AlternateEndDate, AlternateGpsLatitude, AlternateGpsLongitude, CandidateAfterDeadline, ArriveDeadline, DepartureDeadline, TransportDeadline, AccommodationDeadline, FoodDeadline, ParticipantFee, ID_TempFileSimplifiedEntryExtension, Event=None, UnitRegistration=None, ID_EventCongressType=None, EventCongressType=None, ID_EventCongressState=None, EventCongressState=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Location=None, AlternateLocation=None, Note=None, ProtocolExtension=None, ProtocolContent=None, FunctionAgreementExtension=None, SimplifiedEntryExtension=None, SimplifiedEntryTemplateExtension=None):
        return self._client.service.EventCongressUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_UnitRegistration": ID_UnitRegistration, "PromulgationDeadline": PromulgationDeadline, "CommissionDeadline": CommissionDeadline, "CandidateDeadline": CandidateDeadline, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "AlternateStartDate": AlternateStartDate, "AlternateEndDate": AlternateEndDate, "AlternateGpsLatitude": AlternateGpsLatitude, "AlternateGpsLongitude": AlternateGpsLongitude, "CandidateAfterDeadline": CandidateAfterDeadline, "ArriveDeadline": ArriveDeadline, "DepartureDeadline": DepartureDeadline, "TransportDeadline": TransportDeadline, "AccommodationDeadline": AccommodationDeadline, "FoodDeadline": FoodDeadline, "ParticipantFee": ParticipantFee, "ID_TempFileSimplifiedEntryExtension": ID_TempFileSimplifiedEntryExtension, "Event": Event, "UnitRegistration": UnitRegistration, "ID_EventCongressType": ID_EventCongressType, "EventCongressType": EventCongressType, "ID_EventCongressState": ID_EventCongressState, "EventCongressState": EventCongressState, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Location": Location, "AlternateLocation": AlternateLocation, "Note": Note, "ProtocolExtension": ProtocolExtension, "ProtocolContent": ProtocolContent, "FunctionAgreementExtension": FunctionAgreementExtension, "SimplifiedEntryExtension": SimplifiedEntryExtension, "SimplifiedEntryTemplateExtension": SimplifiedEntryTemplateExtension})

    # Načíst detail umístění vzdělávací akce
    def EventEducationLocationDetail(self, ID_Login, ID):
        return self._client.service.EventEducationLocationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit umístění vzdělávací akce
    def EventEducationLocationInsert(self, ID_Login, ID, IsActive, ID_EventEducation, ID_Region, Latitude, Longitude, DisplayName=None, Region=None, Street=None, Postcode=None, City=None, Note=None, FirstLine=None):
        return self._client.service.EventEducationLocationInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_Region": ID_Region, "Latitude": Latitude, "Longitude": Longitude, "DisplayName": DisplayName, "Region": Region, "Street": Street, "Postcode": Postcode, "City": City, "Note": Note, "FirstLine": FirstLine})

    # Upravit umístění vzdělávací akce
    def EventEducationLocationUpdate(self, ID_Login, ID, IsActive, ID_EventEducation, ID_Region, Latitude, Longitude, DisplayName=None, Region=None, Street=None, Postcode=None, City=None, Note=None, FirstLine=None):
        return self._client.service.EventEducationLocationUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_Region": ID_Region, "Latitude": Latitude, "Longitude": Longitude, "DisplayName": DisplayName, "Region": Region, "Street": Street, "Postcode": Postcode, "City": City, "Note": Note, "FirstLine": FirstLine})

    # Načíst ilustrační fotografie z dalších údajů VzA
    def EventEducationOtherDetailPhotos(self, ID_Login, ID_Application, ID_EventEducation, ID_EventEducationCourse, Variant, Size=None):
        return self._client.service.EventEducationOtherDetailPhotos({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "Variant": Variant, "Size": Size})

    # No documentation
    def EventEducationStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.EventEducationStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam termínů vzdělávací akce
    def EventEducationTermAll(self, ID_Login, ID_EventEducation, ID, ID_EventEducationLocation, Year, DisplayName=None):
        return self._client.service.EventEducationTermAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "ID_EventEducationLocation": ID_EventEducationLocation, "Year": Year, "DisplayName": DisplayName})

    # Smazat termín vzdělávací akce
    def EventEducationTermDelete(self, ID_Login, ID):
        return self._client.service.EventEducationTermDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail termínu vzdělávací akce
    def EventEducationTermDetail(self, ID_Login, ID):
        return self._client.service.EventEducationTermDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit termín vzdělávací akce
    def EventEducationTermInsert(self, ID_Login, ID, IsActive, ID_EventEducation, ID_EventEducationLocation, DateFrom, DateTo, IsRealParticipationSet, DisplayName=None, EventEducationLocation=None, Note=None):
        return self._client.service.EventEducationTermInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_EventEducationLocation": ID_EventEducationLocation, "DateFrom": DateFrom, "DateTo": DateTo, "IsRealParticipationSet": IsRealParticipationSet, "DisplayName": DisplayName, "EventEducationLocation": EventEducationLocation, "Note": Note})

    # No documentation
    def EventEducationTermUpdate(self, ID_Login, ID, IsActive, ID_EventEducation, ID_EventEducationLocation, DateFrom, DateTo, IsRealParticipationSet, DisplayName=None, EventEducationLocation=None, Note=None):
        return self._client.service.EventEducationTermUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_EventEducationLocation": ID_EventEducationLocation, "DateFrom": DateFrom, "DateTo": DateTo, "IsRealParticipationSet": IsRealParticipationSet, "DisplayName": DisplayName, "EventEducationLocation": EventEducationLocation, "Note": Note})

    # Načíst seznam typů vzdělávacích akcí a poskytnout URL
    def EventEducationTypeAllCalendarURLPublic(self, ID_Login, ID_Application):
        return self._client.service.EventEducationTypeAllCalendarURLPublic({"ID_Login": ID_Login, "ID_Application": ID_Application})

    # Načíst seznam typů vzdělávacích akcí
    def EventEducationTypeAll(self, ID_Login, ID, IsQualificationExam, ID_EventEducationGroup=None, DisplayName=None):
        return self._client.service.EventEducationTypeAll({"ID_Login": ID_Login, "ID": ID, "IsQualificationExam": IsQualificationExam, "ID_EventEducationGroup": ID_EventEducationGroup, "DisplayName": DisplayName})

    # Načíst detail typu vzdělávací akce
    def EventEducationTypeDetail(self, ID_Login, ID):
        return self._client.service.EventEducationTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Schválit závěrečnou zprávu
    def EventEducationUpdateFinalReportConfirm(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateFinalReportConfirm({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Vrátit závěrečnou zprávu k dopracování
    def EventEducationUpdateFinalReportCancel(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateFinalReportCancel({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Schválit projekt
    def EventEducationUpdateProjectConfirm(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateProjectConfirm({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Vrátit projekt k přepracování
    def EventEducationUpdateProjectCancel(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateProjectCancel({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Zveřejnit vzdělávací akci
    def EventEducationUpdatePublicize(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdatePublicize({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Odmítnout schválení vodní akce
    def EventEducationUpdateWaterDisapprove(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateWaterDisapprove({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Odmítnout schválení vzdělávací akce
    def EventEducationUpdateDisapprove(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateDisapprove({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Schválit vodní akci
    def EventEducationUpdateWaterApprove(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateWaterApprove({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Schválit vzdělávací akci
    def EventEducationUpdateApprove(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateApprove({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit závěrečnou zprávu vzdělávací akce
    def EventEducationUpdateFinalReport(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateFinalReport({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit projekt vzdělávací akce
    def EventEducationUpdateProject(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateProject({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit vzdělávací akci
    def EventEducationUpdate(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdate({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit vedení vzdělávací akce
    def EventEducationUpdateLeader(self, ID_Login, ID, ID_PersonLeader, ID_PersonSecretary, ID_PersonEconomist, ID_PersonMedic, LeaderNote=None, SecretaryNote=None, EconomistNote=None, MedicNote=None):
        return self._client.service.EventEducationUpdateLeader({"ID_Login": ID_Login, "ID": ID, "ID_PersonLeader": ID_PersonLeader, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "ID_PersonMedic": ID_PersonMedic, "LeaderNote": LeaderNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "MedicNote": MedicNote})

    # Zkontrolovat projekt vzdělávací akce před odevzdáním
    def EventEducationProjectFinalCheck(self, ID_Login, ID, ShowValid):
        return self._client.service.EventEducationProjectFinalCheck({"ID_Login": ID_Login, "ID": ID, "ShowValid": ShowValid})

    # Potvrdit vzdělávací akci
    def EventEducationUpdateConfirm(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateConfirm({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Nahlásit vzdělávací akci
    def EventEducationUpdatePublish(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdatePublish({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Načíst zástupce vedoucího vzdělávací akce
    def EventFunctionAllEducationAssistant(self, ID_Login, ID_EventEducation, ID_Person):
        return self._client.service.EventFunctionAllEducationAssistant({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person})

    # Načíst vedení vzdělávací akce
    def EventFunctionAllEducationLeader(self, ID_Login, ID_EventEducation, ID_Person, ID_EventFunctionType):
        return self._client.service.EventFunctionAllEducationLeader({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType})

    # Smazat zástupce vedoucího vzdělávací akce
    def EventFunctionDeleteEducationAssistant(self, ID_Login, ID):
        return self._client.service.EventFunctionDeleteEducationAssistant({"ID_Login": ID_Login, "ID": ID})

    # Vložit zástupce vedoucího vzdělávací akce
    def EventFunctionInsertEducationAssistant(self, ID_Login, ID, ID_Event, ID_EventEducation, ID_Person, ID_EventFunctionType, HealthQualification, HealthQualificationDate, Event=None, Person=None, EventFunctionType=None, Note=None):
        return self._client.service.EventFunctionInsertEducationAssistant({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType, "HealthQualification": HealthQualification, "HealthQualificationDate": HealthQualificationDate, "Event": Event, "Person": Person, "EventFunctionType": EventFunctionType, "Note": Note})

    # Upravit zástupce vedoucího vzdělávací akce
    def EventFunctionUpdateEducationAssistant(self, ID_Login, ID, ID_Event, ID_EventEducation, ID_Person, ID_EventFunctionType, HealthQualification, HealthQualificationDate, Event=None, Person=None, EventFunctionType=None, Note=None):
        return self._client.service.EventFunctionUpdateEducationAssistant({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType, "HealthQualification": HealthQualification, "HealthQualificationDate": HealthQualificationDate, "Event": Event, "Person": Person, "EventFunctionType": EventFunctionType, "Note": Note})

    # No documentation
    def ParticipantEducationAllEventEducationExam(self, ID_Login, ID_EventEducationExam, ExcludeExisting):
        return self._client.service.ParticipantEducationAllEventEducationExam({"ID_Login": ID_Login, "ID_EventEducationExam": ID_EventEducationExam, "ExcludeExisting": ExcludeExisting})

    # No documentation
    def ParticipantEducationAll(self, ID_Login, ID_EventEducation, ID, ID_Participant, ShowPossibleGraduates, ShowSubstitutes, IsActive, ID_EventEducationCourse=None, ID_EventEducationType=None):
        return self._client.service.ParticipantEducationAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "ID_Participant": ID_Participant, "ShowPossibleGraduates": ShowPossibleGraduates, "ShowSubstitutes": ShowSubstitutes, "IsActive": IsActive, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_EventEducationType": ID_EventEducationType})

    # Smazat účastníka vzdělávací akce
    def ParticipantEducationDelete(self, ID_Login, ID, SignOutNote=None):
        return self._client.service.ParticipantEducationDelete({"ID_Login": ID_Login, "ID": ID, "SignOutNote": SignOutNote})

    # No documentation
    def ParticipantEducationDetail(self, ID_Login, ID, ID_EventEducation):
        return self._client.service.ParticipantEducationDetail({"ID_Login": ID_Login, "ID": ID, "ID_EventEducation": ID_EventEducation})

    # Načíst seznam účastníků zkoušek
    def ParticipantEducationExamAll(self, ID_Login, ID_EventEducationExam, ID, ID_Person, ID_ParticipantEducation):
        return self._client.service.ParticipantEducationExamAll({"ID_Login": ID_Login, "ID_EventEducationExam": ID_EventEducationExam, "ID": ID, "ID_Person": ID_Person, "ID_ParticipantEducation": ID_ParticipantEducation})

    # Smazat účastníka zkoušky
    def ParticipantEducationExamDelete(self, ID_Login, ID):
        return self._client.service.ParticipantEducationExamDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit účastníka zkoušky
    def ParticipantEducationExamInsert(self, ID_Login, ID, IsActive, ID_Person, ID_ParticipantEducation, DateExam, DateLetter, ID_EventEducationExam, LetterNumber=None):
        return self._client.service.ParticipantEducationExamInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_Person": ID_Person, "ID_ParticipantEducation": ID_ParticipantEducation, "DateExam": DateExam, "DateLetter": DateLetter, "ID_EventEducationExam": ID_EventEducationExam, "LetterNumber": LetterNumber})

    # Upravit účastníka zkoušky
    def ParticipantEducationExamUpdate(self, ID_Login, ID, IsActive, ID_Person, ID_ParticipantEducation, DateExam, DateLetter, ID_EventEducationExam, LetterNumber=None):
        return self._client.service.ParticipantEducationExamUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_Person": ID_Person, "ID_ParticipantEducation": ID_ParticipantEducation, "DateExam": DateExam, "DateLetter": DateLetter, "ID_EventEducationExam": ID_EventEducationExam, "LetterNumber": LetterNumber})

    # No documentation
    def ParticipantEducationInsert(self, ID_Login, ID_Person, ID_EventEducation, ID_EventEducationCourse, Person=None):
        return self._client.service.ParticipantEducationInsert({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "Person": Person})

    # Upravit účastníka vzdělávací akce
    def ParticipantEducationUpdate(self, ID_Login, ID, ID_Participant, ID_Person, ID_EventEducation, ID_EventEducationCourse, IsActive, FillCondition, IsSubstitute, IsAccepted, Graduated, DateLetterRequest, Person=None, ID_EventEducationType=None, EventEducationType=None, Note=None):
        return self._client.service.ParticipantEducationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Participant": ID_Participant, "ID_Person": ID_Person, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "IsActive": IsActive, "FillCondition": FillCondition, "IsSubstitute": IsSubstitute, "IsAccepted": IsAccepted, "Graduated": Graduated, "DateLetterRequest": DateLetterRequest, "Person": Person, "ID_EventEducationType": ID_EventEducationType, "EventEducationType": EventEducationType, "Note": Note})

    # Provedení kontroly všech příznaků VzA
    def EventConditionAllCheck(self, ID_Login):
        return self._client.service.EventConditionAllCheck({"ID_Login": ID_Login})

    # Načíst seznam stavů příznaku pro akci
    def EventConditionAll(self, ID_Login, ID_Event, ID, ID_User, ID_ConditionType=None):
        return self._client.service.EventConditionAll({"ID_Login": ID_Login, "ID_Event": ID_Event, "ID": ID, "ID_User": ID_User, "ID_ConditionType": ID_ConditionType})

    # Smazat stav příznaku pro akci
    def EventConditionDelete(self, ID_Login, ID):
        return self._client.service.EventConditionDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail stavu příznaku pro akci
    def EventConditionDetail(self, ID_Login, ID):
        return self._client.service.EventConditionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit stav příznaku pro akci
    def EventConditionInsert(self, ID_Login, ID, ID_Event, Date, ID_User, ID_ConditionType=None, Note=None):
        return self._client.service.EventConditionInsert({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "Date": Date, "ID_User": ID_User, "ID_ConditionType": ID_ConditionType, "Note": Note})

    # Načíst detail dalších údajů VzA
    def EventEducationOtherDetail(self, ID_Login, ID_EventEducation, ID_EventEducationCourse):
        return self._client.service.EventEducationOtherDetail({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse})

    # Upravit další údaje VzA
    def EventEducationOtherUpdate(self, ID_Login, ID, ID_EventEducation, ID_EventEducationCourse, IsForester, IsQualifyingExam, ParticipantFee, NextOccurrenceYear, Graduates, ID_TempFileIllustrativePhoto1, ID_TempFileIllustrativePhoto2, ID_TempFileIllustrativePhoto3, EventEducation=None, EventEducationCourse=None, Annotation=None, TargetGroup=None, EventFocus=None, EntryConditions=None, GraduateConditions=None, AuthenticationForm=None, CourseFrequency=None, PhotoGallery=None, IllustrativePhoto1Extension=None, IllustrativePhoto2Extension=None, IllustrativePhoto3Extension=None, EventHistory=None, Note=None):
        return self._client.service.EventEducationOtherUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducation": ID_EventEducation, "ID_EventEducationCourse": ID_EventEducationCourse, "IsForester": IsForester, "IsQualifyingExam": IsQualifyingExam, "ParticipantFee": ParticipantFee, "NextOccurrenceYear": NextOccurrenceYear, "Graduates": Graduates, "ID_TempFileIllustrativePhoto1": ID_TempFileIllustrativePhoto1, "ID_TempFileIllustrativePhoto2": ID_TempFileIllustrativePhoto2, "ID_TempFileIllustrativePhoto3": ID_TempFileIllustrativePhoto3, "EventEducation": EventEducation, "EventEducationCourse": EventEducationCourse, "Annotation": Annotation, "TargetGroup": TargetGroup, "EventFocus": EventFocus, "EntryConditions": EntryConditions, "GraduateConditions": GraduateConditions, "AuthenticationForm": AuthenticationForm, "CourseFrequency": CourseFrequency, "PhotoGallery": PhotoGallery, "IllustrativePhoto1Extension": IllustrativePhoto1Extension, "IllustrativePhoto2Extension": IllustrativePhoto2Extension, "IllustrativePhoto3Extension": IllustrativePhoto3Extension, "EventHistory": EventHistory, "Note": Note})

    # Načíst seznam položek rozpočtu jiné akce
    def EventGeneralStatementAll(self, ID_Login, ID_EventGeneral, IsEstimate, IsRevenue):
        return self._client.service.EventGeneralStatementAll({"ID_Login": ID_Login, "ID_EventGeneral": ID_EventGeneral, "IsEstimate": IsEstimate, "IsRevenue": IsRevenue})

    # Smazat položku rozpočtu jiné akce
    def EventGeneralStatementDelete(self, ID_Login, ID, ID_EventGeneral, IsRevenue, ID_EventGeneralStatementType, Ammount, IsEstimate, EventGeneralStatementType=None):
        return self._client.service.EventGeneralStatementDelete({"ID_Login": ID_Login, "ID": ID, "ID_EventGeneral": ID_EventGeneral, "IsRevenue": IsRevenue, "ID_EventGeneralStatementType": ID_EventGeneralStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventGeneralStatementType": EventGeneralStatementType})

    # Založit položku rozpočtu jiné akce
    def EventGeneralStatementInsert(self, ID_Login, ID, ID_EventGeneral, IsRevenue, ID_EventGeneralStatementType, Ammount, IsEstimate, EventGeneralStatementType=None):
        return self._client.service.EventGeneralStatementInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventGeneral": ID_EventGeneral, "IsRevenue": IsRevenue, "ID_EventGeneralStatementType": ID_EventGeneralStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventGeneralStatementType": EventGeneralStatementType})

    # Upravit položku rozpočtu jiné akce
    def EventGeneralStatementUpdate(self, ID_Login, ID, ID_EventGeneral, IsRevenue, ID_EventGeneralStatementType, Ammount, IsEstimate, EventGeneralStatementType=None):
        return self._client.service.EventGeneralStatementUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventGeneral": ID_EventGeneral, "IsRevenue": IsRevenue, "ID_EventGeneralStatementType": ID_EventGeneralStatementType, "Ammount": Ammount, "IsEstimate": IsEstimate, "EventGeneralStatementType": EventGeneralStatementType})

    # Načíst seznam instruktorů VzA dle typu
    def InstructorAllInstructorType(self, ID_Login, ID_EventEducation, ShowAll, ID_EventEducationExam, ID_InstructorType=None):
        return self._client.service.InstructorAllInstructorType({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ShowAll": ShowAll, "ID_EventEducationExam": ID_EventEducationExam, "ID_InstructorType": ID_InstructorType})

    # Načíst seznam instruktorů VzA
    def InstructorAllEventEducationPublic(self, ID_Login, ID_Application, ID_EventEducation):
        return self._client.service.InstructorAllEventEducationPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_EventEducation": ID_EventEducation})

    # Načíst veřejný detail instruktora
    def InstructorDetailPublic(self, ID_Login, ID_Application, ID):
        return self._client.service.InstructorDetailPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst detail instruktora
    def InstructorDetail(self, ID_Login, ID):
        return self._client.service.InstructorDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit instruktora
    def InstructorUpdate(self, ID_Login, ID, ID_EventEducation, ID_Person, EventEducation=None, Person=None, ID_InstructorType=None, InstructorType=None, ScoutExperience=None, EventFocus=None, ProfessionalExperience=None):
        return self._client.service.InstructorUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person, "EventEducation": EventEducation, "Person": Person, "ID_InstructorType": ID_InstructorType, "InstructorType": InstructorType, "ScoutExperience": ScoutExperience, "EventFocus": EventFocus, "ProfessionalExperience": ProfessionalExperience})

    # Načíst seznam instruktorů
    def InstructorAll(self, ID_Login, ID_EventEducation, ID, ID_Person, ID_InstructorType=None):
        return self._client.service.InstructorAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "ID_Person": ID_Person, "ID_InstructorType": ID_InstructorType})

    # Smazat 
    def InstructorDelete(self, ID_Login, ID):
        return self._client.service.InstructorDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit 
    def InstructorInsert(self, ID_Login, ID, ID_EventEducation, ID_Person, EventEducation=None, Person=None, ID_InstructorType=None, InstructorType=None, ScoutExperience=None, EventFocus=None, ProfessionalExperience=None):
        return self._client.service.InstructorInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventEducation": ID_EventEducation, "ID_Person": ID_Person, "EventEducation": EventEducation, "Person": Person, "ID_InstructorType": ID_InstructorType, "InstructorType": InstructorType, "ScoutExperience": ScoutExperience, "EventFocus": EventFocus, "ProfessionalExperience": ProfessionalExperience})

    # Načíst seznam typů instruktora
    def InstructorTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.InstructorTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam míst
    def LocationAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.LocationAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam obsazenosti
    def OccupancyAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.OccupancyAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam táborů
    def EventCampAllZip(self, IsFuture, IsRelation, IsChildDirect, IsChildUnit, ID_Login, ID_Unit, Started, Year, ForEvaluation, DisplayName=None, ID_EventCampState=None, RegistrationNumber=None, Location=None):
        return self._client.service.EventCampAllZip({"IsFuture": IsFuture, "IsRelation": IsRelation, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "ID_Login": ID_Login, "ID_Unit": ID_Unit, "Started": Started, "Year": Year, "ForEvaluation": ForEvaluation, "DisplayName": DisplayName, "ID_EventCampState": ID_EventCampState, "RegistrationNumber": RegistrationNumber, "Location": Location})

    # Načíst seznam předchozích táborů
    def EventCampAllParent(self, ID_Login, Year):
        return self._client.service.EventCampAllParent({"ID_Login": ID_Login, "Year": Year})

    # Načíst detail hlášení tábora pro MHMP
    def EventCampCapitalDataDetail(self, ID_Login, ID_EventCamp, IsForReport):
        return self._client.service.EventCampCapitalDataDetail({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "IsForReport": IsForReport})

    # Upravit hlášení tábora pro MHMP
    def EventCampCapitalDataUpdate(self, ID_Login, ID, ID_EventCamp, StartDate, EndDate, GpsLatitude, GpsLongitude, EstimateCount, IsAutoComputed, DateGenerated, DateSent, ID_PersonSent, ID_PersonCorrection, DateSentCorrection, ID_EventCampCity, CityZfoValue, ID_EventCampRegion, RegionZfoValue, ID_EventCampZfoType, ZfoTypeZfoValue, ID_EventCampForm, FormZfoValue, ID_EventCampAccommodationForm, AccommodationFormZfoValue, EventCamp=None, Price=None, EstimateDotation=None, Description=None, PersonGenerated=None, PersonSent=None, PersonCorrection=None, Map=None, ProjectCode=None, EventCampCity=None, EventCampRegion=None, EventCampZfoType=None, EventCampForm=None, EventCampAccommodationForm=None):
        return self._client.service.EventCampCapitalDataUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "EstimateCount": EstimateCount, "IsAutoComputed": IsAutoComputed, "DateGenerated": DateGenerated, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "ID_PersonCorrection": ID_PersonCorrection, "DateSentCorrection": DateSentCorrection, "ID_EventCampCity": ID_EventCampCity, "CityZfoValue": CityZfoValue, "ID_EventCampRegion": ID_EventCampRegion, "RegionZfoValue": RegionZfoValue, "ID_EventCampZfoType": ID_EventCampZfoType, "ZfoTypeZfoValue": ZfoTypeZfoValue, "ID_EventCampForm": ID_EventCampForm, "FormZfoValue": FormZfoValue, "ID_EventCampAccommodationForm": ID_EventCampAccommodationForm, "AccommodationFormZfoValue": AccommodationFormZfoValue, "EventCamp": EventCamp, "Price": Price, "EstimateDotation": EstimateDotation, "Description": Description, "PersonGenerated": PersonGenerated, "PersonSent": PersonSent, "PersonCorrection": PersonCorrection, "Map": Map, "ProjectCode": ProjectCode, "EventCampCity": EventCampCity, "EventCampRegion": EventCampRegion, "EventCampZfoType": EventCampZfoType, "EventCampForm": EventCampForm, "EventCampAccommodationForm": EventCampAccommodationForm})

    # Odeslat hlášenku tábora na MHMP
    def EventCampCapitalDataUpdateSend(self, ID_Login, ID, ID_EventCamp, StartDate, EndDate, GpsLatitude, GpsLongitude, EstimateCount, IsAutoComputed, DateGenerated, DateSent, ID_PersonSent, ID_PersonCorrection, DateSentCorrection, ID_EventCampCity, CityZfoValue, ID_EventCampRegion, RegionZfoValue, ID_EventCampZfoType, ZfoTypeZfoValue, ID_EventCampForm, FormZfoValue, ID_EventCampAccommodationForm, AccommodationFormZfoValue, EventCamp=None, Price=None, EstimateDotation=None, Description=None, PersonGenerated=None, PersonSent=None, PersonCorrection=None, Map=None, ProjectCode=None, EventCampCity=None, EventCampRegion=None, EventCampZfoType=None, EventCampForm=None, EventCampAccommodationForm=None):
        return self._client.service.EventCampCapitalDataUpdateSend({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "EstimateCount": EstimateCount, "IsAutoComputed": IsAutoComputed, "DateGenerated": DateGenerated, "DateSent": DateSent, "ID_PersonSent": ID_PersonSent, "ID_PersonCorrection": ID_PersonCorrection, "DateSentCorrection": DateSentCorrection, "ID_EventCampCity": ID_EventCampCity, "CityZfoValue": CityZfoValue, "ID_EventCampRegion": ID_EventCampRegion, "RegionZfoValue": RegionZfoValue, "ID_EventCampZfoType": ID_EventCampZfoType, "ZfoTypeZfoValue": ZfoTypeZfoValue, "ID_EventCampForm": ID_EventCampForm, "FormZfoValue": FormZfoValue, "ID_EventCampAccommodationForm": ID_EventCampAccommodationForm, "AccommodationFormZfoValue": AccommodationFormZfoValue, "EventCamp": EventCamp, "Price": Price, "EstimateDotation": EstimateDotation, "Description": Description, "PersonGenerated": PersonGenerated, "PersonSent": PersonSent, "PersonCorrection": PersonCorrection, "Map": Map, "ProjectCode": ProjectCode, "EventCampCity": EventCampCity, "EventCampRegion": EventCampRegion, "EventCampZfoType": EventCampZfoType, "EventCampForm": EventCampForm, "EventCampAccommodationForm": EventCampAccommodationForm})

    # Načíst detail zabezpečení tábora
    def EventCampProvisionDetail(self, ID_Login, ID_EventCamp):
        return self._client.service.EventCampProvisionDetail({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp})

    # Upravit zabezpečení tábora
    def EventCampProvisionUpdate(self, ID_Login, ID, ID_EventCamp, DrinkingWater, DrinkingWaterCheckDate, ServiceWaterSame, BathingAllowed, ServiceWaterCheckDate, FirstAidKitDate, ID_PersonFirstAidKit, DrinkingWaterCheckPerson=None, ServiceWaterCheckPerson=None, PersonFirstAidKit=None, DoctorPhone=None, DoctorPhoneDisplay=None, DoctorAddress=None, HospitalPhone=None, HospitalPhoneDisplay=None, HospitalAddress=None):
        return self._client.service.EventCampProvisionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "DrinkingWater": DrinkingWater, "DrinkingWaterCheckDate": DrinkingWaterCheckDate, "ServiceWaterSame": ServiceWaterSame, "BathingAllowed": BathingAllowed, "ServiceWaterCheckDate": ServiceWaterCheckDate, "FirstAidKitDate": FirstAidKitDate, "ID_PersonFirstAidKit": ID_PersonFirstAidKit, "DrinkingWaterCheckPerson": DrinkingWaterCheckPerson, "ServiceWaterCheckPerson": ServiceWaterCheckPerson, "PersonFirstAidKit": PersonFirstAidKit, "DoctorPhone": DoctorPhone, "DoctorPhoneDisplay": DoctorPhoneDisplay, "DoctorAddress": DoctorAddress, "HospitalPhone": HospitalPhone, "HospitalPhoneDisplay": HospitalPhoneDisplay, "HospitalAddress": HospitalAddress})

    # Nastavit, zda se počty účastníků počítají automaticky
    def EventGeneralUpdateStatisticAutoComputed(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateStatisticAutoComputed({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Načíst detail účastníka obecné akce
    def ParticipantGeneralDetail(self, ID_Login, ID):
        return self._client.service.ParticipantGeneralDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit celkové skutečné náklady
    def EventCampUpdateRealTotalCost(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateRealTotalCost({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Zrušit odevzdání skutečnosti 
    def EventCampUpdateCancelReal(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateCancelReal({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Odevzdat skutečnost
    def EventCampUpdateReal(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateReal({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Nastavit, zda se počty tábořících počítají automaticky
    def EventCampUpdateDays(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateDays({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Načíst detail počty účastníků v kategoriích
    def EventCampStatisticDetail(self, ID_Login, ID_EventCamp, IsEstimate):
        return self._client.service.EventCampStatisticDetail({"ID_Login": ID_Login, "ID_EventCamp": ID_EventCamp, "IsEstimate": IsEstimate})

    # Zrušit tábor
    def EventCampUpdateCancel(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateCancel({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Smazat tábor
    def EventCampDelete(self, ID_Login, ID):
        return self._client.service.EventCampDelete({"ID_Login": ID_Login, "ID": ID})

    # Upravit počet dospělých účastníků
    def EventCampSendMessage(self, ID_Login):
        return self._client.service.EventCampSendMessage({"ID_Login": ID_Login})

    # Otevřít tábor po schválení střediskem
    def EventCampUpdateReOpen(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateReOpen({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Upravit tabořícího
    def ParticipantCampUpdate(self, ID_Login, ID, ID_Person, ID_Participant, Estimate, Real, Days, Note=None):
        return self._client.service.ParticipantCampUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Participant": ID_Participant, "Estimate": Estimate, "Real": Real, "Days": Days, "Note": Note})

    # Načíst seznam typů akcí
    def EventTypeAll(self, ID_Login, DisplayName=None, ID_Table=None):
        return self._client.service.EventTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_Table": ID_Table})

    # Upravit počty dnů účastníků akce
    def EventGeneralUpdateDays(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateDays({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Upravit vedení obecné akce
    def EventGeneralUpdateFunction(self, ID_Login, ID, ID_PersonLeader, ID_PersonAssistant, ID_PersonEconomist, ID_PersonMedic, LeaderNote=None, AssistantNote=None, EconomistNote=None, MedicNote=None):
        return self._client.service.EventGeneralUpdateFunction({"ID_Login": ID_Login, "ID": ID, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonEconomist": ID_PersonEconomist, "ID_PersonMedic": ID_PersonMedic, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "EconomistNote": EconomistNote, "MedicNote": MedicNote})

    # Načíst vedení obecné akce
    def EventFunctionAllGeneral(self, ID_Login, ID_EventGeneral, ID_Person, ID_EventFunctionType):
        return self._client.service.EventFunctionAllGeneral({"ID_Login": ID_Login, "ID_EventGeneral": ID_EventGeneral, "ID_Person": ID_Person, "ID_EventFunctionType": ID_EventFunctionType})

    # Otevřít obecnou akci
    def EventGeneralUpdateOpen(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateOpen({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Uzavřít obecnou akci
    def EventGeneralUpdateClose(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateClose({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Upravit zprávu z akce
    def EventGeneralUpdateReport(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateReport({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Zrušit obecnou akci
    def EventGeneralUpdateCancel(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdateCancel({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Načíst seznam obecných akcí
    def EventGeneralAll(self, IsFuture, IsRelation, IsChildDirect, IsChildUnit, ID_Login, ID_EventGeneralType, ID_EventGeneralScope, Year, ID_EventGeneralState=None):
        return self._client.service.EventGeneralAll({"IsFuture": IsFuture, "IsRelation": IsRelation, "IsChildDirect": IsChildDirect, "IsChildUnit": IsChildUnit, "ID_Login": ID_Login, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "Year": Year, "ID_EventGeneralState": ID_EventGeneralState})

    # Smazat obecnou akci
    def EventGeneralDelete(self, ID_Login, ID):
        return self._client.service.EventGeneralDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail obecné akce
    def EventGeneralDetail(self, ID_Login, ID):
        return self._client.service.EventGeneralDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit obecnou akci
    def EventGeneralInsert(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralInsert({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Načíst seznam rozsahů obecné akce
    def EventGeneralScopeAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventGeneralScopeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam stavů obecné akce
    def EventGeneralStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventGeneralStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam typů obecné akce
    def EventGeneralTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventGeneralTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit obecnou akci
    def EventGeneralUpdate(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, TotalDays, GpsLatitude, GpsLongitude, ID_Event, ID_UnitEducative, ID_EventGeneralType, ID_EventGeneralScope, ForeignParticipants, LeaderParticipants, AssistantParticipants, IsStatisticAutoComputed, ChildDays, PersonDays, ID_PersonClosed, DateClosed, IsAutoComputedDays, TotalParticipants, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, Event=None, ID_EventGeneralState=None, EventGeneralState=None, UnitEducative=None, UnitEducativeRegistrationNumber=None, EventGeneralType=None, EventGeneralScope=None, Street=None, Postcode=None, Region=None, State=None, Target=None, Program=None, PersonClosed=None, ID_EventSpecificationTypeArray=None, EventSpecificationType=None):
        return self._client.service.EventGeneralUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "TotalDays": TotalDays, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "ID_UnitEducative": ID_UnitEducative, "ID_EventGeneralType": ID_EventGeneralType, "ID_EventGeneralScope": ID_EventGeneralScope, "ForeignParticipants": ForeignParticipants, "LeaderParticipants": LeaderParticipants, "AssistantParticipants": AssistantParticipants, "IsStatisticAutoComputed": IsStatisticAutoComputed, "ChildDays": ChildDays, "PersonDays": PersonDays, "ID_PersonClosed": ID_PersonClosed, "DateClosed": DateClosed, "IsAutoComputedDays": IsAutoComputedDays, "TotalParticipants": TotalParticipants, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "Event": Event, "ID_EventGeneralState": ID_EventGeneralState, "EventGeneralState": EventGeneralState, "UnitEducative": UnitEducative, "UnitEducativeRegistrationNumber": UnitEducativeRegistrationNumber, "EventGeneralType": EventGeneralType, "EventGeneralScope": EventGeneralScope, "Street": Street, "Postcode": Postcode, "Region": Region, "State": State, "Target": Target, "Program": Program, "PersonClosed": PersonClosed, "ID_EventSpecificationTypeArray": ID_EventSpecificationTypeArray, "EventSpecificationType": EventSpecificationType})

    # Načíst seznam typů dalších údajů akxe
    def EventSpecificationTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventSpecificationTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam počtů účastníků podle kategorií
    def EventStatisticAllEventGeneral(self, ID_Login, ID_EventGeneral, ID_ParticipantCategory):
        return self._client.service.EventStatisticAllEventGeneral({"ID_Login": ID_Login, "ID_EventGeneral": ID_EventGeneral, "ID_ParticipantCategory": ID_ParticipantCategory})

    # Upravit počet účastníku podle kategorie
    def EventStatisticUpdateEventGeneral(self, ID_Login, ID, Count):
        return self._client.service.EventStatisticUpdateEventGeneral({"ID_Login": ID_Login, "ID": ID, "Count": Count})

    # Načíst seznam účastníků obecné akce
    def ParticipantGeneralAll(self, ID_Login, ID_EventGeneral):
        return self._client.service.ParticipantGeneralAll({"ID_Login": ID_Login, "ID_EventGeneral": ID_EventGeneral})

    # Smazat účastníka obecné akce
    def ParticipantGeneralDelete(self, ID_Login, ID, DeletePerson):
        return self._client.service.ParticipantGeneralDelete({"ID_Login": ID_Login, "ID": ID, "DeletePerson": DeletePerson})

    # Založit účastníka obecné akce
    def ParticipantGeneralInsert(self, ID_Login, ID_EventGeneral, ID_Person, Person=None):
        return self._client.service.ParticipantGeneralInsert({"ID_Login": ID_Login, "ID_EventGeneral": ID_EventGeneral, "ID_Person": ID_Person, "Person": Person})

    # Upravit účastníka obecné akce
    def ParticipantGeneralUpdate(self, ID_Login, ID, ID_Participant, Days, Note=None):
        return self._client.service.ParticipantGeneralUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Participant": ID_Participant, "Days": Days, "Note": Note})

    # Načíst seznam stavů tábora
    def EventCampStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.EventCampStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Zrušit schválení tábora
    def EventCampUpdateCancelApprove(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateCancelApprove({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Schválit tábor
    def EventCampUpdateApprove(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateApprove({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Otevřít tábor
    def EventCampUpdateOpen(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateOpen({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Uzavřít tábor
    def EventCampUpdateClose(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateClose({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Upravit vedení tábora
    def EventCampUpdateFunction(self, ID_Login, ID, ID_PersonLeader, LeaderHealthQualification, LeaderHealthQualificationDate, ID_PersonAssistant, AssistantHealthQualification, AssistantHealthQualificationDate, ID_PersonMedic, ID_PersonEconomist, ID_PersonCook, LeaderNote=None, AssistantNote=None, MedicNote=None, EconomistNote=None, CookNote=None):
        return self._client.service.EventCampUpdateFunction({"ID_Login": ID_Login, "ID": ID, "ID_PersonLeader": ID_PersonLeader, "LeaderHealthQualification": LeaderHealthQualification, "LeaderHealthQualificationDate": LeaderHealthQualificationDate, "ID_PersonAssistant": ID_PersonAssistant, "AssistantHealthQualification": AssistantHealthQualification, "AssistantHealthQualificationDate": AssistantHealthQualificationDate, "ID_PersonMedic": ID_PersonMedic, "ID_PersonEconomist": ID_PersonEconomist, "ID_PersonCook": ID_PersonCook, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "MedicNote": MedicNote, "EconomistNote": EconomistNote, "CookNote": CookNote})

    # Načíst seznam ubytování
    def AccommodationAll(self, ID_Login, ID_EventCongress, ID_Person, DateFree, DisplayName=None):
        return self._client.service.AccommodationAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID_Person": ID_Person, "DateFree": DateFree, "DisplayName": DisplayName})

    # Smazat ubytování
    def AccommodationDelete(self, ID_Login, ID):
        return self._client.service.AccommodationDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail ubytování
    def AccommodationDetail(self, ID_Login, ID):
        return self._client.service.AccommodationDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit ubytování
    def AccommodationInsert(self, ID_Login, ID, ID_EventCongress, Fee, DisplayName=None):
        return self._client.service.AccommodationInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "Fee": Fee, "DisplayName": DisplayName})

    # Načíst seznam typů účastníků ubytování
    def AccommodationParticipantTypeAll(self, ID_Login, ID_Accommodation, ID_ParticipantType=None):
        return self._client.service.AccommodationParticipantTypeAll({"ID_Login": ID_Login, "ID_Accommodation": ID_Accommodation, "ID_ParticipantType": ID_ParticipantType})

    # Smazat typ účastníka ubytování
    def AccommodationParticipantTypeDelete(self, ID_Login, ID):
        return self._client.service.AccommodationParticipantTypeDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit typ účastníka ubytování
    def AccommodationParticipantTypeInsert(self, ID_Login, ID_Accommodation, ID_ParticipantType=None):
        return self._client.service.AccommodationParticipantTypeInsert({"ID_Login": ID_Login, "ID_Accommodation": ID_Accommodation, "ID_ParticipantType": ID_ParticipantType})

    # Upravit ubytování
    def AccommodationUpdate(self, ID_Login, ID, ID_EventCongress, Fee, DisplayName=None):
        return self._client.service.AccommodationUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "Fee": Fee, "DisplayName": DisplayName})

    # Načíst seznam typů tábora
    def CampTypeAll(self, ID_Login, DisplayName=None):
        return self._client.service.CampTypeAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit počet dospělých účastníků
    def EventCampUpdateAdult(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateAdult({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Načíst seznam akcí osoby
    def EventAllPersonParticipation(self, ID_Login, ID_Person, Year, ID_EventType=None, DisplayName=None):
        return self._client.service.EventAllPersonParticipation({"ID_Login": ID_Login, "ID_Person": ID_Person, "Year": Year, "ID_EventType": ID_EventType, "DisplayName": DisplayName})

    # Načíst seznam odpovědí
    def CampAnswerAll(self, ID_Login, ID, ID_CampQuestion, ID_EventCamp):
        return self._client.service.CampAnswerAll({"ID_Login": ID_Login, "ID": ID, "ID_CampQuestion": ID_CampQuestion, "ID_EventCamp": ID_EventCamp})

    # Načíst seznam stavů tábora
    def CampPlaceAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.CampPlaceAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam otázek
    def CampQuestionAll(self, ID_Login, ID, ID_EventCamp, DisplayName=None):
        return self._client.service.CampQuestionAll({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "DisplayName": DisplayName})

    # Načíst detail Jedinečné ID
    def CampQuestionDetail(self, ID_Login, ID):
        return self._client.service.CampQuestionDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam dotazníků
    def CampSurveyAll(self, ID_Login, ID, ID_Person, ID_Event, ID_CampQuestion, ID_CampAnswer):
        return self._client.service.CampSurveyAll({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Event": ID_Event, "ID_CampQuestion": ID_CampQuestion, "ID_CampAnswer": ID_CampAnswer})

    # Založit 
    def CampSurveyInsert(self, ID_Login, ID, ID_Person, ID_Event, ID_CampQuestion, ID_CampAnswer, Event=None, CampQuestion=None, CampSurveyQuestionAnswer=None):
        return self._client.service.CampSurveyInsert({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_Event": ID_Event, "ID_CampQuestion": ID_CampQuestion, "ID_CampAnswer": ID_CampAnswer, "Event": Event, "CampQuestion": CampQuestion, "CampSurveyQuestionAnswer": CampSurveyQuestionAnswer})

    # Načtení informací o osobě pro souhlas se zápisem do spolkového rejstříku
    def CandidateDetailAgreementTemplate(self, ID_Login, ID, ID_FunctionType, CityText=None):
        return self._client.service.CandidateDetailAgreementTemplate({"ID_Login": ID_Login, "ID": ID, "ID_FunctionType": ID_FunctionType, "CityText": CityText})

    # Načíst detail souhlasu se zápisem kandidáta na pozici
    def CandidateDetailFunctionAgreement(self, ID_Login, ID, FunctionText=None, CityText=None):
        return self._client.service.CandidateDetailFunctionAgreement({"ID_Login": ID_Login, "ID": ID, "FunctionText": FunctionText, "CityText": CityText})

    # Načíst seznam kandidátů sněmů pro souhlas se zápisem
    def EventCongressAllCandidateFunctionAgreement(self, ID, ID_Login):
        return self._client.service.EventCongressAllCandidateFunctionAgreement({"ID": ID, "ID_Login": ID_Login})

    # Načíst zkrácený výpis sněmu OJ
    def EventCongressDetailSimplifiedEntry(self, ID_Login, ID):
        return self._client.service.EventCongressDetailSimplifiedEntry({"ID_Login": ID_Login, "ID": ID})

    # Načte detail sněmu pro zkrácený zápis
    def EventCongressDetailSimplified(self, ID_Login, ID):
        return self._client.service.EventCongressDetailSimplified({"ID_Login": ID_Login, "ID": ID})

    # Načíst zabalené souhlasy se zápisem do spolkového rejstříku
    def EventCongressDetailFunctionAgreement(self, ID_Login, ID):
        return self._client.service.EventCongressDetailFunctionAgreement({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam volených funkcí
    def EventCongressFunctionAllSimplifiedResult(self, ID_Login, ID):
        return self._client.service.EventCongressFunctionAllSimplifiedResult({"ID_Login": ID_Login, "ID": ID})

    # Načte ID a název typu volené funkce
    def EventCongressFunctionAllSimplified(self, ID_Login, ID):
        return self._client.service.EventCongressFunctionAllSimplified({"ID_Login": ID_Login, "ID": ID})

    # Nahrát zkrácený výpis sněmu
    def EventCongressUpdateSimplifiedEntry(self, ID_Login, ID, ID_Event, ID_UnitRegistration, PromulgationDeadline, CommissionDeadline, CandidateDeadline, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, AlternateStartDate, AlternateEndDate, AlternateGpsLatitude, AlternateGpsLongitude, CandidateAfterDeadline, ArriveDeadline, DepartureDeadline, TransportDeadline, AccommodationDeadline, FoodDeadline, ParticipantFee, ID_TempFileSimplifiedEntryExtension, Event=None, UnitRegistration=None, ID_EventCongressType=None, EventCongressType=None, ID_EventCongressState=None, EventCongressState=None, Unit=None, RegistrationNumber=None, ID_UnitType=None, Location=None, AlternateLocation=None, Note=None, ProtocolExtension=None, ProtocolContent=None, FunctionAgreementExtension=None, SimplifiedEntryExtension=None, SimplifiedEntryTemplateExtension=None):
        return self._client.service.EventCongressUpdateSimplifiedEntry({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event, "ID_UnitRegistration": ID_UnitRegistration, "PromulgationDeadline": PromulgationDeadline, "CommissionDeadline": CommissionDeadline, "CandidateDeadline": CandidateDeadline, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "AlternateStartDate": AlternateStartDate, "AlternateEndDate": AlternateEndDate, "AlternateGpsLatitude": AlternateGpsLatitude, "AlternateGpsLongitude": AlternateGpsLongitude, "CandidateAfterDeadline": CandidateAfterDeadline, "ArriveDeadline": ArriveDeadline, "DepartureDeadline": DepartureDeadline, "TransportDeadline": TransportDeadline, "AccommodationDeadline": AccommodationDeadline, "FoodDeadline": FoodDeadline, "ParticipantFee": ParticipantFee, "ID_TempFileSimplifiedEntryExtension": ID_TempFileSimplifiedEntryExtension, "Event": Event, "UnitRegistration": UnitRegistration, "ID_EventCongressType": ID_EventCongressType, "EventCongressType": EventCongressType, "ID_EventCongressState": ID_EventCongressState, "EventCongressState": EventCongressState, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "ID_UnitType": ID_UnitType, "Location": Location, "AlternateLocation": AlternateLocation, "Note": Note, "ProtocolExtension": ProtocolExtension, "ProtocolContent": ProtocolContent, "FunctionAgreementExtension": FunctionAgreementExtension, "SimplifiedEntryExtension": SimplifiedEntryExtension, "SimplifiedEntryTemplateExtension": SimplifiedEntryTemplateExtension})

    # Načíst seznam osobodnů akce
    def EducationPersonDaysAll(self, ID_Login, ID_EventEducation, ID, ID_EventEducationType, Year):
        return self._client.service.EducationPersonDaysAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "Year": Year})

    # Upravit osobodny akce
    def EducationPersonDaysUpdate(self, ID_Login, ID, ID_EventEducation, ID_EventEducationType, PersonDays, Year, EventEducationType=None):
        return self._client.service.EducationPersonDaysUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducation": ID_EventEducation, "ID_EventEducationType": ID_EventEducationType, "PersonDays": PersonDays, "Year": Year, "EventEducationType": EventEducationType})

    # Načíst seznam vzdělávacích akcí
    def EventEducationCheckRealParticipation(self, ID_Login):
        return self._client.service.EventEducationCheckRealParticipation({"ID_Login": ID_Login})

    # Načíst seznam vzdělávacích akcí
    def EventEducationAllCalendarPublic(self, ID_Login, ID_Application, ID_EventEducationType):
        return self._client.service.EventEducationAllCalendarPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_EventEducationType": ID_EventEducationType})

    # Vygeneruje kalendář
    def GenerateCalendar(self, EventEducationAllCalendarPublicOutput=None):
        return self._client.service.GenerateCalendar({"EventEducationAllCalendarPublicOutput": EventEducationAllCalendarPublicOutput})

    # Přehled dotovaných vzdělávacích akcí
    def EventEducationAllGrantOverview(self, ID_Login, Year):
        return self._client.service.EventEducationAllGrantOverview({"ID_Login": ID_Login, "Year": Year})

    # Načíst seznam vzdělávacích akcí
    def EventEducationAllEducatationSeminary(self, ID_Login):
        return self._client.service.EventEducationAllEducatationSeminary({"ID_Login": ID_Login})

    # Načíst seznam vzdělávacích akcí
    def EventEducationAllPublic(self, ID_Login, ID_Application, GpsLatitude, GpsLongitude, Distance, IsQualificationExam, From, To, StartsTo, EndsTo, ParticipantFeeFrom, ParticipantFeeTo, DurationFrom, DurationTo, ParticipantCountFrom, ParticipantCountTo, IsApproved, IsRegistrationOpen, EventEducationType=None, DisplayName=None, ID_EventEducationGroup=None, ID_RegionList=None, ID_DistrictList=None, ID_OccupancyList=None):
        return self._client.service.EventEducationAllPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "Distance": Distance, "IsQualificationExam": IsQualificationExam, "From": From, "To": To, "StartsTo": StartsTo, "EndsTo": EndsTo, "ParticipantFeeFrom": ParticipantFeeFrom, "ParticipantFeeTo": ParticipantFeeTo, "DurationFrom": DurationFrom, "DurationTo": DurationTo, "ParticipantCountFrom": ParticipantCountFrom, "ParticipantCountTo": ParticipantCountTo, "IsApproved": IsApproved, "IsRegistrationOpen": IsRegistrationOpen, "EventEducationType": EventEducationType, "DisplayName": DisplayName, "ID_EventEducationGroup": ID_EventEducationGroup, "ID_RegionList": ID_RegionList, "ID_DistrictList": ID_DistrictList, "ID_OccupancyList": ID_OccupancyList})

    # Načíst přehled vzdělávacích akcí
    def EventEducationAllOverview(self, ID_Login, ShowAll, ShowValid, Year, ID_EventEducationType=None, ID_EventEducationState=None, ID_GrantState=None, ID_EventEducationCommissionState=None):
        return self._client.service.EventEducationAllOverview({"ID_Login": ID_Login, "ShowAll": ShowAll, "ShowValid": ShowValid, "Year": Year, "ID_EventEducationType": ID_EventEducationType, "ID_EventEducationState": ID_EventEducationState, "ID_GrantState": ID_GrantState, "ID_EventEducationCommissionState": ID_EventEducationCommissionState})

    # Načíst seznam akcí jednotky u kterých není žádost o dotaci
    def EventEducationAllUnitNoGrant(self, ID_Login, ID_Unit, ID_EventType=None):
        return self._client.service.EventEducationAllUnitNoGrant({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_EventType": ID_EventType})

    # Načíst seznam vzdělávacích akcí - Moje akce
    def EventEducationAllEvaluation(self, ID_Login, ID_EventEducationType, IsParent, Year):
        return self._client.service.EventEducationAllEvaluation({"ID_Login": ID_Login, "ID_EventEducationType": ID_EventEducationType, "IsParent": IsParent, "Year": Year})

    # Načíst seznam forem ubytování
    def EventCampAccommodationFormAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.EventCampAccommodationFormAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst ZFO formulář
    def EventCampCapitalDataDetailZfo(self, ID_Login, ID):
        return self._client.service.EventCampCapitalDataDetailZfo({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam obcí
    def EventCampCityAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.EventCampCityAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam forem tábora
    def EventCampFormAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.EventCampFormAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Načíst seznam krajů
    def EventCampRegionAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.EventCampRegionAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit opravu hlášenky
    def EventCampReportCapitalCorrectionInsert(self, ID_Login, ID, ID_EventCamp, ID_PersonCreated, DateCreated, PersonCreated=None, Decision=None):
        return self._client.service.EventCampReportCapitalCorrectionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCamp": ID_EventCamp, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "PersonCreated": PersonCreated, "Decision": Decision})

    # Upravit celkové skutečné náklady před koncem akce
    def EventCampUpdateRealTotalCostBeforeEnd(self, ID_Login, ID, ID_Group, ID_UserCreate, DateCreate, ID_Unit, StartDate, EndDate, GpsLatitude, GpsLongitude, ID_Event, RegistrationDeadline, ID_Region, IsFloodArea, IsAutoComputed, ID_PersonApproved, DateApproved, ID_PersonApprovedParent, DateApprovedParent, DateApprovedExecutive, TotalDays, IsRecovering, EstimateChild, EstimateAdult, EstimateCount, EstimateChildDays, EstimatePersonDays, IsAutoComputedDays, RealTotalCost, IsRealTotalCostAutoComputed, IsRealAutoComputed, IsRealAutoComputedDays, ID_PersonReal, DateReal, RealAdult, RealChild, RealCount, RealChildDays, RealPersonDays, HasEstimateStatement, ID_PersonLeader, Profit, ProfitComputed, ProfitComputedEstimation, ID_CampPlace, ID_EventType=None, DisplayName=None, Unit=None, RegistrationNumber=None, GpsLatitudeText=None, GpsLongitudeText=None, Location=None, Note=None, CancelDecision=None, ID_EventCampState=None, EventCampState=None, MobileContact=None, MobileContactDisplay=None, Region=None, Postcode=None, PersonApproved=None, PersonApprovedParent=None, CampType=None, ID_CampTypeArray=None, ID_UnitArray=None, Units=None, PersonReal=None, PersonLeader=None, PersonLeaderFirstName=None, PersonLeaderLastName=None, PersonLeaderCivilName=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderCity=None, UnitLocation=None, PersonStatutory=None, CampPlace=None):
        return self._client.service.EventCampUpdateRealTotalCostBeforeEnd({"ID_Login": ID_Login, "ID": ID, "ID_Group": ID_Group, "ID_UserCreate": ID_UserCreate, "DateCreate": DateCreate, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "ID_Event": ID_Event, "RegistrationDeadline": RegistrationDeadline, "ID_Region": ID_Region, "IsFloodArea": IsFloodArea, "IsAutoComputed": IsAutoComputed, "ID_PersonApproved": ID_PersonApproved, "DateApproved": DateApproved, "ID_PersonApprovedParent": ID_PersonApprovedParent, "DateApprovedParent": DateApprovedParent, "DateApprovedExecutive": DateApprovedExecutive, "TotalDays": TotalDays, "IsRecovering": IsRecovering, "EstimateChild": EstimateChild, "EstimateAdult": EstimateAdult, "EstimateCount": EstimateCount, "EstimateChildDays": EstimateChildDays, "EstimatePersonDays": EstimatePersonDays, "IsAutoComputedDays": IsAutoComputedDays, "RealTotalCost": RealTotalCost, "IsRealTotalCostAutoComputed": IsRealTotalCostAutoComputed, "IsRealAutoComputed": IsRealAutoComputed, "IsRealAutoComputedDays": IsRealAutoComputedDays, "ID_PersonReal": ID_PersonReal, "DateReal": DateReal, "RealAdult": RealAdult, "RealChild": RealChild, "RealCount": RealCount, "RealChildDays": RealChildDays, "RealPersonDays": RealPersonDays, "HasEstimateStatement": HasEstimateStatement, "ID_PersonLeader": ID_PersonLeader, "Profit": Profit, "ProfitComputed": ProfitComputed, "ProfitComputedEstimation": ProfitComputedEstimation, "ID_CampPlace": ID_CampPlace, "ID_EventType": ID_EventType, "DisplayName": DisplayName, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "GpsLatitudeText": GpsLatitudeText, "GpsLongitudeText": GpsLongitudeText, "Location": Location, "Note": Note, "CancelDecision": CancelDecision, "ID_EventCampState": ID_EventCampState, "EventCampState": EventCampState, "MobileContact": MobileContact, "MobileContactDisplay": MobileContactDisplay, "Region": Region, "Postcode": Postcode, "PersonApproved": PersonApproved, "PersonApprovedParent": PersonApprovedParent, "CampType": CampType, "ID_CampTypeArray": ID_CampTypeArray, "ID_UnitArray": ID_UnitArray, "Units": Units, "PersonReal": PersonReal, "PersonLeader": PersonLeader, "PersonLeaderFirstName": PersonLeaderFirstName, "PersonLeaderLastName": PersonLeaderLastName, "PersonLeaderCivilName": PersonLeaderCivilName, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderCity": LeaderCity, "UnitLocation": UnitLocation, "PersonStatutory": PersonStatutory, "CampPlace": CampPlace})

    # Načíst seznam typů tábora pro ZFO formulář
    def EventCampZfoTypeAll(self, ID_Login, ID, DisplayName=None):
        return self._client.service.EventCampZfoTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit účastníka VSJ
    def ParticipantUpdateUstredi(self, ID_Login, ID, Note=None):
        return self._client.service.ParticipantUpdateUstredi({"ID_Login": ID_Login, "ID": ID, "Note": Note})

    # Načíst seznam kapacit ubytování
    def AccommodationCapacityAll(self, ID_Login, ID_Accommodation, ID):
        return self._client.service.AccommodationCapacityAll({"ID_Login": ID_Login, "ID_Accommodation": ID_Accommodation, "ID": ID})

    # Upravit kapacitu ubytování
    def AccommodationCapacityUpdate(self, ID_Login, ID, ID_Accommodation, Date, Capacity, Accommodation=None):
        return self._client.service.AccommodationCapacityUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Accommodation": ID_Accommodation, "Date": Date, "Capacity": Capacity, "Accommodation": Accommodation})

    # Načíst seznam usnesení sněmů
    def EventCongressDecisionAll(self, ID_Login, ID_EventCongress, ID, ID_PersonCreated, IsSuggest, ID_EventCongressDecisionType=None, ID_UnitType=None):
        return self._client.service.EventCongressDecisionAll({"ID_Login": ID_Login, "ID_EventCongress": ID_EventCongress, "ID": ID, "ID_PersonCreated": ID_PersonCreated, "IsSuggest": IsSuggest, "ID_EventCongressDecisionType": ID_EventCongressDecisionType, "ID_UnitType": ID_UnitType})

    # Smazat usnesení sněmu
    def EventCongressDecisionDelete(self, ID_Login, ID):
        return self._client.service.EventCongressDecisionDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail usnesení sněmu
    def EventCongressDecisionDetail(self, ID_Login, ID):
        return self._client.service.EventCongressDecisionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit usnesení sněmu
    def EventCongressDecisionInsert(self, ID_Login, ID, ID_EventCongress, IsSuggest, ID_PersonCreated, DateCreated, Suggester=None, ID_EventCongressDecisionType=None, EventCongressDecisionType=None, ID_UnitType=None, UnitType=None, Text=None, Decision=None, PersonCreated=None):
        return self._client.service.EventCongressDecisionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "IsSuggest": IsSuggest, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "Suggester": Suggester, "ID_EventCongressDecisionType": ID_EventCongressDecisionType, "EventCongressDecisionType": EventCongressDecisionType, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Text": Text, "Decision": Decision, "PersonCreated": PersonCreated})

    # Načíst seznam typů usnesení
    def EventCongressDecisionTypeAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.EventCongressDecisionTypeAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit usnesení sněmu
    def EventCongressDecisionUpdate(self, ID_Login, ID, ID_EventCongress, IsSuggest, ID_PersonCreated, DateCreated, Suggester=None, ID_EventCongressDecisionType=None, EventCongressDecisionType=None, ID_UnitType=None, UnitType=None, Text=None, Decision=None, PersonCreated=None):
        return self._client.service.EventCongressDecisionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventCongress": ID_EventCongress, "IsSuggest": IsSuggest, "ID_PersonCreated": ID_PersonCreated, "DateCreated": DateCreated, "Suggester": Suggester, "ID_EventCongressDecisionType": ID_EventCongressDecisionType, "EventCongressDecisionType": EventCongressDecisionType, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "Text": Text, "Decision": Decision, "PersonCreated": PersonCreated})

    # Načíst detail sněmu
    def EventCongressDetailStatistics(self, ID_Login, ID):
        return self._client.service.EventCongressDetailStatistics({"ID_Login": ID_Login, "ID": ID})

    # No documentation
    def DistrictAll(self, ID_Login, ID, ID_Region, DisplayName=None):
        return self._client.service.DistrictAll({"ID_Login": ID_Login, "ID": ID, "ID_Region": ID_Region, "DisplayName": DisplayName})

    # Načíst seznam vzdělávacích akcí
    def EventEducationAll(self, ID_Login, ID, ID_EventEducationType, DisplayName=None, ID_EventEducationGroup=None):
        return self._client.service.EventEducationAll({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "DisplayName": DisplayName, "ID_EventEducationGroup": ID_EventEducationGroup})

    # Načíst seznam vzdělávacích akcí - Moje akce
    def EventEducationAllMyActions(self, ID_Login, ID, ID_EventEducationType, IsFuture, Year, ID_Unit, DisplayName=None, ID_EventEducationGroup=None, ID_EventEducationState=None):
        return self._client.service.EventEducationAllMyActions({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "IsFuture": IsFuture, "Year": Year, "ID_Unit": ID_Unit, "DisplayName": DisplayName, "ID_EventEducationGroup": ID_EventEducationGroup, "ID_EventEducationState": ID_EventEducationState})

    # No documentation
    def EventEducationCommissionStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.EventEducationCommissionStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Přehled žádostí o dotaci u kurzů
    def EventEducationCourseAllGrantSummary(self, ID_Login, Year):
        return self._client.service.EventEducationCourseAllGrantSummary({"ID_Login": ID_Login, "Year": Year})

    # Načíst seznam kurzů vzdělávacích akcí
    def EventEducationCourseAllPublic(self, ID_Login, ID_Application, ID_Occupancy, MinParticipants, MaxParticipants, HasFreeSlot, ID_EventEducation, DisplayName=None):
        return self._client.service.EventEducationCourseAllPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID_Occupancy": ID_Occupancy, "MinParticipants": MinParticipants, "MaxParticipants": MaxParticipants, "HasFreeSlot": HasFreeSlot, "ID_EventEducation": ID_EventEducation, "DisplayName": DisplayName})

    # Načíst seznam kurzů vzdělávacích akcí
    def EventEducationCourseAllGrant(self, ID_Login, ID_Grant):
        return self._client.service.EventEducationCourseAllGrant({"ID_Login": ID_Login, "ID_Grant": ID_Grant})

    # Načíst detail kurzu vzdělávací akce pro přihlášku
    def EventEducationCourseDetailEnroll(self, ID_Login, ID):
        return self._client.service.EventEducationCourseDetailEnroll({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail kurzu vzdělávací akce
    def EventEducationCourseDetailPublic(self, ID, ID_Login, ID_Application, DisplayName=None):
        return self._client.service.EventEducationCourseDetailPublic({"ID": ID, "ID_Login": ID_Login, "ID_Application": ID_Application, "DisplayName": DisplayName})

    # Načíst seznam termínů vzdělávacího kurzu
    def EventEducationCourseTermAllPublic(self, ID_Login, ID_Application, GpsLatitude, GpsLongitude, Distance, Start, End, MinimalLength, MaximalLength, ID_EventEducationCourse, ID_EventEducationTerm, ID_EventEducation, RegionList=None):
        return self._client.service.EventEducationCourseTermAllPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "GpsLatitude": GpsLatitude, "GpsLongitude": GpsLongitude, "Distance": Distance, "Start": Start, "End": End, "MinimalLength": MinimalLength, "MaximalLength": MaximalLength, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_EventEducationTerm": ID_EventEducationTerm, "ID_EventEducation": ID_EventEducation, "RegionList": RegionList})

    # Načíst detail termínu vzdělávacího kurzu
    def EventEducationCourseTermDetailPublic(self, ID, ID_Login, ID_Application):
        return self._client.service.EventEducationCourseTermDetailPublic({"ID": ID, "ID_Login": ID_Login, "ID_Application": ID_Application})

    # Načíst roky vzdělávací akce
    def EventEducationDetailEventYears(self, ID_Login, ID, ID_Event):
        return self._client.service.EventEducationDetailEventYears({"ID_Login": ID_Login, "ID": ID, "ID_Event": ID_Event})

    # Informace o udělení kvalifikace
    def ParticipantEducationExamGrantedReminder(self, ID_Login):
        return self._client.service.ParticipantEducationExamGrantedReminder({"ID_Login": ID_Login})

    # Odeslat výzvy k dokončení neúspěšně absolvované zkoušky
    def ParticipantEducationExamUnfinishedReminder(self, ID_Login):
        return self._client.service.ParticipantEducationExamUnfinishedReminder({"ID_Login": ID_Login})

    # Odeslat výzvy k dokončení hlášenky vzdělávací akce
    def EventEducationUnfinishedReminder(self, ID_Login):
        return self._client.service.EventEducationUnfinishedReminder({"ID_Login": ID_Login})

    # Odeslat výzvy k zadání výsledků proběhlé zkoušky
    def EventEducationExamCheckReminder(self, ID_Login):
        return self._client.service.EventEducationExamCheckReminder({"ID_Login": ID_Login})

    # Načíst žádosti o dekret bez vygenerovaného čísla
    def EventEducationLetterRequestAllNotGenerated(self, ID_Login):
        return self._client.service.EventEducationLetterRequestAllNotGenerated({"ID_Login": ID_Login})

    # Načíst seznam žádostí o dekret pro export
    def EventEducationLetterRequestAllAttachmentExport(self, ID_Login, IsParticipantEducation, ExportAttachments, ID_Items=None):
        return self._client.service.EventEducationLetterRequestAllAttachmentExport({"ID_Login": ID_Login, "IsParticipantEducation": IsParticipantEducation, "ExportAttachments": ExportAttachments, "ID_Items": ID_Items})

    # Najde žádosti k vyřízení a informuje o nich administrátora kvalifikací 
    def EventEducationLetterRequestCheck(self, ID_Login):
        return self._client.service.EventEducationLetterRequestCheck({"ID_Login": ID_Login})

    # Generovat číslo k žádosti
    def EventEducationLetterRequestUpdateGenerate(self, ID_Login, ID, ID_ParticipantEducationExam, ID_ParticipantEducation, Date, DateSent, ID_EventEducationLetterRequestState=None, EventEducationLetterRequestState=None, LetterNumber=None):
        return self._client.service.EventEducationLetterRequestUpdateGenerate({"ID_Login": ID_Login, "ID": ID, "ID_ParticipantEducationExam": ID_ParticipantEducationExam, "ID_ParticipantEducation": ID_ParticipantEducation, "Date": Date, "DateSent": DateSent, "ID_EventEducationLetterRequestState": ID_EventEducationLetterRequestState, "EventEducationLetterRequestState": EventEducationLetterRequestState, "LetterNumber": LetterNumber})

    # Hlídá dobu po kterou je dekrety možné předávat
    def EventEducationtExamAllCheckLetter(self, ID_Login):
        return self._client.service.EventEducationtExamAllCheckLetter({"ID_Login": ID_Login})

    # Dekrety pro zkoušku byly odeslány
    def EventEducationLetterRequestAllCheckDateSent(self, ID_Login):
        return self._client.service.EventEducationLetterRequestAllCheckDateSent({"ID_Login": ID_Login})

    # No documentation
    def EventEducationTermUpdateIsRealParticipationSet(self, ID_Login, ID, IsActive, ID_EventEducation, ID_EventEducationLocation, DateFrom, DateTo, IsRealParticipationSet, DisplayName=None, EventEducationLocation=None, Note=None):
        return self._client.service.EventEducationTermUpdateIsRealParticipationSet({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_EventEducationLocation": ID_EventEducationLocation, "DateFrom": DateFrom, "DateTo": DateTo, "IsRealParticipationSet": IsRealParticipationSet, "DisplayName": DisplayName, "EventEducationLocation": EventEducationLocation, "Note": Note})

    # Uzavřít vzdělávací akci
    def EventEducationUpdateClose(self, ID_Login, ID):
        return self._client.service.EventEducationUpdateClose({"ID_Login": ID_Login, "ID": ID})

    # Zadat datum schválení pořádající jednotkou
    def EventEducationUpdateUnitApproved(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateUnitApproved({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit poznámku vzdělávací akce
    def EventEducationUpdateOverview(self, ID_Login, ID, HasProject, ProjectNote=None):
        return self._client.service.EventEducationUpdateOverview({"ID_Login": ID_Login, "ID": ID, "HasProject": HasProject, "ProjectNote": ProjectNote})

    # Zruśit potvrzení vzdělávací akce
    def EventEducationUpdateReject(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationUpdateReject({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Upravit poznámku vzdělávací akce
    def EventEducationUpdateNote(self, ID_Login, ID, ProjectNote=None):
        return self._client.service.EventEducationUpdateNote({"ID_Login": ID_Login, "ID": ID, "ProjectNote": ProjectNote})

    # Rozeslat zprávy o přijetí/nepřijetí účastníkům VzA
    def ParticipantEducationAllSendMessages(self, ID_Login):
        return self._client.service.ParticipantEducationAllSendMessages({"ID_Login": ID_Login})

    # Založit účastníka vzdělávací akce z přihlášky
    def ParticipantEducationInsertEnroll(self, ID_Login, ID_EventEducationCourse, Acknownledgement, Affirmation, Phone=None):
        return self._client.service.ParticipantEducationInsertEnroll({"ID_Login": ID_Login, "ID_EventEducationCourse": ID_EventEducationCourse, "Acknownledgement": Acknownledgement, "Affirmation": Affirmation, "Phone": Phone})

    # Načíst zjednodušený detail vzdělávací akce
    def EventEducationDetailSimple(self, ID_Login, ID):
        return self._client.service.EventEducationDetailSimple({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail vzdělávací akce
    def EventEducationDetailPublic(self, ID_Login, ID_Application, ID):
        return self._client.service.EventEducationDetailPublic({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID})

    # Načíst maximalní možnou velikost dotací pro akci
    def EventEducationDetailMaxGrantAmount(self, ID_Login, ID_EventEducation):
        return self._client.service.EventEducationDetailMaxGrantAmount({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation})

    # Načíst maximalní možnou velikost dotací pro jednotlivé kurz
    def EventEducationDetailMaxGrantAmounts(self, ID_Login, ID_Event, ID_Grant, Year):
        return self._client.service.EventEducationDetailMaxGrantAmounts({"ID_Login": ID_Login, "ID_Event": ID_Event, "ID_Grant": ID_Grant, "Year": Year})

    # Načíst provizorní žádost o dotaci
    def EventEducationDetailGrant(self, ID_Login, ID):
        return self._client.service.EventEducationDetailGrant({"ID_Login": ID_Login, "ID": ID})

    # Kontrola zkušební komise
    def EventEducationExamCheck(self, ID_Login, ID):
        return self._client.service.EventEducationExamCheck({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam členů zkušební komise
    def EventEducationCommissionAll(self, ID_Login, ID_EventEducationExam, ID, ID_Person):
        return self._client.service.EventEducationCommissionAll({"ID_Login": ID_Login, "ID_EventEducationExam": ID_EventEducationExam, "ID": ID, "ID_Person": ID_Person})

    # Smazat 
    def EventEducationCommissionDelete(self, ID_Login, ID):
        return self._client.service.EventEducationCommissionDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit 
    def EventEducationCommissionInsert(self, ID_Login, ID, ID_EventEducationExam, ID_Person, IsLeader, Person=None):
        return self._client.service.EventEducationCommissionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationExam": ID_EventEducationExam, "ID_Person": ID_Person, "IsLeader": IsLeader, "Person": Person})

    # Změnit člena zkušební komise na předsedu
    def EventEducationCommissionUpdateSetLeader(self, ID_Login, ID, ID_EventEducationExam, ID_Person, IsLeader, Person=None):
        return self._client.service.EventEducationCommissionUpdateSetLeader({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationExam": ID_EventEducationExam, "ID_Person": ID_Person, "IsLeader": IsLeader, "Person": Person})

    # Načíst obsazenost kurzů vzdělávacích akcí
    def EventEducationCourseAllParticipants(self, ID_Login, ID_EventEducation):
        return self._client.service.EventEducationCourseAllParticipants({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation})

    # Načíst seznam kurzů vzdělávacích akcí
    def EventEducationCourseAll(self, ID_Login, ID_EventEducation, ID_Event, ID, ID_EventEducationType, ID_Occupation):
        return self._client.service.EventEducationCourseAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID_Event": ID_Event, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "ID_Occupation": ID_Occupation})

    # Smazat kurz vzdělávací akce
    def EventEducationCourseDelete(self, ID_Login, ID):
        return self._client.service.EventEducationCourseDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail kurzu vzdělávací akce
    def EventEducationCourseDetail(self, ID_Login, ID):
        return self._client.service.EventEducationCourseDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit kurz vzdělávací akce
    def EventEducationCourseInsert(self, ID_Login, ID, IsActive, ID_EventEducation, ID_EventEducationType, ID_Occupation, CapacityCourse, CapacitySubstitute, RegistrationDeadline, EstimatedParticipantCount, CanUpdateType, IsContractor, IsAccredited, Fulfillment, PersonDays, IsCustomPersonDays, IsAccreditedExternal, EventEducationType=None, Occupation=None, Note=None, EventEducation=None, AccreditationNumber=None, DisplayName=None):
        return self._client.service.EventEducationCourseInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_EventEducationType": ID_EventEducationType, "ID_Occupation": ID_Occupation, "CapacityCourse": CapacityCourse, "CapacitySubstitute": CapacitySubstitute, "RegistrationDeadline": RegistrationDeadline, "EstimatedParticipantCount": EstimatedParticipantCount, "CanUpdateType": CanUpdateType, "IsContractor": IsContractor, "IsAccredited": IsAccredited, "Fulfillment": Fulfillment, "PersonDays": PersonDays, "IsCustomPersonDays": IsCustomPersonDays, "IsAccreditedExternal": IsAccreditedExternal, "EventEducationType": EventEducationType, "Occupation": Occupation, "Note": Note, "EventEducation": EventEducation, "AccreditationNumber": AccreditationNumber, "DisplayName": DisplayName})

    # Načíst seznam termínů vzdělávacího kurzu
    def EventEducationCourseTermAll(self, ID_Login, ID, ID_EventEducationCourse, ID_EventEducationTerm, ID_EventEducation):
        return self._client.service.EventEducationCourseTermAll({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_EventEducationTerm": ID_EventEducationTerm, "ID_EventEducation": ID_EventEducation})

    # Smazat termín vzdělávacího kurzu
    def EventEducationCourseTermDelete(self, ID_Login, ID):
        return self._client.service.EventEducationCourseTermDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail termínu vzdělávacího kurzu
    def EventEducationCourseTermDetail(self, ID_Login, ID):
        return self._client.service.EventEducationCourseTermDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit termín vzdělávacího kurzu
    def EventEducationCourseTermInsert(self, ID_Login, ID, ID_EventEducationCourse, ID_EventEducationTerm, DateFrom, DateTo, ID_EventEducationLocation, Longitude, Latitude, TermNote=None, FirstLine=None, ID_Region=None, Region=None, Street=None, Postcode=None, City=None, LocationNote=None):
        return self._client.service.EventEducationCourseTermInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_EventEducationTerm": ID_EventEducationTerm, "DateFrom": DateFrom, "DateTo": DateTo, "ID_EventEducationLocation": ID_EventEducationLocation, "Longitude": Longitude, "Latitude": Latitude, "TermNote": TermNote, "FirstLine": FirstLine, "ID_Region": ID_Region, "Region": Region, "Street": Street, "Postcode": Postcode, "City": City, "LocationNote": LocationNote})

    # Upravit termín vzdělávacího kurzu
    def EventEducationCourseTermUpdate(self, ID_Login, ID, ID_EventEducationCourse, ID_EventEducationTerm, DateFrom, DateTo, ID_EventEducationLocation, Longitude, Latitude, TermNote=None, FirstLine=None, Region=None, Street=None, Postcode=None, City=None, LocationNote=None):
        return self._client.service.EventEducationCourseTermUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_EventEducationTerm": ID_EventEducationTerm, "DateFrom": DateFrom, "DateTo": DateTo, "ID_EventEducationLocation": ID_EventEducationLocation, "Longitude": Longitude, "Latitude": Latitude, "TermNote": TermNote, "FirstLine": FirstLine, "Region": Region, "Street": Street, "Postcode": Postcode, "City": City, "LocationNote": LocationNote})

    # Upravit kurz vzdělávací akce
    def EventEducationCourseUpdate(self, ID_Login, ID, IsActive, ID_EventEducation, ID_EventEducationType, ID_Occupation, CapacityCourse, CapacitySubstitute, RegistrationDeadline, EstimatedParticipantCount, CanUpdateType, IsContractor, IsAccredited, Fulfillment, PersonDays, IsCustomPersonDays, IsAccreditedExternal, EventEducationType=None, Occupation=None, Note=None, EventEducation=None, AccreditationNumber=None, DisplayName=None):
        return self._client.service.EventEducationCourseUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_EventEducation": ID_EventEducation, "ID_EventEducationType": ID_EventEducationType, "ID_Occupation": ID_Occupation, "CapacityCourse": CapacityCourse, "CapacitySubstitute": CapacitySubstitute, "RegistrationDeadline": RegistrationDeadline, "EstimatedParticipantCount": EstimatedParticipantCount, "CanUpdateType": CanUpdateType, "IsContractor": IsContractor, "IsAccredited": IsAccredited, "Fulfillment": Fulfillment, "PersonDays": PersonDays, "IsCustomPersonDays": IsCustomPersonDays, "IsAccreditedExternal": IsAccreditedExternal, "EventEducationType": EventEducationType, "Occupation": Occupation, "Note": Note, "EventEducation": EventEducation, "AccreditationNumber": AccreditationNumber, "DisplayName": DisplayName})

    # Smazat vzdělávací akci
    def EventEducationDelete(self, ID_Login, ID):
        return self._client.service.EventEducationDelete({"ID_Login": ID_Login, "ID": ID})

    # Zkontrolovat validitu vzdělávací akce
    def EventEducationCheck(self, ID_Login, ID):
        return self._client.service.EventEducationCheck({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail vzdělávací akce
    def EventEducationDetail(self, ID_Login, ID):
        return self._client.service.EventEducationDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail vzdělávací akce
    def EventEducationDetailLogo(self, ID_Login, ID_Application, ID, Size=None):
        return self._client.service.EventEducationDetailLogo({"ID_Login": ID_Login, "ID_Application": ID_Application, "ID": ID, "Size": Size})

    # Načíst seznam zkoušek
    def EventEducationExamAll(self, ID_Login, ID_EventEducation, ID, ID_QualificationType):
        return self._client.service.EventEducationExamAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "ID_QualificationType": ID_QualificationType})

    # Kontrola osob ve zkušební komisi
    def EventEducationExamCheckPerson(self, ID_Login, ID):
        return self._client.service.EventEducationExamCheckPerson({"ID_Login": ID_Login, "ID": ID})

    # Smazat zkoušku
    def EventEducationExamDelete(self, ID_Login, ID):
        return self._client.service.EventEducationExamDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail zkoušky
    def EventEducationExamDetail(self, ID_Login, ID):
        return self._client.service.EventEducationExamDetail({"ID_Login": ID_Login, "ID": ID})

    # Smazat výjimku člena zkušební komise
    def EventEducationExamExceptionDelete(self, ID_Login, ID):
        return self._client.service.EventEducationExamExceptionDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail výjimky člena zkušební komise
    def EventEducationExamExceptionDetail(self, ID_Login, ID):
        return self._client.service.EventEducationExamExceptionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit výjimku člena zkušební komise
    def EventEducationExamExceptionInsert(self, ID_Login, ID, ID_EventEducationExam, ID_Person, Person=None, Note=None):
        return self._client.service.EventEducationExamExceptionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationExam": ID_EventEducationExam, "ID_Person": ID_Person, "Person": Person, "Note": Note})

    # Upravit výjimku člena zkušební komise
    def EventEducationExamExceptionUpdate(self, ID_Login, ID, ID_EventEducationExam, ID_Person, Person=None, Note=None):
        return self._client.service.EventEducationExamExceptionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationExam": ID_EventEducationExam, "ID_Person": ID_Person, "Person": Person, "Note": Note})

    # Založit zkoušku
    def EventEducationExamInsert(self, ID_Login, ID, IsActive, ID_QualificationType, ID_EventEducation, Capacity, Date, ID_EventEducationTypeExam, ID_EventEducationCourse, ID_PersonLeader, HasLeaderQualification, EventLastDay, CanChangeQualificationType, QualificationType=None, EventEducation=None, ID_EventEducationCommissionState=None, EventEducationCommissionState=None, CommissionNote=None, PersonLeader=None, LeaderQualifications=None):
        return self._client.service.EventEducationExamInsert({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_QualificationType": ID_QualificationType, "ID_EventEducation": ID_EventEducation, "Capacity": Capacity, "Date": Date, "ID_EventEducationTypeExam": ID_EventEducationTypeExam, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_PersonLeader": ID_PersonLeader, "HasLeaderQualification": HasLeaderQualification, "EventLastDay": EventLastDay, "CanChangeQualificationType": CanChangeQualificationType, "QualificationType": QualificationType, "EventEducation": EventEducation, "ID_EventEducationCommissionState": ID_EventEducationCommissionState, "EventEducationCommissionState": EventEducationCommissionState, "CommissionNote": CommissionNote, "PersonLeader": PersonLeader, "LeaderQualifications": LeaderQualifications})

    # Upravit zkoušku
    def EventEducationExamUpdate(self, ID_Login, ID, IsActive, ID_QualificationType, ID_EventEducation, Capacity, Date, ID_EventEducationTypeExam, ID_EventEducationCourse, ID_PersonLeader, HasLeaderQualification, EventLastDay, CanChangeQualificationType, QualificationType=None, EventEducation=None, ID_EventEducationCommissionState=None, EventEducationCommissionState=None, CommissionNote=None, PersonLeader=None, LeaderQualifications=None):
        return self._client.service.EventEducationExamUpdate({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_QualificationType": ID_QualificationType, "ID_EventEducation": ID_EventEducation, "Capacity": Capacity, "Date": Date, "ID_EventEducationTypeExam": ID_EventEducationTypeExam, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_PersonLeader": ID_PersonLeader, "HasLeaderQualification": HasLeaderQualification, "EventLastDay": EventLastDay, "CanChangeQualificationType": CanChangeQualificationType, "QualificationType": QualificationType, "EventEducation": EventEducation, "ID_EventEducationCommissionState": ID_EventEducationCommissionState, "EventEducationCommissionState": EventEducationCommissionState, "CommissionNote": CommissionNote, "PersonLeader": PersonLeader, "LeaderQualifications": LeaderQualifications})

    # Změnit stav zkušební komise
    def EventEducationExamUpdateCommissionState(self, ID_Login, ID, IsActive, ID_QualificationType, ID_EventEducation, Capacity, Date, ID_EventEducationTypeExam, ID_EventEducationCourse, ID_PersonLeader, HasLeaderQualification, EventLastDay, CanChangeQualificationType, QualificationType=None, EventEducation=None, ID_EventEducationCommissionState=None, EventEducationCommissionState=None, CommissionNote=None, PersonLeader=None, LeaderQualifications=None):
        return self._client.service.EventEducationExamUpdateCommissionState({"ID_Login": ID_Login, "ID": ID, "IsActive": IsActive, "ID_QualificationType": ID_QualificationType, "ID_EventEducation": ID_EventEducation, "Capacity": Capacity, "Date": Date, "ID_EventEducationTypeExam": ID_EventEducationTypeExam, "ID_EventEducationCourse": ID_EventEducationCourse, "ID_PersonLeader": ID_PersonLeader, "HasLeaderQualification": HasLeaderQualification, "EventLastDay": EventLastDay, "CanChangeQualificationType": CanChangeQualificationType, "QualificationType": QualificationType, "EventEducation": EventEducation, "ID_EventEducationCommissionState": ID_EventEducationCommissionState, "EventEducationCommissionState": EventEducationCommissionState, "CommissionNote": CommissionNote, "PersonLeader": PersonLeader, "LeaderQualifications": LeaderQualifications})

    # Načíst seznam skupin typů vzdělávacích akcí
    def EventEducationGroupAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.EventEducationGroupAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Založit vzdělávací akci
    def EventEducationInsert(self, ID_Login, ID, DateApproved, Grant, DateClosed, ID_PersonClosed, LoginSkautis, ID_Unit, StartDate, EndDate, ID_EventEducationType, ID_Event, ID_PersonLeader, ID_PersonAssistant, ID_PersonSecretary, ID_PersonEconomist, RegistrationDeadline, ID_TempFileProject, ProjectDelete, ID_PersonProject, ProjectApproved, ProjectUpdate, ID_TempFileFinalReport, FinalReportDelete, ID_PersonFinalReport, FinalReportUpdate, FinalReportApproved, IsWaterman, IsForester, IsPossibleToGraduate, Published, Confirmed, Approved, ApprovedWater, GrantNew, GrantApproved, GrantDecisionNew, GrantDecisionConfirmed, AdvanceSent, ID_Grant, Fulfilment, Publicized, IsQualifyingExam, HasGrantRequest, HasTermsOnlyForNextYear, LastTerm, IsCounselor, DateUnitApproved, IsProjectRequired, IsFinalReportRequired, ID_EventEducationState=None, EventEducationState=None, Web=None, EmailContact=None, PhoneContact=None, ID_GrantType=None, GrantType=None, ID_GrantAdvanceType=None, GrantAdvanceType=None, PersonClosed=None, LogoFileName=None, PropagationFileName1=None, PropagationFileName2=None, PropagationFileName3=None, LoginLocation=None, Description=None, DisplayName=None, Location=None, Note=None, Unit=None, RegistrationNumber=None, PersonLeader=None, LeaderPhone=None, LeaderPhoneDisplay=None, LeaderEmail=None, LeaderEmailDisplay=None, LeaderNote=None, AssistantNote=None, SecretaryNote=None, EconomistNote=None, LogoContent=None, Project=None, ProjectExtension=None, ProjectNote=None, ProjectContent=None, PersonProject=None, FinalReport=None, FinalReportExtension=None, FinalReportNote=None, FinalReportContent=None, PersonFinalReport=None, RejectionNote=None, DisapproveNote=None, WaterDisapproveNote=None, ID_GrantState=None):
        return self._client.service.EventEducationInsert({"ID_Login": ID_Login, "ID": ID, "DateApproved": DateApproved, "Grant": Grant, "DateClosed": DateClosed, "ID_PersonClosed": ID_PersonClosed, "LoginSkautis": LoginSkautis, "ID_Unit": ID_Unit, "StartDate": StartDate, "EndDate": EndDate, "ID_EventEducationType": ID_EventEducationType, "ID_Event": ID_Event, "ID_PersonLeader": ID_PersonLeader, "ID_PersonAssistant": ID_PersonAssistant, "ID_PersonSecretary": ID_PersonSecretary, "ID_PersonEconomist": ID_PersonEconomist, "RegistrationDeadline": RegistrationDeadline, "ID_TempFileProject": ID_TempFileProject, "ProjectDelete": ProjectDelete, "ID_PersonProject": ID_PersonProject, "ProjectApproved": ProjectApproved, "ProjectUpdate": ProjectUpdate, "ID_TempFileFinalReport": ID_TempFileFinalReport, "FinalReportDelete": FinalReportDelete, "ID_PersonFinalReport": ID_PersonFinalReport, "FinalReportUpdate": FinalReportUpdate, "FinalReportApproved": FinalReportApproved, "IsWaterman": IsWaterman, "IsForester": IsForester, "IsPossibleToGraduate": IsPossibleToGraduate, "Published": Published, "Confirmed": Confirmed, "Approved": Approved, "ApprovedWater": ApprovedWater, "GrantNew": GrantNew, "GrantApproved": GrantApproved, "GrantDecisionNew": GrantDecisionNew, "GrantDecisionConfirmed": GrantDecisionConfirmed, "AdvanceSent": AdvanceSent, "ID_Grant": ID_Grant, "Fulfilment": Fulfilment, "Publicized": Publicized, "IsQualifyingExam": IsQualifyingExam, "HasGrantRequest": HasGrantRequest, "HasTermsOnlyForNextYear": HasTermsOnlyForNextYear, "LastTerm": LastTerm, "IsCounselor": IsCounselor, "DateUnitApproved": DateUnitApproved, "IsProjectRequired": IsProjectRequired, "IsFinalReportRequired": IsFinalReportRequired, "ID_EventEducationState": ID_EventEducationState, "EventEducationState": EventEducationState, "Web": Web, "EmailContact": EmailContact, "PhoneContact": PhoneContact, "ID_GrantType": ID_GrantType, "GrantType": GrantType, "ID_GrantAdvanceType": ID_GrantAdvanceType, "GrantAdvanceType": GrantAdvanceType, "PersonClosed": PersonClosed, "LogoFileName": LogoFileName, "PropagationFileName1": PropagationFileName1, "PropagationFileName2": PropagationFileName2, "PropagationFileName3": PropagationFileName3, "LoginLocation": LoginLocation, "Description": Description, "DisplayName": DisplayName, "Location": Location, "Note": Note, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "PersonLeader": PersonLeader, "LeaderPhone": LeaderPhone, "LeaderPhoneDisplay": LeaderPhoneDisplay, "LeaderEmail": LeaderEmail, "LeaderEmailDisplay": LeaderEmailDisplay, "LeaderNote": LeaderNote, "AssistantNote": AssistantNote, "SecretaryNote": SecretaryNote, "EconomistNote": EconomistNote, "LogoContent": LogoContent, "Project": Project, "ProjectExtension": ProjectExtension, "ProjectNote": ProjectNote, "ProjectContent": ProjectContent, "PersonProject": PersonProject, "FinalReport": FinalReport, "FinalReportExtension": FinalReportExtension, "FinalReportNote": FinalReportNote, "FinalReportContent": FinalReportContent, "PersonFinalReport": PersonFinalReport, "RejectionNote": RejectionNote, "DisapproveNote": DisapproveNote, "WaterDisapproveNote": WaterDisapproveNote, "ID_GrantState": ID_GrantState})

    # Načíst seznam filtrů pro žádostí o dekret
    def EventEducationLetterFilterAll(self, ID_Login):
        return self._client.service.EventEducationLetterFilterAll({"ID_Login": ID_Login})

    # Načíst seznam žádostí o dekret pro export
    def EventEducationLetterRequestAllExport(self, ID_Login, IsParticipantEducation, ID_Items=None):
        return self._client.service.EventEducationLetterRequestAllExport({"ID_Login": ID_Login, "IsParticipantEducation": IsParticipantEducation, "ID_Items": ID_Items})

    # Načíst seznam žádostí o dekret
    def EventEducationLetterRequestAllEventEducation(self, ID_Login, ID, ID_ParticipantEducationExam, ID_EventEducationLetterRequestState=None):
        return self._client.service.EventEducationLetterRequestAllEventEducation({"ID_Login": ID_Login, "ID": ID, "ID_ParticipantEducationExam": ID_ParticipantEducationExam, "ID_EventEducationLetterRequestState": ID_EventEducationLetterRequestState})

    # Načíst seznam žádostí o dekret
    def EventEducationLetterRequestAll(self, ID_Login, Person=None, EventEducation=None, IdentificationCode=None, EventEducationLetterRequestFilter=None, ID_QualificationType=None):
        return self._client.service.EventEducationLetterRequestAll({"ID_Login": ID_Login, "Person": Person, "EventEducation": EventEducation, "IdentificationCode": IdentificationCode, "EventEducationLetterRequestFilter": EventEducationLetterRequestFilter, "ID_QualificationType": ID_QualificationType})

    # Obnovit žádost o dekret
    def EventEducationLetterRequestRestore(self, ID_Login, ID):
        return self._client.service.EventEducationLetterRequestRestore({"ID_Login": ID_Login, "ID": ID})

    # Smazat žádost o dekret
    def EventEducationLetterRequestDelete(self, ID_Login, ID):
        return self._client.service.EventEducationLetterRequestDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit žádost o dekret
    def EventEducationLetterRequestInsert(self, ID_Login, ID, ID_ParticipantEducationExam, ID_ParticipantEducation, Date, DateSent, ID_EventEducationLetterRequestState=None, EventEducationLetterRequestState=None, LetterNumber=None):
        return self._client.service.EventEducationLetterRequestInsert({"ID_Login": ID_Login, "ID": ID, "ID_ParticipantEducationExam": ID_ParticipantEducationExam, "ID_ParticipantEducation": ID_ParticipantEducation, "Date": Date, "DateSent": DateSent, "ID_EventEducationLetterRequestState": ID_EventEducationLetterRequestState, "EventEducationLetterRequestState": EventEducationLetterRequestState, "LetterNumber": LetterNumber})

    # Načíst seznam stavů žádosti o dekret
    def EventEducationLetterRequestStateAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.EventEducationLetterRequestStateAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

    # Upravit žádost o dekret
    def EventEducationLetterRequestUpdate(self, ID_Login, ID, ID_ParticipantEducationExam, ID_ParticipantEducation, Date, DateSent, ID_EventEducationLetterRequestState=None, EventEducationLetterRequestState=None, LetterNumber=None):
        return self._client.service.EventEducationLetterRequestUpdate({"ID_Login": ID_Login, "ID": ID, "ID_ParticipantEducationExam": ID_ParticipantEducationExam, "ID_ParticipantEducation": ID_ParticipantEducation, "Date": Date, "DateSent": DateSent, "ID_EventEducationLetterRequestState": ID_EventEducationLetterRequestState, "EventEducationLetterRequestState": EventEducationLetterRequestState, "LetterNumber": LetterNumber})

    # Načíst seznam umístění vzdělávací akce
    def EventEducationLocationAll(self, ID_Login, ID_EventEducation, ID, DisplayName=None):
        return self._client.service.EventEducationLocationAll({"ID_Login": ID_Login, "ID_EventEducation": ID_EventEducation, "ID": ID, "DisplayName": DisplayName})

    # Smazat umístění vzdělávací akce
    def EventEducationLocationDelete(self, ID_Login, ID):
        return self._client.service.EventEducationLocationDelete({"ID_Login": ID_Login, "ID": ID})

