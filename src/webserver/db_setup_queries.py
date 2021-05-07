setup_queries = [
    {
        "author": "-1",
        "description": "Creazione tabella 'Frequenza'",
        "query": '''
            CREATE TABLE Frequenza (
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
                descrizione VARCHAR(255),
                frequenzaId INT REFERENCES Frequenza(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'TipologiaEventi'",
        "query": '''
            CREATE TABLE TipologiaEventi (
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
                ts TIMESTAMP,
                note VARCHAR(255),
                sedeId INT REFERENCES Sede(id),
                plessoId INT REFERENCES Plesso(id),
                attivitàId INT REFERENCES Attività(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Utilizza'",
        "query": '''
            CREATE TABLE Utilizza (
                id INT PRIMARY KEY,
                attrezzaturaId INT REFERENCES Attrezzatura(id),
                interventoId INT REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Consuma'",
        "query": '''
            CREATE TABLE Consuma (
                id INT PRIMARY KEY,
                prodottoId INT REFERENCES Attrezzatura(id),
                interventoId INT REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Stanza'",
        "query": '''
            CREATE TABLE Stanza (
                id INT PRIMARY KEY,
                vanoId INT REFERENCES Attrezzatura(id),
                interventoId INT REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
    {
        "author": "-1",
        "description": "Creazione tabella 'Watchdog'",
        "query": '''
            CREATE TABLE Watchdog (
                id INT PRIMARY KEY,
                ts TIMESTAMP,
                note VARCHAR(255),
                tipologiaEventiId INT REFERENCES TipologiaEventi(id),
                utenteId INT REFERENCES Utente(id)
            )
        '''
    },

    {
        "author": "-1",
        "description": "Creazione tabella 'Utente'",
        "query": '''
            CREATE TABLE Utente (
                id INT PRIMARY KEY,
                username VARCHAR(255),
                qualifica VARCHAR(255),
                profiloId INT REFERENCES Intervento(id),
                enabled BOOL
            )
        '''
    },
]
