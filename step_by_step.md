# Gjennomførings plan

Planen er delt inn i seks faser. Hvert kulepunkt er ment å være lite nok til å bli et eget GitHub issue (1–4 timers arbeid).

## 1. Prosjektoppsett

- Opprette `.gitignore` for Python (venv, `__pycache__`, `.env`, IDE-filer)
- Sette opp `venv` og dokumentere aktiveringskommando i README
- Lage `requirements.txt` med startavhengigheter:
  - Flask
  - `mariadb` eller `PyMySQL` (database-driver)
  - `python-dotenv` (miljøvariabler)
  - `Flask-WTF` (skjema og CSRF)
  - `gunicorn` (produksjonsserver)
- Definere mappestruktur: `app/`, `app/templates/`, `app/static/`, `app/routes/`, `app/models/`, `tests/`, `db/`
- Lage `.env.example` med nøkler for `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `FLASK_SECRET_KEY`
- Skrive `run.py` som starter Flask-appen via application factory

## 2. Database (datalagsystem)

### Design
- Tegne UML/ER-diagram med entitetene: `Kunde`, `Pizza`, `Ingrediens`, `PizzaIngrediens`, `Bestilling`, `Bestillingslinje`, `Bestillingsstatus`
- Definere relasjoner og kardinaliteter (én kunde → mange bestillinger, mange pizzaer ↔ mange ingredienser)
- Bestemme primær- og fremmednøkler, samt indekser på `bestilling.kunde_id` og `bestilling.status`
- Legge UML-diagram i `db/diagram.png` og referere det fra README

### Oppsett av MariaDB på Raspberry Pi
- Installere MariaDB-server på Raspberry Pi og åpne port 3306 for lokalt nett
- Opprette database `peace_pizza`
- Opprette tre databasebrukere med minimumstilgang:
  - `pp_app` (SELECT/INSERT/UPDATE på alle tabeller)
  - `pp_admin` (full tilgang, brukes til migrasjoner)
  - `pp_readonly` (SELECT, brukes til rapporter)
- Dokumentere tilkoblingsstrengen i `README.md` (uten passord)

### Skjema og data
- Skrive `db/schema.sql` med `CREATE TABLE`-setninger basert på UML
- Skrive `db/seed.sql` med 8–10 eksempelpizzaer og tilhørende ingredienser
- Skrive `db/statuser.sql` som fyller `Bestillingsstatus` (mottatt, tilberedes, klar, levert)
- Lage Python-skript `db/init_db.py` som kjører schema + seed mot konfigurert database

## 3. Backend (applikasjonslag)

### Grunnstruktur
- Implementere application factory i `app/__init__.py`
- Implementere `app/db.py` med tilkoblingspool og `get_db()`-funksjon
- Sette opp sentralisert feilhåndtering (404, 500) som returnerer JSON for API og HTML for sider
- Sette opp logging til fil og stdout

### API-endepunkter
- `GET /api/pizzaer` — returnerer hele menyen med ingredienser
- `GET /api/pizzaer/<id>` — detaljer for én pizza
- `POST /api/handlevogn` — legger pizza i handlevogn (sesjonsbasert)
- `GET /api/handlevogn` — henter innholdet i handlevognen
- `DELETE /api/handlevogn/<linje_id>` — fjerner en linje
- `POST /api/bestillinger` — oppretter bestilling fra handlevogn, returnerer bestillings-ID
- `GET /api/bestillinger/<id>` — henter status og innhold for en bestilling

### Forretningslogikk
- Validere at alle pizzaer i en bestilling finnes og er tilgjengelige
- Beregne totalpris på serversiden (aldri stole på frontend-pris)
- Generere unik sporingskode per bestilling
- Skrive enhetstester for prisberegning og validering i `tests/`

## 4. Frontend (presentasjonslag)

- Lage `base.html` med navigasjon, footer og felles CSS
- Lage menyside `index.html` som henter `/api/pizzaer` og viser kort per pizza
- Lage handlevogn-side med mulighet for å endre antall og fjerne linjer
- Lage kasse-side med skjema for navn, telefon, adresse
- Lage sporingsside `/spor/<kode>` som viser bestillingsstatus
- Skrive `static/css/style.css` med en enkel, ren stil (mobil først)
- Skrive `static/js/handlevogn.js` for klient-side oppdateringer

## 5. Deployment

- Sette opp systemd-service for Flask-appen på Raspberry Pi
- Konfigurere `gunicorn` med 2–3 workers bak `nginx` som reverse proxy
- Sette opp HTTPS med Let's Encrypt
- Skrive backup-skript som tar daglig `mysqldump` av databasen
- Dokumentere oppstart, stopp og logginspeksjon i `README.md`

## 6. Testing og QA

- Skrive enhetstester for modeller og forretningslogikk (pytest)
- Skrive integrasjonstester som kjører mot en testdatabase
- Manuell testjekkliste: bestille pizza fra start til slutt, sjekke sporing
- Sette opp GitHub Actions som kjører `pytest` på hver PR
