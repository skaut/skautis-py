from .ApplicationManagement import ApplicationManagement
from .ContentManagement import ContentManagement
from .DocumentStorage import DocumentStorage
from .Evaluation import Evaluation
from .Events import Events
from .Exports import Exports
from .GoogleApps import GoogleApps
from .Grants import Grants
from .Insurance import Insurance
from .Journal import Journal
from .Material import Material
from .Message import Message
from .OrganizationUnit import OrganizationUnit
from .Power import Power
from .Reports import Reports
from .Summary import Summary
from .Task import Task
from .Telephony import Telephony
from .UserManagement import UserManagement
from .Vivant import Vivant
from .Welcome import Welcome

class SkautisApi(object):
    def __init__(self, appId, test=False):
        self._appId = appId
        self._test = test
        
        self.ApplicationManagement = ApplicationManagement(test)
        self.ContentManagement = ContentManagement(test)
        self.DocumentStorage = DocumentStorage(test)
        self.Evaluation = Evaluation(test)
        self.Events = Events(test)
        self.Exports = Exports(test)
        self.GoogleApps = GoogleApps(test)
        self.Grants = Grants(test)
        self.Insurance = Insurance(test)
        self.Journal = Journal(test)
        self.Material = Material(test)
        self.Message = Message(test)
        self.OrganizationUnit = OrganizationUnit(test)
        self.Power = Power(test)
        self.Reports = Reports(test)
        self.Summary = Summary(test)
        self.Task = Task(test)
        self.Telephony = Telephony(test)
        self.UserManagement = UserManagement(test)
        self.Vivant = Vivant(test)
        self.Welcome = Welcome(test)

    def get_login_url(self):
        if self._test:
            return "https://test-is.skaut.cz/Login/?appid={}".format(self._appId)
        return "https://is.skaut.cz/Login/?appid={}".format(self._appId)
