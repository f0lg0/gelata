'''
NOTE

questo modulo è diverso dagli altri relativi al database perchè
quando si lavora con Flask sorge un problema:

gli oggetti conn e c DEVONO essere creati e utilizzati nello stesso thread
ciò significa che creare una classe qui e chiamare i suoi metodi tipo user_signup
dalle funzioni nei blueprints di Flask fallisce, in quanto quelle funzioni sono in threads diversi rispetto agli oggetti sqlite3

una soluzione sarebbe ignorare questi errori di threads passando una flag alla connessione sqlite ma ciò è un rischio a livello
di sicurezza: si potrebbe corrompere della memoria nel database SE NON SI GESTISTONO I LOCKS MANUALMENTE (queue etc)

la soluzione adottata è quella di istanziare e chiudere una nuova connessione ogni volta
così si sfruttano i metodi e le precauzioni di locking che adotta sqlite3 in maniera automatica
'''

import sqlite3
import time
from watchdog import Watchdog

DB_PATH = None
wd = None


def dbops_init(path):
    global DB_PATH
    global wd

    DB_PATH = path
    wd = Watchdog(DB_PATH)


def dbops_user_signup(user):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        query = c.execute(f'''
            SELECT EXISTS(SELECT 1 FROM Utente WHERE username = "{user['email']}")
        ''')

        exists = query.fetchall()[0][0]

        if exists != 0:
            return {
                "success": True,
                "signup": False,
                "message": "Utente già registrato"
            }

        # prima volta che incontriamo questo utente
        profilo_query = f'''
            INSERT INTO Profilo (descrizione, enabled)
            VALUES ("collaboratore", 1)
        '''
        c.execute(profilo_query)

        profilo_id = c.lastrowid

        utente_query = f'''
            INSERT INTO Utente (username, qualifica, enabled)
            VALUES ("{user['email']}", {profilo_id}, 1)
        '''
        c.execute(utente_query)

        user_id = c.lastrowid

        conn.commit()
    except Exception as e:
        print(f"Error while connecting to sqlite database: {e}")
        return {
            "success": False,
            "signup": False,
            "message": "Errore interno"
        }

    conn.close()

    wd.log(user_id, "Creazione profilo dell'utente", profilo_query)
    wd.log(user_id, "Inserimento dettagli utente in tabella Utente", utente_query)

    return {
        "success": True,
        "signup": True,
        "message": "Utente registrato con successo"
    }


def dbops_save_intervento(data, user_email):
    '''
    data {
        timestamp
        note
        enabled
        sede {
            descrizione
            enabled
        }
        plesso {
            descrizione
            enabled
        }
        vano { --> no FK ma tabella
            codice
            descrizione
            enabled
        }
        attività {
            descrizione
            enabled
            frequenza {
                descrizione
                enabled
            }
        }
        prodotto { --> no FK ma tabella
            descrizione
            enabled
        }
        attrezzatura { --> no FK ma tabella
            descrizione
            enabled
        }
    }
    '''

    if data == None:
        return {
            "success": False,
            "message": "L'intervento è nullo"
        }

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # TODO: sanitazation

        # sede
        c.execute(f'''
            INSERT INTO Sede (descrizione, enabled)
            VALUES ("{data['sede']['descrizione']}", 1)
        ''')

        sede_id = c.lastrowid

        # plesso
        c.execute(f'''
            INSERT INTO Plesso (descrizione, enabled)
            VALUES ("{data['plesso']['descrizione']}", 1)
        ''')

        plesso_id = c.lastrowid

        # frequenza
        c.execute(f'''
            INSERT INTO Frequenza (descrizione, enabled)
            VALUES ("{data['attività']['frequenza']['descrizione']}", 1)
        ''')

        # attività
        c.execute(f'''
            INSERT INTO Attività (descrizione, frequenzaId, enabled)
            VALUES ("{data['attività']['descrizione']}", {c.lastrowid}, 1)
        ''')

        attività_id = c.lastrowid

        # intervento
        intervento_mutation = f'''
            INSERT INTO Intervento (ts, note, sedeId, plessoId, attivitàId, enabled)
            VALUES ({time.time()}, "{data['note']}", {sede_id}, {plesso_id}, {attività_id}, 1)
        '''

        c.execute(intervento_mutation)

        intervento_id = c.lastrowid

        # vano
        c.execute(f'''
            INSERT INTO Vano (codice, descrizione, enabled)
            VALUES ("{data['vano']['codice']}", "{data['vano']['descrizione']}", 1)
        ''')

        vano_id = c.lastrowid

        # relazione tra vano e intervento
        c.execute(f'''
            INSERT INTO Stanza (vanoId, interventoId, enabled)
            VALUES ({vano_id}, {intervento_id}, 1)
        ''')

        # prodotto
        c.execute(f'''
            INSERT INTO Prodotto (descrizione, enabled)
            VALUES ("{data['prodotto']['descrizione']}", 1)
        ''')

        prodotto_id = c.lastrowid

        # relazione tra intervento e prodotto
        c.execute(f'''
            INSERT INTO Consuma (prodottoId, interventoId, enabled)
            VALUES ({prodotto_id}, {intervento_id}, 1)
        ''')

        # attrezzatura
        c.execute(f'''
            INSERT INTO Attrezzatura (descrizione, enabled)
            VALUES ("{data['attrezzatura']['descrizione']}", 1)
        ''')

        attrezzatura_id = c.lastrowid

        # relazione tra attrezzatura e intervento
        c.execute(f'''
            INSERT INTO Utilizza (attrezzaturaId, interventoId, enabled)
            VALUES ({attrezzatura_id}, {intervento_id}, 1)
        ''')

        conn.commit()
    except Exception as e:
        print(e)

        return {
            "success": False,
            "message": "Internal error."
        }

    # get user id from email for logging
    user = c.execute(f'''
        SELECT id FROM Utente WHERE username = "{user_email}"
    ''')

    user_id = user.fetchall()[0][0]

    conn.close()

    wd.log(user_id, "Inserimento intervento",
           intervento_mutation)

    return {
        "success": True,
        "message": "Intervento caricato con successo"
    }
