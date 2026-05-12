# Peace Pizza

## Om Peace Pizza

Peace Pizza er en fiktiv pizzabutikk lokalisert i hjertet av Oslo. Vi tilbyr autentisk italiensk pizza laget etter tradisjonelle oppskrifter med ferske, lokale ingredienser. Butikken er kjent for sitt rolige miljø, venlig betjening og deilige pizzaer som bringer fred og ro til våre kunder.

## Om Prosjektet

Dette prosjektet er en funksjonsrik nettside for Peace Pizza. Målet er å lage en komplett e-handel-løsning der kunder kan:

- Browsing menu og se tilgjengelige pizzaer
- Legge pizzaer i handlevogn
- Gjøre bestillinger online
- Spore bestillingsstatus

### Teknologi Stack

- **Backend**: Flask (Python)
- **Database**: MariaDB
- **Frontend**: HTML, CSS, JavaScript
- **Server**: Flask development/production server
- **Hardware**: Raspberry Pi for hosting av database og server

### Arkitektur

Prosjektet benytter en klassisk tre-lags arkitektur:

1. **Presentasjonslag** - Web-grensesnitt for brukere
2. **Applikasjonslag** - Flask server som håndterer forretningslogikk
3. **Datalagsystem** - MariaDB database for lagring av produkter, bestillinger og kundedata

Databasen lagrer informasjon om pizzaer, ingredienser, bestillinger og kundehistorikk, mens Flask-serveren håndterer API-er og serverlogikk.

## Se og prøv prosjektet på din egen pc

Du kan se prosjektet gjennom lenken https://github.com/akselkirk/prosjekt_eksempel og prøve det ut med gjøre `git clone https://github.com/akselkirk/prosjekt_eksempel` request i terminalen.
