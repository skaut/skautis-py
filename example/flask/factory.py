class SkautisApi:

    def init_app(self, app):
        appId = app.config.setdefault("SKAUTIS_APPID", None)
        test = app.config.setdefault("SKAUTIS_TEST", False)
        from skautis import SkautisApi as _SkautisApi
        self._skautis = _SkautisApi(appId, test)

    def __getattr__(self, name):
        if not self._skautis:
            raise RuntimeError("init_app was never called.")
        return getattr(self._skautis, name)
