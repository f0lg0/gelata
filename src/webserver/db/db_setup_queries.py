setup_queries = [
    {
        "author": "-1",
        "description": "Creazione tabella 'Frequenza'",
        "query": '''
            CREATE TABLE Frequenza (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Vano'",
        "query": '''
            CREATE TABLE Vano (
                id INTEGER PRIMARY KEY,
                codice VARCHAR(255),
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Plesso'",
        "query": '''
            CREATE TABLE Plesso (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Sede'",
        "query": '''
            CREATE TABLE Sede (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Attrezzatura'",
        "query": '''
            CREATE TABLE Attrezzatura (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Prodotto'",
        "query": '''
            CREATE TABLE Prodotto (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },

    {
        "author": "-1",
        "description": "Creazione tabella 'Attività'",
        "query": '''
            CREATE TABLE Attività (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                frequenzaId INTEGER REFERENCES Frequenza(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'TipologiaEventi'",
        "query": '''
            CREATE TABLE TipologiaEventi (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Profilo'",
        "query": '''
            CREATE TABLE Profilo (
                id INTEGER PRIMARY KEY,
                descrizione VARCHAR(255),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Intervento'",
        "query": '''
            CREATE TABLE Intervento (
                id INTEGER PRIMARY KEY,
                ts TIMESTAMP,
                note VARCHAR(255),
                sedeId INTEGER REFERENCES Sede(id),
                plessoId INTEGER REFERENCES Plesso(id),
                attivitàId INTEGER REFERENCES Attività(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Utilizza'",
        "query": '''
            CREATE TABLE Utilizza (
                id INTEGER PRIMARY KEY,
                attrezzaturaId INTEGER REFERENCES Attrezzatura(id),
                interventoId INTEGER REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Consuma'",
        "query": '''
            CREATE TABLE Consuma (
                id INTEGER PRIMARY KEY,
                prodottoId INTEGER REFERENCES Attrezzatura(id),
                interventoId INTEGER REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Stanza'",
        "query": '''
            CREATE TABLE Stanza (
                id INTEGER PRIMARY KEY,
                vanoId INTEGER REFERENCES Attrezzatura(id),
                interventoId INTEGER REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Watchdog'",
        "query": '''
            CREATE TABLE Watchdog (
                id INTEGER PRIMARY KEY,
                ts TIMESTAMP,
                note VARCHAR(255),
                tipologiaEventiId INTEGER REFERENCES TipologiaEventi(id),
                utenteId INTEGER REFERENCES Utente(id)
            )
        '''
    },

    {
        "author": "-1",
        "description": "Creazione tabella 'Utente'",
        "query": '''
            CREATE TABLE Utente (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255),
                qualifica INTEGER REFERENCES Profilo(id),
                enabled BOOL
            )
        '''
    },
]
