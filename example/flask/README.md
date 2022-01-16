# Ukázka použití s Flask

Tato složka obsahuje jednoduchý příklad použití knihovny s web frameworkem Flask. Nainstalovat a spustit na portu `5000` se dá jednoduše takto:

```sh
python -m venv venv
./venv/bin/pip install -r requirements
./venv/bin/python run.py
```

Soubor `factory.py` obsahuje jednoduchý wrapper pro použití s [Flask factory patternem](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/). Pro jeho použití stačí`app.py` upravit následujícím způsobem:

```python
#from skautis import SkautisApi
#skautis = SkautisApi(app.config['SKAUTIS_APPID'], test=app.config['SKAUTIS_TEST'])

from factory import SkautisApi
skautis = SkautisApi()
skautis.init_app(app)
```
