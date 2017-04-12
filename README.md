# SkautIS
Python knihovna pro připojení do [Skautisu](https://is.skaut.cz/)

## Instalace a použití
Knihovna se instaluje pomocí setup scriptu:

    python setup.py install

Po instalaci stačí zavolat `SkautisApi` s klíčem aplikace, nad kterým se dají poté volat jednotlivé operace.
Všechna volání jsou ve formátu: `skautis.<webservice>.<operation>(args)`.

Seznam možných volání se dají najít na https://is.skaut.cz/JunakWebservice/.

### Příklad použití
```
skautis = SkautisApi(SKAUTIS_APPID, test=True)
...
// načtení informací o uživateli
user_info = skautis.UserManagement.UserDetail(skautis_token, None)

// získání logout linku
logout_link = skautis.get_logout_url(skautis_token)
```
