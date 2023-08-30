# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s hodnocením kvality
class Evaluation(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Evaluation.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Evaluation.asmx?wsdl')

    # Načíst počty hodnocení po jednotlivých úrovních
    def EvaluationAllDegradationCount(self, ID_Login, Year):
        return self._client.service.EvaluationAllDegradationCount({"ID_Login": ID_Login, "Year": Year})

    # Načíst seznam hodnocení kvality akcí
    def EvaluationAllChild(self, ID_Login, Year, IsUnit):
        return self._client.service.EvaluationAllChild({"ID_Login": ID_Login, "Year": Year, "IsUnit": IsUnit})

    # Grafický pohled - počty hodnocení dané úrovně za posledních 10 let
    def EvaluationAllGraphParticipationYearCompare(self, ID_Login, EvaluationTypeID=None):
        return self._client.service.EvaluationAllGraphParticipationYearCompare({"ID_Login": ID_Login, "EvaluationTypeID": EvaluationTypeID})

    # Grafický pohled - počty hodnocení dané úrovně dle výsledků za posledních 10 let
    def EvaluationAllGraphRatingYearCompare(self, ID_Login, EvaluationTypeID=None):
        return self._client.service.EvaluationAllGraphRatingYearCompare({"ID_Login": ID_Login, "EvaluationTypeID": EvaluationTypeID})

    # Grafický pohled na hodnocení podřízených jednotek - Valašský frgál
    def EvaluationAllGraphSummary(self, ID_Login, ID_EvaluationSubtype, Year, DrawGraph):
        return self._client.service.EvaluationAllGraphSummary({"ID_Login": ID_Login, "ID_EvaluationSubtype": ID_EvaluationSubtype, "Year": Year, "DrawGraph": DrawGraph})

    # Načíst počty hodnocení po jednotlivých úrovních
    def EvaluationAllImprovementCount(self, ID_Login, Year):
        return self._client.service.EvaluationAllImprovementCount({"ID_Login": ID_Login, "Year": Year})

    # Načíst seznam hodnocení kvality akcí
    def EvaluationAllParent(self, ID_Login, Year):
        return self._client.service.EvaluationAllParent({"ID_Login": ID_Login, "Year": Year})

    # Načíst účást HK podřízených jednotek
    def EvaluationAllParticipation(self, ID_Login, Year, EvaluationTypeID=None):
        return self._client.service.EvaluationAllParticipation({"ID_Login": ID_Login, "Year": Year, "EvaluationTypeID": EvaluationTypeID})

    # Načíst účást HK podřízených jednotek
    def EvaluationAllParticipationCompare(self, ID_Login, Year):
        return self._client.service.EvaluationAllParticipationCompare({"ID_Login": ID_Login, "Year": Year})

    # Načíst počty stabilních hodnocení po jednotlivých úrovních
    def EvaluationAllSectionMedian(self, ID_Login, Year, ID_EvaluationSubtype):
        return self._client.service.EvaluationAllSectionMedian({"ID_Login": ID_Login, "Year": Year, "ID_EvaluationSubtype": ID_EvaluationSubtype})

    # Načíst počty stabilních hodnocení po jednotlivých úrovních
    def EvaluationAllStabilityCount(self, ID_Login, Year):
        return self._client.service.EvaluationAllStabilityCount({"ID_Login": ID_Login, "Year": Year})

    # Načíst počty hodnocení po jednotlivých úrovních
    def EvaluationAllTypeCount(self, ID_Login, Year, EvaluationTypeID=None):
        return self._client.service.EvaluationAllTypeCount({"ID_Login": ID_Login, "Year": Year, "EvaluationTypeID": EvaluationTypeID})

    # Načíst seznam kritérii pro oblast hodnocní
    def EvaluationCriteriaAllEvaluation(self, ID_Login, ID_Evaluation, ID_EvaluationSection):
        return self._client.service.EvaluationCriteriaAllEvaluation({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation, "ID_EvaluationSection": ID_EvaluationSection})

    # Načíst srovnání s ostatními
    def EvaluationAllCompare(self, ID_Login, Year, DrawGraph, Culture=None):
        return self._client.service.EvaluationAllCompare({"ID_Login": ID_Login, "Year": Year, "DrawGraph": DrawGraph, "Culture": Culture})

    # Načíst srovnání s ostatními
    def EvaluationDetailCompare(self, ID_Login, ID, DrawGraph, Culture=None):
        return self._client.service.EvaluationDetailCompare({"ID_Login": ID_Login, "ID": ID, "DrawGraph": DrawGraph, "Culture": Culture})

    # Stáhnout všechny exporty hodnocení kvality
    def EvaluationDetailExport(self, ID_Login, ID):
        return self._client.service.EvaluationDetailExport({"ID_Login": ID_Login, "ID": ID})

    # Načíst graf vah oblastí daného hodnocení
    def EvaluationDetailGraphSectionWeight(self, ID_Login, ID, ID_EvaluationSection, SectionColor=None):
        return self._client.service.EvaluationDetailGraphSectionWeight({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSection": ID_EvaluationSection, "SectionColor": SectionColor})

    # Načíst meziroční srovnání
    def EvaluationDetailYearCompare(self, ID_Login, ID, ID_Unit, ID_Event):
        return self._client.service.EvaluationDetailYearCompare({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event})

    # Načíst graf meziroční srovnání
    def EvaluationDetailGraphYearCompare(self, ID_Login, ID, ID_Unit, ID_Event):
        return self._client.service.EvaluationDetailGraphYearCompare({"ID_Login": ID_Login, "ID": ID, "ID_Unit": ID_Unit, "ID_Event": ID_Event})

    # Grafický pohled na hodnocení - Valašský frgál
    def EvaluationGraph(self, DrawGraph, ID_Login, ID):
        return self._client.service.EvaluationGraph({"DrawGraph": DrawGraph, "ID_Login": ID_Login, "ID": ID})

    # Načíst seznam hodnocení kvality
    def EvaluationAll(self, ID_Login, Year, NotExists, IsUnit, ID_EventEducationType, ID_EvaluationState=None, Unit=None, ID_EventType=None):
        return self._client.service.EvaluationAll({"ID_Login": ID_Login, "Year": Year, "NotExists": NotExists, "IsUnit": IsUnit, "ID_EventEducationType": ID_EventEducationType, "ID_EvaluationState": ID_EvaluationState, "Unit": Unit, "ID_EventType": ID_EventType})

    # Načíst seznam hodnocení kvality akcí
    def EvaluationAllPerson(self, ID_Login, Year, IsUnit, NotExists, ID_EventEducationType, ID_EventType=None):
        return self._client.service.EvaluationAllPerson({"ID_Login": ID_Login, "Year": Year, "IsUnit": IsUnit, "NotExists": NotExists, "ID_EventEducationType": ID_EventEducationType, "ID_EventType": ID_EventType})

    # Seznam let, ve kterých je mozne zalozit hodnocení kvality
    def EvaluationAllYearCreate(self, ID_Login, IsUnit, IsEventEducation):
        return self._client.service.EvaluationAllYearCreate({"ID_Login": ID_Login, "IsUnit": IsUnit, "IsEventEducation": IsEventEducation})

    # Načíst seznam odpovědí individuálního hodnocení kvality
    def EvaluationAnswerAllEvaluationPerson(self, ID_Login, ID_EvaluationPerson):
        return self._client.service.EvaluationAnswerAllEvaluationPerson({"ID_Login": ID_Login, "ID_EvaluationPerson": ID_EvaluationPerson})

    # Načíst seznam individuálních hodnocení k základnímu hodnocení
    def EvaluationPersonAllEvaluation(self, ID_Login, ID, ID_Evaluation, ID_Person):
        return self._client.service.EvaluationPersonAllEvaluation({"ID_Login": ID_Login, "ID": ID, "ID_Evaluation": ID_Evaluation, "ID_Person": ID_Person})

    # Založit individuální hodnocení
    def EvaluationPersonInsert(self, ID_Login, ID_Evaluation, ID_Person, ID_Event, ID_EvaluationSubtype, Year):
        return self._client.service.EvaluationPersonInsert({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation, "ID_Person": ID_Person, "ID_Event": ID_Event, "ID_EvaluationSubtype": ID_EvaluationSubtype, "Year": Year})

    # Upravit individuální hodnocení kvality
    def EvaluationPersonUpdate(self, ID_Login, ID, Answers=None):
        return self._client.service.EvaluationPersonUpdate({"ID_Login": ID_Login, "ID": ID, "Answers": Answers})

    # Načíst číselný přehled hodnocení
    def EvaluationSectionAllEvaluation(self, ID_Login, ID_Evaluation):
        return self._client.service.EvaluationSectionAllEvaluation({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation})

    # Načíst graf s váhami bodů vize dané oblasti
    def EvaluationSectionDetailGraphCriteriaWeight(self, ID_Login, ID, ID_Evaluation, GraphColor=None):
        return self._client.service.EvaluationSectionDetailGraphCriteriaWeight({"ID_Login": ID_Login, "ID": ID, "ID_Evaluation": ID_Evaluation, "GraphColor": GraphColor})

    # Načíst číselný přehled hodnocení
    def EvaluationSetAllEvaluation(self, ID_Login, ID_Evaluation):
        return self._client.service.EvaluationSetAllEvaluation({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation})

    # Načíst seznam základních typů hodnocení kvality
    def EvaluationSubtypeAllType(self, ID_Login, EvaluationTypeID=None):
        return self._client.service.EvaluationSubtypeAllType({"ID_Login": ID_Login, "EvaluationTypeID": EvaluationTypeID})

    # Načíst seznam celkových hodnocení
    def RatingAll(self, ID_Login, DisplayName=None):
        return self._client.service.RatingAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit celkové hodnocení
    def RatingUpdate(self, ID_Login, ID, ScoreFrom, ScoreTo, DisplayName=None, Color=None):
        return self._client.service.RatingUpdate({"ID_Login": ID_Login, "ID": ID, "ScoreFrom": ScoreFrom, "ScoreTo": ScoreTo, "DisplayName": DisplayName, "Color": Color})

    # Věřejná sumarizovaná data hodnocení kvality
    def EvaluationSummaryPublic(self, ID_Login, Year, ID_EvaluationSubtype, ID_UnitArray=None, ID_UnitType=None):
        return self._client.service.EvaluationSummaryPublic({"ID_Login": ID_Login, "Year": Year, "ID_EvaluationSubtype": ID_EvaluationSubtype, "ID_UnitArray": ID_UnitArray, "ID_UnitType": ID_UnitType})

    # Detailní výsledek hodnocení kvality
    def EvaluationAnswerAllResult(self, ID_Login, ID_Evaluation):
        return self._client.service.EvaluationAnswerAllResult({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation})

    # Založit hodnocení kvality akce
    def EvaluationInsertEvent(self, ID_Login, ID, ID_EvaluationSubtype, EvaluationCount, ID_EvaluationVersion, ID_Unit, ID_Event, ID_EventParent, Year, DateLastUpdate, ID_PersonClose, DateClose, Score, ID_EvaluationRating, HideDetail, EvaluationSubtype=None, Description=None, EvaluationVersion=None, Unit=None, RegistrationNumber=None, Event=None, ID_EvaluationState=None, EvaluationState=None, Note=None, NoteParent=None, PersonClose=None, EvaluationRating=None, Color=None, ID_UnitType=None, UnitType=None):
        return self._client.service.EvaluationInsertEvent({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationCount": EvaluationCount, "ID_EvaluationVersion": ID_EvaluationVersion, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_EventParent": ID_EventParent, "Year": Year, "DateLastUpdate": DateLastUpdate, "ID_PersonClose": ID_PersonClose, "DateClose": DateClose, "Score": Score, "ID_EvaluationRating": ID_EvaluationRating, "HideDetail": HideDetail, "EvaluationSubtype": EvaluationSubtype, "Description": Description, "EvaluationVersion": EvaluationVersion, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Event": Event, "ID_EvaluationState": ID_EvaluationState, "EvaluationState": EvaluationState, "Note": Note, "NoteParent": NoteParent, "PersonClose": PersonClose, "EvaluationRating": EvaluationRating, "Color": Color, "ID_UnitType": ID_UnitType, "UnitType": UnitType})

    # Načíst seznam hodnocení kvality akcí
    def EvaluationAllEvent(self, ID_Login, Year, NotExists, ID_EvaluationState=None, Unit=None, ID_EventType=None):
        return self._client.service.EvaluationAllEvent({"ID_Login": ID_Login, "Year": Year, "NotExists": NotExists, "ID_EvaluationState": ID_EvaluationState, "Unit": Unit, "ID_EventType": ID_EventType})

    # Načíst seznam akcí posunů
    def EvaluationAnswerAllShift(self, ID_Login, ID_Evaluation, ID_EvaluationSection, Count, RowMin):
        return self._client.service.EvaluationAnswerAllShift({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation, "ID_EvaluationSection": ID_EvaluationSection, "Count": Count, "RowMin": RowMin})

    # Výsledky hodnocení kvality pohled na regiony
    def EvaluationSummaryRegion(self, ID_Login, Year, ID_EvaluationSubtype, ID_UnitType=None):
        return self._client.service.EvaluationSummaryRegion({"ID_Login": ID_Login, "Year": Year, "ID_EvaluationSubtype": ID_EvaluationSubtype, "ID_UnitType": ID_UnitType})

    # Otevřít hodnocení
    def EvaluationUpdateOpen(self, ID_Login, ID, ID_EvaluationSubtype, EvaluationCount, ID_EvaluationVersion, ID_Unit, ID_Event, ID_EventParent, Year, DateLastUpdate, ID_PersonClose, DateClose, Score, ID_EvaluationRating, HideDetail, EvaluationSubtype=None, Description=None, EvaluationVersion=None, Unit=None, RegistrationNumber=None, Event=None, ID_EvaluationState=None, EvaluationState=None, Note=None, NoteParent=None, PersonClose=None, EvaluationRating=None, Color=None, ID_UnitType=None, UnitType=None):
        return self._client.service.EvaluationUpdateOpen({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationCount": EvaluationCount, "ID_EvaluationVersion": ID_EvaluationVersion, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_EventParent": ID_EventParent, "Year": Year, "DateLastUpdate": DateLastUpdate, "ID_PersonClose": ID_PersonClose, "DateClose": DateClose, "Score": Score, "ID_EvaluationRating": ID_EvaluationRating, "HideDetail": HideDetail, "EvaluationSubtype": EvaluationSubtype, "Description": Description, "EvaluationVersion": EvaluationVersion, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Event": Event, "ID_EvaluationState": ID_EvaluationState, "EvaluationState": EvaluationState, "Note": Note, "NoteParent": NoteParent, "PersonClose": PersonClose, "EvaluationRating": EvaluationRating, "Color": Color, "ID_UnitType": ID_UnitType, "UnitType": UnitType})

    # Uzavřít hodnocení
    def EvaluationUpdateClose(self, ID_Login, ID, ID_EvaluationSubtype, EvaluationCount, ID_EvaluationVersion, ID_Unit, ID_Event, ID_EventParent, Year, DateLastUpdate, ID_PersonClose, DateClose, Score, ID_EvaluationRating, HideDetail, EvaluationSubtype=None, Description=None, EvaluationVersion=None, Unit=None, RegistrationNumber=None, Event=None, ID_EvaluationState=None, EvaluationState=None, Note=None, NoteParent=None, PersonClose=None, EvaluationRating=None, Color=None, ID_UnitType=None, UnitType=None):
        return self._client.service.EvaluationUpdateClose({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationCount": EvaluationCount, "ID_EvaluationVersion": ID_EvaluationVersion, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_EventParent": ID_EventParent, "Year": Year, "DateLastUpdate": DateLastUpdate, "ID_PersonClose": ID_PersonClose, "DateClose": DateClose, "Score": Score, "ID_EvaluationRating": ID_EvaluationRating, "HideDetail": HideDetail, "EvaluationSubtype": EvaluationSubtype, "Description": Description, "EvaluationVersion": EvaluationVersion, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Event": Event, "ID_EvaluationState": ID_EvaluationState, "EvaluationState": EvaluationState, "Note": Note, "NoteParent": NoteParent, "PersonClose": PersonClose, "EvaluationRating": EvaluationRating, "Color": Color, "ID_UnitType": ID_UnitType, "UnitType": UnitType})

    # Seznam let, ve kterých jsou hodnocení kvality k dispozici
    def EvaluationAllYear(self, ID_Login):
        return self._client.service.EvaluationAllYear({"ID_Login": ID_Login})

    # Načíst seznam hodnocení kvality jednoty
    def EvaluationAllUnit(self, ID_Login, Year, NotExists, ID_EvaluationState=None, Unit=None):
        return self._client.service.EvaluationAllUnit({"ID_Login": ID_Login, "Year": Year, "NotExists": NotExists, "ID_EvaluationState": ID_EvaluationState, "Unit": Unit})

    # Načíst seznam odpovědí hodnocení kvality
    def EvaluationAnswerAll(self, ID_Login, ID_Evaluation, EvaluationPersonCount):
        return self._client.service.EvaluationAnswerAll({"ID_Login": ID_Login, "ID_Evaluation": ID_Evaluation, "EvaluationPersonCount": EvaluationPersonCount})

    # Načíst detail hodnocení kvality
    def EvaluationDetail(self, ID_Login, ID, ID_EvaluationPerson):
        return self._client.service.EvaluationDetail({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationPerson": ID_EvaluationPerson})

    # Založit hodnocení kvality
    def EvaluationInsert(self, ID_Login, ID, ID_EvaluationSubtype, EvaluationCount, ID_EvaluationVersion, ID_Unit, ID_Event, ID_EventParent, Year, DateLastUpdate, ID_PersonClose, DateClose, Score, ID_EvaluationRating, HideDetail, EvaluationSubtype=None, Description=None, EvaluationVersion=None, Unit=None, RegistrationNumber=None, Event=None, ID_EvaluationState=None, EvaluationState=None, Note=None, NoteParent=None, PersonClose=None, EvaluationRating=None, Color=None, ID_UnitType=None, UnitType=None):
        return self._client.service.EvaluationInsert({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationCount": EvaluationCount, "ID_EvaluationVersion": ID_EvaluationVersion, "ID_Unit": ID_Unit, "ID_Event": ID_Event, "ID_EventParent": ID_EventParent, "Year": Year, "DateLastUpdate": DateLastUpdate, "ID_PersonClose": ID_PersonClose, "DateClose": DateClose, "Score": Score, "ID_EvaluationRating": ID_EvaluationRating, "HideDetail": HideDetail, "EvaluationSubtype": EvaluationSubtype, "Description": Description, "EvaluationVersion": EvaluationVersion, "Unit": Unit, "RegistrationNumber": RegistrationNumber, "Event": Event, "ID_EvaluationState": ID_EvaluationState, "EvaluationState": EvaluationState, "Note": Note, "NoteParent": NoteParent, "PersonClose": PersonClose, "EvaluationRating": EvaluationRating, "Color": Color, "ID_UnitType": ID_UnitType, "UnitType": UnitType})

    # Načíst seznam celkových číselných hodnocení
    def EvaluationRatingAll(self, ID_Login, ID_EvaluationVersion, DisplayName=None):
        return self._client.service.EvaluationRatingAll({"ID_Login": ID_Login, "ID_EvaluationVersion": ID_EvaluationVersion, "DisplayName": DisplayName})

    # Smazat celkové číselné hodnocení
    def EvaluationRatingDelete(self, ID_Login, ID):
        return self._client.service.EvaluationRatingDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit celkové číselné hodnocení
    def EvaluationRatingInsert(self, ID_Login, ID, ID_EvaluationVersion, ScoreFrom, ScoreTo, DisplayName=None):
        return self._client.service.EvaluationRatingInsert({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationVersion": ID_EvaluationVersion, "ScoreFrom": ScoreFrom, "ScoreTo": ScoreTo, "DisplayName": DisplayName})

    # Upravit celkové ?íselné hodnocení
    def EvaluationRatingUpdate(self, ID_Login, ID, ID_EvaluationVersion, ScoreFrom, ScoreTo, DisplayName=None):
        return self._client.service.EvaluationRatingUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationVersion": ID_EvaluationVersion, "ScoreFrom": ScoreFrom, "ScoreTo": ScoreTo, "DisplayName": DisplayName})

    # Načíst seznam stavů hodnocení kvality
    def EvaluationStateAll(self, ID_Login, DisplayName=None):
        return self._client.service.EvaluationStateAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Upravit hodnocení kvality
    def EvaluationUpdate(self, ID_Login, ID, Answers=None):
        return self._client.service.EvaluationUpdate({"ID_Login": ID_Login, "ID": ID, "Answers": Answers})

    # Otevřít publikovanou verzi typu pro úpravy
    def EvaluationVersionInsertEvaluationSubtype(self, ID_Login, ID_EvaluationSubtype):
        return self._client.service.EvaluationVersionInsertEvaluationSubtype({"ID_Login": ID_Login, "ID_EvaluationSubtype": ID_EvaluationSubtype})

    # Otevřít publikovanou verzi typu pro úpravy
    def EvaluationSubtypeUpdateOpen(self, ID_Login, ID):
        return self._client.service.EvaluationSubtypeUpdateOpen({"ID_Login": ID_Login, "ID": ID})

    # Upravit typ hodnocení kvality
    def EvaluationSubtypeUpdate(self, ID_Login, ID, ID_EventEducationType, ID_EvaluationVersion, DisplayName=None, ID_UnitType=None, UnitType=None, ID_EventType=None, EventType=None, EventEducationType=None, Description=None, Note=None):
        return self._client.service.EvaluationSubtypeUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "ID_EvaluationVersion": ID_EvaluationVersion, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "ID_EventType": ID_EventType, "EventType": EventType, "EventEducationType": EventEducationType, "Description": Description, "Note": Note})

    # Načíst seznam kritérií hodnocení
    def EvaluationCriteriaAll(self, ID_Login, ID_EvaluationSet, DisplayName=None):
        return self._client.service.EvaluationCriteriaAll({"ID_Login": ID_Login, "ID_EvaluationSet": ID_EvaluationSet, "DisplayName": DisplayName})

    # Smazat kritérium hodnocení
    def EvaluationCriteriaDelete(self, ID_Login, ID):
        return self._client.service.EvaluationCriteriaDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail kritéria hodnocení
    def EvaluationCriteriaDetail(self, ID_Login, ID):
        return self._client.service.EvaluationCriteriaDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit kritérium hodnocení
    def EvaluationCriteriaInsert(self, ID_Login, ID, ID_EvaluationSet, Order, Weight, EvaluationSet=None, DisplayName=None, Answer1=None, Shift1=None, Answer2=None, Shift2=None, Answer3=None, Shift3=None, Answer4=None, Note=None, ID_EvaluationVersionState=None, EvaluationVersionState=None):
        return self._client.service.EvaluationCriteriaInsert({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSet": ID_EvaluationSet, "Order": Order, "Weight": Weight, "EvaluationSet": EvaluationSet, "DisplayName": DisplayName, "Answer1": Answer1, "Shift1": Shift1, "Answer2": Answer2, "Shift2": Shift2, "Answer3": Answer3, "Shift3": Shift3, "Answer4": Answer4, "Note": Note, "ID_EvaluationVersionState": ID_EvaluationVersionState, "EvaluationVersionState": EvaluationVersionState})

    # Upravit kritérium hodnocení
    def EvaluationCriteriaUpdate(self, ID_Login, ID, ID_EvaluationSet, Order, Weight, EvaluationSet=None, DisplayName=None, Answer1=None, Shift1=None, Answer2=None, Shift2=None, Answer3=None, Shift3=None, Answer4=None, Note=None, ID_EvaluationVersionState=None, EvaluationVersionState=None):
        return self._client.service.EvaluationCriteriaUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSet": ID_EvaluationSet, "Order": Order, "Weight": Weight, "EvaluationSet": EvaluationSet, "DisplayName": DisplayName, "Answer1": Answer1, "Shift1": Shift1, "Answer2": Answer2, "Shift2": Shift2, "Answer3": Answer3, "Shift3": Shift3, "Answer4": Answer4, "Note": Note, "ID_EvaluationVersionState": ID_EvaluationVersionState, "EvaluationVersionState": EvaluationVersionState})

    # Smazat oblast kvality
    def EvaluationSectionDelete(self, ID_Login, ID):
        return self._client.service.EvaluationSectionDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail oblasti kvality
    def EvaluationSectionDetail(self, ID_Login, ID):
        return self._client.service.EvaluationSectionDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit oblast kvality
    def EvaluationSectionInsert(self, ID_Login, ID, ID_EvaluationVersion, Order, Weight, ID_EvaluationSubtype, DisplayName=None, Note=None, Description=None, EvaluationSubtype=None, Color=None):
        return self._client.service.EvaluationSectionInsert({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationVersion": ID_EvaluationVersion, "Order": Order, "Weight": Weight, "ID_EvaluationSubtype": ID_EvaluationSubtype, "DisplayName": DisplayName, "Note": Note, "Description": Description, "EvaluationSubtype": EvaluationSubtype, "Color": Color})

    # Upravit oblast kvality
    def EvaluationSectionUpdate(self, ID_Login, ID, ID_EvaluationVersion, Order, Weight, ID_EvaluationSubtype, DisplayName=None, Note=None, Description=None, EvaluationSubtype=None, Color=None):
        return self._client.service.EvaluationSectionUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationVersion": ID_EvaluationVersion, "Order": Order, "Weight": Weight, "ID_EvaluationSubtype": ID_EvaluationSubtype, "DisplayName": DisplayName, "Note": Note, "Description": Description, "EvaluationSubtype": EvaluationSubtype, "Color": Color})

    # Načíst seznam skupin kritérií
    def EvaluationSetAll(self, ID_Login, ID_EvaluationVersion, DisplayName=None):
        return self._client.service.EvaluationSetAll({"ID_Login": ID_Login, "ID_EvaluationVersion": ID_EvaluationVersion, "DisplayName": DisplayName})

    # Smazat skupinu kritérií
    def EvaluationSetDelete(self, ID_Login, ID):
        return self._client.service.EvaluationSetDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail bodu vize
    def EvaluationSetDetail(self, ID_Login, ID):
        return self._client.service.EvaluationSetDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit skupinu kritérií
    def EvaluationSetInsert(self, ID_Login, ID, ID_EvaluationSection, Order, Weight, ID_EvaluationSubtype, EvaluationSection=None, DisplayName=None, Note=None, Description=None):
        return self._client.service.EvaluationSetInsert({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSection": ID_EvaluationSection, "Order": Order, "Weight": Weight, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationSection": EvaluationSection, "DisplayName": DisplayName, "Note": Note, "Description": Description})

    # Upravit skupinu kritérií
    def EvaluationSetUpdate(self, ID_Login, ID, ID_EvaluationSection, Order, Weight, ID_EvaluationSubtype, EvaluationSection=None, DisplayName=None, Note=None, Description=None):
        return self._client.service.EvaluationSetUpdate({"ID_Login": ID_Login, "ID": ID, "ID_EvaluationSection": ID_EvaluationSection, "Order": Order, "Weight": Weight, "ID_EvaluationSubtype": ID_EvaluationSubtype, "EvaluationSection": EvaluationSection, "DisplayName": DisplayName, "Note": Note, "Description": Description})

    # Načíst seznam typů hodnocení kvality
    def EvaluationSubtypeAll(self, ID_Login, ID_EvaluationVersion, IsEvent, IsPublished, DisplayName=None, ID_UnitType=None, ID_EventType=None):
        return self._client.service.EvaluationSubtypeAll({"ID_Login": ID_Login, "ID_EvaluationVersion": ID_EvaluationVersion, "IsEvent": IsEvent, "IsPublished": IsPublished, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType, "ID_EventType": ID_EventType})

    # Smazat typ hodnocení kvality
    def EvaluationSubtypeDelete(self, ID_Login, ID):
        return self._client.service.EvaluationSubtypeDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail typu hodnocení kvality
    def EvaluationSubtypeDetail(self, ID_Login, ID):
        return self._client.service.EvaluationSubtypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit typ hodnocení kvality
    def EvaluationSubtypeInsert(self, ID_Login, ID, ID_EventEducationType, ID_EvaluationVersion, DisplayName=None, ID_UnitType=None, UnitType=None, ID_EventType=None, EventType=None, EventEducationType=None, Description=None, Note=None):
        return self._client.service.EvaluationSubtypeInsert({"ID_Login": ID_Login, "ID": ID, "ID_EventEducationType": ID_EventEducationType, "ID_EvaluationVersion": ID_EvaluationVersion, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType, "UnitType": UnitType, "ID_EventType": ID_EventType, "EventType": EventType, "EventEducationType": EventEducationType, "Description": Description, "Note": Note})

    # Publikovat rozpracovanou verzi typu
    def EvaluationSubtypeUpdatePublish(self, ID_Login, ID):
        return self._client.service.EvaluationSubtypeUpdatePublish({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam verzí typu hodnocení kvality
    def EvaluationVersionAll(self, ID_Login, ID_EvaluationSubtype, ID_EvaluationVersionState=None):
        return self._client.service.EvaluationVersionAll({"ID_Login": ID_Login, "ID_EvaluationSubtype": ID_EvaluationSubtype, "ID_EvaluationVersionState": ID_EvaluationVersionState})

    # Přepočítat výsledky hodnocení kvality
    def EvaluationVersionUpdateCache(self, ID_Login, ID):
        return self._client.service.EvaluationVersionUpdateCache({"ID_Login": ID_Login, "ID": ID})

