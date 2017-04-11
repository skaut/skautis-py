# -*- coding: utf-8 -*-

import zeep

# Exporty pro Vivant
class Vivant(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Vivant.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Vivant.asmx?wsdl')

    # Načíst seznam exportovaných souborů
    def ExportFileAll(self, ID_Login, ID, ID_ExportFileState=None):
        return self._client.service.ExportFileAll({"ID_Login": ID_Login, "ID": ID, "ID_ExportFileState": ID_ExportFileState})

    # Stáhnout exportovaný soubor
    def ExportFileDetailDownload(self, ID_Login, ID):
        return self._client.service.ExportFileDetailDownload({"ID_Login": ID_Login, "ID": ID})

    # Vygenerovat export pro vivant
    def ExportFileGenerate(self, ID_Login, ID, Year, DateGenerate, DateDownload, ID_ExportFileState=None, ExportFileState=None, Content=None):
        return self._client.service.ExportFileGenerate({"ID_Login": ID_Login, "ID": ID, "Year": Year, "DateGenerate": DateGenerate, "DateDownload": DateDownload, "ID_ExportFileState": ID_ExportFileState, "ExportFileState": ExportFileState, "Content": Content})

    # Založit exportovaný souboru
    def ExportFileInsert(self, ID_Login, ID, Year, DateGenerate, DateDownload, ID_ExportFileState=None, ExportFileState=None, Content=None):
        return self._client.service.ExportFileInsert({"ID_Login": ID_Login, "ID": ID, "Year": Year, "DateGenerate": DateGenerate, "DateDownload": DateDownload, "ID_ExportFileState": ID_ExportFileState, "ExportFileState": ExportFileState, "Content": Content})

    # Upravit exportovaný souboru
    def ExportFileUpdate(self, ID_Login, ID, Year, DateGenerate, DateDownload, ID_ExportFileState=None, ExportFileState=None, Content=None):
        return self._client.service.ExportFileUpdate({"ID_Login": ID_Login, "ID": ID, "Year": Year, "DateGenerate": DateGenerate, "DateDownload": DateDownload, "ID_ExportFileState": ID_ExportFileState, "ExportFileState": ExportFileState, "Content": Content})

