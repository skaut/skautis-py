from requests.utils import quote
from .userManagement import UserManagement
from .vivant import Vivant

class SkautisApi(object):
    def __init__(self, appId, test=False):
        self._appId = appId
        self._test = test

        self.userManagement = UserManagement(test)
        self.vivant = Vivant(test)

    def get_login_url(self):
        if self._test:
            return "https://test-is.skaut.cz/Login/?appid={}".format(self._appId)
        return "https://is.skaut.cz/Login/?appid={}".format(self._appId)
