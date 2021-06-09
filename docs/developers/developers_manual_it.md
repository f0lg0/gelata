# GELATA - Manuale sviluppatore

In questo manuale verrà analizzata l'infrastruttura del `GEstore delLe Attività aTA`.

## Table of contents

-   [Requirements](#Requirements)
-   [Setup](#Setup)
-   [Run](#Run)
-   [Infrastruttura](#Infrastruttura)

## Requirements

-   Python 3.x
-   pip
-   virtualenv

## Setup

### 1. Scaricare il progetto

Scarica questa repository localmente.

### 2. Creazione ambiente virtuale python

Aprire un terminale (Powershell su Windows) e lanciare i seguenti comandi:

Installazione del pacchetto `virtualenv`

```
pip install virtualenv
```

Creazione dell'ambiente virtuale

```
virtualenv .venv
```

Attivazione dell'ambiente appena creato:

Su una piattaforma Windows lanciare:

```
.venv\env\Scripts\activate.bat
```

Su ambienti Linux:

```
source .venv/bin/activate
```

### 3. Installazione requisiti Python:

```
pip install -r requirements.txt
```

### 5. Creazione del file di ambiente

Creare un file nominato `.env` e popolarlo con le credenziali dell'API OAuth di Google (al momento l'applicazione è registrata sotto il dominio di 12212-g@capirla.com)

## Run

In un terminale, cambiare directoy per andare in `/src/webserver` e lanciare il file `main.py`:

```
python main.py
```

In un secondo lancio futuro sarà necessario solamente attivare l'ambiente virtuale e lanciare il file `main.py`.

## Infrastruttura generale

Il quadro high-level dell'infrastruttura si presenta nel seguente modo:

```
clients <----> Apache:80 <----> Webserver:5000 <----> SQLite Database
```

Il `Webserver` è il cuore del sito: serve i file statici agli utenti e si interfaccia al database tutto grazie a `Flask`.

### Techstack

-   HTML, CSS e Vanilla JS nel frontend

-   Python e Flask nel backend

-   SQLite3 come database relazionale

### Overview

Di seguito viene riportato il diagramma dei blocchi funzionali:

![blocchi](https://raw.githubusercontent.com/f0lg0/gelata/main/docs/infrastruttura/out/blocchi_funzionali.png)

Il punto di partenza è il file `main`, accompagnato dai blueprints di Flask (vedi documentazione Flask), dal modulo per la logica degli utenti, dal modulo per la logica del Database e dal Watchdog (servizio per il mantenimento dei logs a livello database).


## Albero cartelle del progetto

```
docs/

src/
    database/
        README.md
    webserver/
        authorization/
            user_session.py
        db/
            database_generator.py
            database_ops.py
            db_setup_queries.py
            watchdog.py
        interventi_handler/
            interventi.py
        oauth/
            login_required.py
            oauth_wrapper.py
        web/
            static/
                css/
                    carica.css
                    home.css
                    profilo.css
                js/
                    components/
                        intervento_card.js
                        navbar.js
                    set_profile_pic.js
            templates/
                carica.html
                home.html
                login.html
                profilo.html
        main.py
.gitignore

LICENSE

README.md

requirements.txt
```
