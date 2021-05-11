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


def dbops_save_intervento(data):
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

    return {
        "success": True,
        "message": "Intervento caricato con successo"
    }
