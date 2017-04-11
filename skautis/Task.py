# -*- coding: utf-8 -*-

import zeep

# Webová služba pro práci s úkoly ve skautISu
class Task(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Task.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Task.asmx?wsdl')

    # Načíst seznam nesplněných úkolů
    def PersonTaskAllAfterDeadline(self, ID_Login):
        return self._client.service.PersonTaskAllAfterDeadline({"ID_Login": ID_Login})

    # Načíst seznam úkolů osoby pro dotace
    def PersonTaskAllGrant(self, ID_Login, ID, ID_TaskType=None, DisplayName=None, ID_TaskAgenda=None, ID_TaskState=None):
        return self._client.service.PersonTaskAllGrant({"ID_Login": ID_Login, "ID": ID, "ID_TaskType": ID_TaskType, "DisplayName": DisplayName, "ID_TaskAgenda": ID_TaskAgenda, "ID_TaskState": ID_TaskState})

    # Načíst seznam úkolů osoby
    def PersonTaskAll(self, ID_Login, ID, Top, ID_TaskType=None, DisplayName=None, ID_TaskAgenda=None, ID_TaskState=None):
        return self._client.service.PersonTaskAll({"ID_Login": ID_Login, "ID": ID, "Top": Top, "ID_TaskType": ID_TaskType, "DisplayName": DisplayName, "ID_TaskAgenda": ID_TaskAgenda, "ID_TaskState": ID_TaskState})

    # Rozeslat specifické upomínky úkolu
    def PersonTaskUpdateReminderSpecific(self, ID_Login, ID):
        return self._client.service.PersonTaskUpdateReminderSpecific({"ID_Login": ID_Login, "ID": ID})

    # Rozeslat upomínky úkolu
    def PersonTaskUpdateReminder(self, ID_Login, ID):
        return self._client.service.PersonTaskUpdateReminder({"ID_Login": ID_Login, "ID": ID})

    # Načtení jednotek s nezadaným hospodářským výkazem a zadání úkolu
    def PersonTaskInsertStatementUnitCall(self, ID_Login):
        return self._client.service.PersonTaskInsertStatementUnitCall({"ID_Login": ID_Login})

    # Načíst detail úkolu osoby
    def PersonTaskDetail(self, ID_Login, ID):
        return self._client.service.PersonTaskDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam agend úkolů
    def TaskAgendaAll(self, ID_Login, ID=None, DisplayName=None):
        return self._client.service.TaskAgendaAll({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName})

