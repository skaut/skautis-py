# SkautIS
Python knihovna pro připojení do [Skautisu](https://is.skaut.cz/)

**Knihovna je automaticky generovaná s limitovaným testováním a může tedy obsahovat chyby.**

Pokud na nějakou narazíte, případně máte nápad na vylepšení generování, určitě dejte vědět. Nicméně vzhledem k jednoduché architektuře a stáří projektu jsou chyby nepravděpodobné.

## Instalace a použití
Knihovna se instaluje pomocí setup scriptu:

    python setup.py install

Po instalaci stačí zavolat `SkautisApi` s klíčem aplikace, nad kterým se dají poté volat jednotlivé operace.
Všechna volání jsou ve formátu: `skautis.<webservice>.<operation>(args)`.

Seznam možných volání je na adrese https://is.skaut.cz/JunakWebservice/.

Složka `example` obsahuje jednoduchou aplikaci, která ukazuje základní využití knihovny jako je přihlášení, získání dat o uživateli a odhlášení.

### Příklad použití
```python
skautis = SkautisApi(SKAUTIS_APPID, test=True)
...
// načtení informací o uživateli
user_info = skautis.UserManagement.UserDetail(skautis_token, None)

// získání logout linku
logout_link = skautis.get_logout_url(skautis_token)
```
