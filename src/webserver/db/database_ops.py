import sqlite3

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
così si sfruttano i metodi e le precauzioni che adotta sqlite3 in maniera automatica
'''

DB_PATH = "../database/gelata.db"


def dbops_user_signup(user):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        query = c.execute(f'''
            SELECT EXISTS(SELECT 1 FROM Utente WHERE username = "{user['email']}")
        ''')

        exists = query.fetchall()[0][0]

        if exists != 0:
            return None

        # prima volta che incontriamo questo utente
        c.execute(f'''
            INSERT INTO Utente (username, qualifica, enabled)
            VALUES ("{user['email']}", "???", 1)
        ''')

        c.execute(f'''
            INSERT INTO Profilo (utenteId, descrizione, enabled)
            VALUES ({c.lastrowid}, "???", 1)
        ''')

        conn.commit()
    except Exception as e:
        print(f"Error while connecting to sqlite database: {e}")
        return False

    conn.close()
    return True
