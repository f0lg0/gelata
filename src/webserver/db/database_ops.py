'''
NOTE

WISH: refactoring in classe

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
from datetime import datetime
from watchdog import Watchdog

DB_PATH = None
wd = None


def get_user_id_from_mail(c, email):
    user = c.execute(f'''
        SELECT id FROM Utente WHERE username = ? 
    ''', (email, ))

    user_id = user.fetchall()[0][0]
    return user_id


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

        user_id = get_user_id_from_mail(c, user_email)

        # sede
        sede = c.execute(f'''
            SELECT id FROM Sede 
            WHERE descrizione = ? 
        ''', (data['sede']['descrizione'], ))
        sede = sede.fetchall()
        sede_id = None

        if not len(sede):
            c.execute(f'''
                INSERT INTO Sede (descrizione, enabled)
                VALUES (?, 1)
            ''', (data['sede']['descrizione'], ))

            sede_id = c.lastrowid
        else:
            sede_id = sede[0][0]

        # plesso
        plesso = c.execute(f'''
            SELECT id FROM Plesso 
            WHERE descrizione = ? 
        ''', (data['plesso']['descrizione'], ))
        plesso = plesso.fetchall()
        plesso_id = None

        if not len(plesso):
            c.execute(f'''
                INSERT INTO Plesso (descrizione, enabled)
                VALUES (?, 1)
            ''', (data['plesso']['descrizione'], ))

            plesso_id = c.lastrowid
        else:
            plesso_id = plesso[0][0]

        # frequenza
        c.execute(f'''
            INSERT INTO Frequenza (descrizione, enabled)
            VALUES (?, 1)
        ''', (data['attività']['frequenza']['descrizione'], ))

        # attività
        c.execute(f'''
            INSERT INTO Attività (descrizione, frequenzaId, enabled)
            VALUES (?, {c.lastrowid}, 1)
        ''', (data['attività']['descrizione'], ))

        attività_id = c.lastrowid

        # leaving this even tho we execute the query using tuples (sanitazation)
        intervento_mutation = f'''
            INSERT INTO Intervento (ts, note, sedeId, plessoId, attivitàId, utenteId, enabled)
            VALUES ({time.time()}, "{data['note']}", {sede_id}, {plesso_id}, {attività_id}, {user_id}, 1)
        '''

        c.execute(f'''
            INSERT INTO Intervento (ts, note, sedeId, plessoId, attivitàId, utenteId, enabled)
            VALUES ({time.time()}, ?, {sede_id}, {plesso_id}, {attività_id}, {user_id}, 1)
        ''', (data['note'], ))

        intervento_id = c.lastrowid

        # vano
        vano = c.execute(f'''
            SELECT id FROM Vano WHERE codice = ? 
        ''', (data['vano']['codice'], ))
        vano = vano.fetchall()
        vano_id = None

        if not len(vano):
            c.execute(f'''
                INSERT INTO Vano (codice, descrizione, enabled)
                VALUES (?, ?, 1)
            ''', (data['vano']['codice'], data['vano']['descrizione']))

            vano_id = c.lastrowid
        else:
            vano_id = vano[0][0]

        # relazione tra vano e intervento
        c.execute(f'''
            INSERT INTO Stanza (vanoId, interventoId, enabled)
            VALUES ({vano_id}, {intervento_id}, 1)
        ''')

        # prodotto
        c.execute(f'''
            INSERT INTO Prodotto (descrizione, enabled)
            VALUES (?, 1)
        ''', (data['prodotto']['descrizione'], ))

        prodotto_id = c.lastrowid

        # relazione tra intervento e prodotto
        c.execute(f'''
            INSERT INTO Consuma (prodottoId, interventoId, enabled)
            VALUES ({prodotto_id}, {intervento_id}, 1)
        ''')

        # attrezzatura
        c.execute(f'''
            INSERT INTO Attrezzatura (descrizione, enabled)
            VALUES (?, 1)
        ''', (data['attrezzatura']['descrizione'], ))

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

    conn.close()

    wd.log(user_id, "Inserimento intervento",
           intervento_mutation)

    return {
        "success": True,
        "message": "Intervento caricato con successo"
    }


def dbops_delete_intervento(intervento_id, user_email):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        user_id = get_user_id_from_mail(c, user_email)

        # leaving this even tho we execute the query using tuples
        query = f'''
            UPDATE Intervento
            SET enabled = 0
            WHERE id = (
                SELECT id FROM Intervento 
                WHERE id = {intervento_id} AND utenteId = {user_id}
            )
        '''

        c.execute(f'''
            UPDATE Intervento
            SET enabled = 0
            WHERE id = (
                SELECT id FROM Intervento 
                WHERE id = ? AND utenteId = {user_id}
            )
        ''', (intervento_id, ))

        conn.commit()
    except Exception as e:
        print(f"Error while connecting to sqlite database: {e}")

        return {
            "success": False,
            "delete": False,
            "message": "Errore interno"
        }

    conn.close()

    wd.log(user_id, "Eliminazione intervento", query)

    return {
        "success": True,
        "delete": True,
        "message": "Intervento eliminato con successo"
    }


def dbops_update_intervento(data, user_email):
    '''
    NOTE: 
    non sapevo come gestire questa operazione in maniera efficiente
    se fosse stato un db NoSQL avrei usato dei loops ma in questo caso non saprei
    di conseguenza vengono modificati TUTTI i fields ogni volta anche se  si cambia un solo campo
    '''
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        user_id = get_user_id_from_mail(c, user_email)

        # get intervento from id
        intervento_id = data["id"]
        intervento = c.execute(f'''
            SELECT * FROM Intervento 
            WHERE 
                id = ? 
            AND 
                utenteId = {user_id} 
            AND 
                enabled = 1;
        ''', (intervento_id, ))

        intervento = intervento.fetchall()

        # TODO: add more error checking and enabled checking
        if len(intervento):
            intervento = intervento[0]

            fks = {
                "sedeId": intervento[3],
                "plessoId": intervento[4],
                "attivitàId": intervento[5]
            }

            # sede
            c.execute(f'''
                UPDATE Sede
                SET descrizione = ? 
                WHERE id = ? 
            ''', (data['sede']['descrizione'], fks['sedeId']))

            # plesso
            c.execute(f'''
                UPDATE Plesso
                SET descrizione = ?
                WHERE id = ?
            ''', (data['plesso']['descrizione'], fks['plessoId']))

            # get frequenza id from attività

            attività = c.execute(f'''
                SELECT * FROM Attività 
                WHERE id = ?
            ''', (fks['attivitàId'], ))

            attività = attività.fetchall()[0]
            frequenza_id = attività[2]

            # frequenza
            c.execute(f'''
                UPDATE Frequenza
                SET descrizione = ? 
                WHERE id = {frequenza_id}
            ''', (data['attività']['frequenza']['descrizione'], ))

            # attività
            c.execute(f'''
                UPDATE Attività
                SET descrizione = ? 
                WHERE id = ?
            ''', (data['attività']['descrizione'], fks['attivitàId']))

            # intervento
            c.execute(f'''
                UPDATE Intervento
                SET note = ?
                WHERE id = ?
            ''', (data['note'], intervento_id))

            # get vano id from Stanza using intervento id
            vano_id = c.execute(f'''
                SELECT vanoId FROM Stanza 
                WHERE interventoId = ?
            ''', (intervento_id, ))

            vano_id = vano_id.fetchall()[0][0]

            # vano
            c.execute(f'''
                UPDATE Vano
                SET codice = ?,  
                descrizione = ?
                WHERE id = {vano_id}
            ''', (data['vano']['codice'], data['vano']['descrizione']))

            # get prodottoId from Consuma using interventoId
            prodotto_id = c.execute(f'''
                SELECT prodottoId FROM Consuma 
                WHERE interventoId = ?
            ''', (intervento_id, ))

            prodotto_id = prodotto_id.fetchall()[0][0]

            # prodotto
            c.execute(f'''
                UPDATE Prodotto
                SET descrizione = ?
                WHERE id = {prodotto_id}
            ''', (data['prodotto']['descrizione'], ))

            # get attrezzaturaId from Utilizza using interventoId
            attrezzatura_id = c.execute(f'''
                SELECT attrezzaturaId from Utilizza
                WHERE interventoId = ?
            ''', (intervento_id, ))

            attrezzatura_id = attrezzatura_id.fetchall()[0][0]

            # attrezzatura
            c.execute(f'''
                UPDATE Attrezzatura
                SET descrizione = ?
                WHERE id = {attrezzatura_id}
            ''', (data['attrezzatura']['descrizione'], ))

            conn.commit()

        else:
            return {
                "success": False,
                "message": "Impossibile trovare l'intervento"
            }
    except Exception as e:
        print(f"Error while connecting to sqlite database: {e}")
        return {
            "success": False,
            "message": "Errore interno"
        }

    conn.close()

    wd.log(user_id, "Modifica intervento",
           f"(NOTE: redacted) UPDATE Intervento WHERE id = {intervento_id}")

    return {
        "success": True,
        "message": "Modifica dell'intervento avvenuta con successo"
    }


def dbops_get_interventi_by_user(user_email, offset=0):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        user_id = get_user_id_from_mail(c, user_email)

        query = f'''
            SELECT
                Intervento.id, Intervento.ts, Intervento.note,
                Sede.descrizione, Plesso.descrizione, Attività.descrizione, Frequenza.descrizione, Utente.username,
                Vano.codice, Vano.descrizione, Prodotto.descrizione, Attrezzatura.descrizione
            FROM
                Intervento

            INNER JOIN Sede ON Intervento.sedeId = Sede.id
            INNER JOIN Plesso ON Intervento.plessoId = Plesso.id
            INNER JOIN Attività ON Intervento.attivitàId = Attività.id
            INNER JOIN Frequenza ON Attività.frequenzaId = Frequenza.id
            INNER JOIN Utente ON Intervento.utenteId = Utente.id
            INNER JOIN Stanza ON Stanza.interventoId = Intervento.id
            INNER JOIN Vano ON Vano.id = Stanza.vanoId
            INNER JOIN Consuma ON Consuma.interventoId = Intervento.id
            INNER JOIN Prodotto ON Prodotto.id = Consuma.prodottoId
            INNER JOIN Utilizza ON Utilizza.interventoId = Intervento.id
            INNER JOIN Attrezzatura ON Attrezzatura.id = Utilizza.attrezzaturaId 

            WHERE
                Intervento.utenteId = {user_id} AND Intervento.enabled = 1

        '''
        interventi = c.execute(query)

        interventi = interventi.fetchall()
        parsed = []

        for i in interventi:
            date_from_ts = str(datetime.fromtimestamp(i[1]))

            # removing seconds from date
            date_from_ts = date_from_ts[:len(date_from_ts) - 10]

            parsed.append({
                "id": i[0],
                "ts": date_from_ts,
                "note": i[2],
                "sede": i[3],
                "plesso": i[4],
                "attività": {
                    "descrizione": i[5],
                    "frequenza": i[6]
                },
                "utente": i[7],
                "vano": {
                    "codice": i[8],
                    "descrizione": i[9]
                },
                "prodotto": i[10],
                "attrezzatura": i[11]
            })
    except Exception as e:
        print(f"Error while connecting to sqlite database: {e}")

        return {
            "success": False,
            "get_interventi": False,
            "message": "Errore interno"
        }

    conn.close()

    wd.log(user_id, "Fetching interventi svolti dall' utente", query)

    return {
        "success": True,
        "get_interventi": True,
        "message": "Ottenuto lista di interventi con successo",
        "interventi": parsed
    }
