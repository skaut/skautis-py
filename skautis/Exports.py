# -*- coding: utf-8 -*-

import zeep

# Webová služba pro export dat do jiných systémů
class Exports(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Exports.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Exports.asmx?wsdl')

    # Uložit tiskovou sestavu s exportovanými daty pro děkovné dopisy
    def ExportFunctionProlongationAll(self, ID_Login, Settings=None):
        return self._client.service.ExportFunctionProlongationAll({"ID_Login": ID_Login, "Settings": Settings})

    # děkovných dopisů
    def ExportFunctionProlongation(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportFunctionProlongation({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # děkovných dopisů
    def ExportFunctionEnd(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportFunctionEnd({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Uložit tiskovou sestavu s exportovanými daty pro děkovné dopisy
    def ExportFunctionEndAll(self, ID_Login, Settings=None):
        return self._client.service.ExportFunctionEndAll({"ID_Login": ID_Login, "Settings": Settings})

    # Uložit exportovaná data pro Google
    def ExportGoogle(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportGoogle({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Uložit tiskovou sestavu s exportovanými daty pro Google - změny
    def ExportGooogleAll(self, ID_Login, ID_ExportLog, Settings=None):
        return self._client.service.ExportGooogleAll({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "Settings": Settings})

    # Uložit exportovaná data pro Seznam.cz - změny
    def ExportSeznamChanges(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportSeznamChanges({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Uložit tiskovou sestavu s exportovanými daty pro Seznam.cz - změny
    def ExportSeznamChangesAll(self, ID_Login, ID_ExportLog, Settings=None):
        return self._client.service.ExportSeznamChangesAll({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "Settings": Settings})

    # jubilantů
    def ExportJubilant(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportJubilant({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Zapsat jméno souboru exportu
    def ExportLogUpdateFileName(self, ID_Login, ID, FileName=None):
        return self._client.service.ExportLogUpdateFileName({"ID_Login": ID_Login, "ID": ID, "FileName": FileName})

    # Odeslat export
    def ExportSend(self, ID_Login, ID, IsEnabled, Interval, IntervalMonth, DateNextRun, Success, DisplayName=None, Webservice=None, NameFormat=None, FileExtension=None, ID_MessageType=None, MessageType=None, Settings=None):
        return self._client.service.ExportSend({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "Interval": Interval, "IntervalMonth": IntervalMonth, "DateNextRun": DateNextRun, "Success": Success, "DisplayName": DisplayName, "Webservice": Webservice, "NameFormat": NameFormat, "FileExtension": FileExtension, "ID_MessageType": ID_MessageType, "MessageType": MessageType, "Settings": Settings})

    # Načíst seznam exportů dat
    def ExportAll(self, ID_Login, DisplayName=None):
        return self._client.service.ExportAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

    # Načíst seznam exportů dat
    def ExportAllReady(self, ID_Login):
        return self._client.service.ExportAllReady({"ID_Login": ID_Login})

    # Smazat export dat
    def ExportDelete(self, ID_Login, ID):
        return self._client.service.ExportDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail exportu dat
    def ExportDetail(self, ID_Login, ID, IsEnabled, Interval, IntervalMonth, DateNextRun, Success, DisplayName=None, Webservice=None, NameFormat=None, FileExtension=None, ID_MessageType=None, MessageType=None, Settings=None):
        return self._client.service.ExportDetail({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "Interval": Interval, "IntervalMonth": IntervalMonth, "DateNextRun": DateNextRun, "Success": Success, "DisplayName": DisplayName, "Webservice": Webservice, "NameFormat": NameFormat, "FileExtension": FileExtension, "ID_MessageType": ID_MessageType, "MessageType": MessageType, "Settings": Settings})

    # Založit export dat
    def ExportInsert(self, ID_Login, ID, IsEnabled, Interval, IntervalMonth, DateNextRun, Success, DisplayName=None, Webservice=None, NameFormat=None, FileExtension=None, ID_MessageType=None, MessageType=None, Settings=None):
        return self._client.service.ExportInsert({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "Interval": Interval, "IntervalMonth": IntervalMonth, "DateNextRun": DateNextRun, "Success": Success, "DisplayName": DisplayName, "Webservice": Webservice, "NameFormat": NameFormat, "FileExtension": FileExtension, "ID_MessageType": ID_MessageType, "MessageType": MessageType, "Settings": Settings})

    # Uložit data pro export pro kamchodit.cz
    def ExportKamChodit(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportKamChodit({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Načíst seznam spuštění exportu
    def ExportLogAll(self, ID_Login, ID_Export, ID_Error):
        return self._client.service.ExportLogAll({"ID_Login": ID_Login, "ID_Export": ID_Export, "ID_Error": ID_Error})

    # Načít detail spuštění exportu
    def ExportLogDetail(self, ID_Login, ID):
        return self._client.service.ExportLogDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit export dat
    def ExportLogUpdateResult(self, ID_Login, ID, Error=None, ErrorDescription=None):
        return self._client.service.ExportLogUpdateResult({"ID_Login": ID_Login, "ID": ID, "Error": Error, "ErrorDescription": ErrorDescription})

    # Uložit exportovaná data pro Seznam.cz
    def ExportSeznam(self, ID_Login, ID_ExportLog, NameFormat=None, Settings=None):
        return self._client.service.ExportSeznam({"ID_Login": ID_Login, "ID_ExportLog": ID_ExportLog, "NameFormat": NameFormat, "Settings": Settings})

    # Uložit tiskovou sestavu s exportovanými daty pro Seznam.cz
    def ExportSeznamAll(self, ID_Login, Settings=None):
        return self._client.service.ExportSeznamAll({"ID_Login": ID_Login, "Settings": Settings})

    # Načíst seznam příjemců exportu
    def ExportToAll(self, ID_Login, ID_Export, ID_Person):
        return self._client.service.ExportToAll({"ID_Login": ID_Login, "ID_Export": ID_Export, "ID_Person": ID_Person})

    # Smazat příjemce exportu
    def ExportToDelete(self, ID_Login, ID):
        return self._client.service.ExportToDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit příjemce exportu
    def ExportToInsert(self, ID_Login, ID, ID_Export, ID_Person, Email=None, Person=None):
        return self._client.service.ExportToInsert({"ID_Login": ID_Login, "ID": ID, "ID_Export": ID_Export, "ID_Person": ID_Person, "Email": Email, "Person": Person})

    # Upravit příjemce exportu
    def ExportToUpdate(self, ID_Login, ID, ID_Export, ID_Person, Email=None, Person=None):
        return self._client.service.ExportToUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Export": ID_Export, "ID_Person": ID_Person, "Email": Email, "Person": Person})

    # Upravit export dat
    def ExportUpdate(self, ID_Login, ID, IsEnabled, Interval, IntervalMonth, DateNextRun, Success, DisplayName=None, Webservice=None, NameFormat=None, FileExtension=None, ID_MessageType=None, MessageType=None, Settings=None):
        return self._client.service.ExportUpdate({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "Interval": Interval, "IntervalMonth": IntervalMonth, "DateNextRun": DateNextRun, "Success": Success, "DisplayName": DisplayName, "Webservice": Webservice, "NameFormat": NameFormat, "FileExtension": FileExtension, "ID_MessageType": ID_MessageType, "MessageType": MessageType, "Settings": Settings})

