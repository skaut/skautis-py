import json
import uuid
import zeep

class Vivant(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Vivant.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Vivant.asmx?wsdl')

    def ExportFileAll(self, idLogin, ID, ID_ExportFileState):
        struct = self._client.get_type('ns0:ExportFileAllInput')
        order = struct(ID_Login=idLogin, ID=ID, ID_ExportFileState=ID_ExportFileState)

        result = self._client.service.ExportFileAll(order)
        return result

#ExportFileDetailDownload(exportFileDetailDownloadInput: ns0:ExportFileDetailDownloadInput) -> ExportFileDetailDownloadResult: ns0:ExportFile
#ExportFileGenerate(exportFile: ns0:ExportFile) -> 
#ExportFileInsert(exportFile: ns0:ExportFile) -> ExportFileInsertResult: ns0:ExportFileInsertOutput
#ExportFileUpdate(exportFile: ns0:ExportFile) -> ExportFileUpdateResult: ns0:ExportFileUpdateOutput    
