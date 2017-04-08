import json
import requests
import zeep

class UserManagement(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/UserManagement.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/UserManagement.asmx?wsdl')

    def ActionAll(self, idLogin):
        #result = self._client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour')
        result = self._client.service.ActionAll()
        return result

    def TableArchive(self, idLogin):
        result = self._client.service.TableArchive(ID_Login=idLogin)
        return result        
