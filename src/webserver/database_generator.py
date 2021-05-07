import sqlite3
import sys
import os


'''
NOTE (TODO?)

potevamo creare una funzione wrapper che esegue una query passata
come parametro anziché creare una funzione per tabella

tale funzione sarà sicuramente implementata nel modulo 'database_ops' (gestisce le operazioni CRUD del db)

la soluzione corrente ha alcuni vantaggi:
    - leggibilità del codice
    - è facile modificare singolarmente le tabelle
    - le funzioni si possono estendere con eventuali aggiunte
    - le query sono formattate su più linee

ma ha anche svantaggi:
    - codice praticamente identico ripetuto molte volte
    - non è molto comodo controllare il return type di ogni funzione manualmente
'''


class DatabaseGenerator:
    def __init__(self):
        self.DB_PATH = "../database/gelata.db"

        if os.path.isfile(self.DB_PATH):
            self.CREATED = True
        else:
            self.CREATED = False

        try:
            self.conn = sqlite3.connect(self.DB_PATH)
            self.c = self.conn.cursor()
        except Exception as e:
            print(f"Error while connecting to sqlite database: {e}")
            sys.exit(1)

        if not self.CREATED:
            print("[!] Initializing database...")
            self._create_tables()
            print("[!] Database created.")

    def __create_utente_table(self):
        try:
            print("[+] Creating Utente table...")

            self.c.execute('''
                CREATE TABLE Utente (
                    id INT PRIMARY KEY,
                    username VARCHAR(255),
                    qualifica VARCHAR(255),
                    profiloId INT REFERENCES Intervento(id),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_intervento_table(self):
        try:
            print("[+] Creating Intervento table...")

            # le relazioni con Vano, Prodotto e Attrezzatura verranno implementata con tabelle

            self.c.execute('''
                CREATE TABLE Intervento (
                    id INT PRIMARY KEY,
                    ts TIMESTAMP,
                    note VARCHAR(255),
                    sedeId REFERENCES Sede(id),
                    plessoId REFERENCES Plesso(id),
                    attivitàId REFERENCES Attività(id),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_profilo_table(self):
        try:
            print("[+] Creating Profilo table...")

            self.c.execute('''
                CREATE TABLE Profilo (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_sede_table(self):
        try:
            print("[+] Creating Sede table...")

            self.c.execute('''
                CREATE TABLE Sede (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_plesso_table(self):
        try:
            print("[+] Creating Plesso table...")

            self.c.execute('''
                CREATE TABLE Plesso (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_vano_table(self):
        try:
            print("[+] Creating Vano table...")

            self.c.execute('''
                CREATE TABLE Vano (
                    id INT PRIMARY KEY,
                    codice VARCHAR(255),
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_attività_table(self):
        try:
            print("[+] Creating Attività table...")

            self.c.execute('''
                CREATE TABLE Attività (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    frequenzaId REFERENCES Frequenza(id),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_frequenza_table(self):
        try:
            print("[+] Creating Frequenza table...")

            self.c.execute('''
                CREATE TABLE Frequenza (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_prodotto_table(self):
        try:
            print("[+] Creating Prodotto table...")

            self.c.execute('''
                CREATE TABLE Prodotto (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_attrezzatura_table(self):
        try:
            print("[+] Creating Attrezzatura table...")

            self.c.execute('''
                CREATE TABLE Attrezzatura (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_watchdog_table(self):
        try:
            print("[+] Creating Watchdog table...")

            self.c.execute('''
                CREATE TABLE Watchdog (
                    id INT PRIMARY KEY,
                    ts TIMESTAMP,
                    note VARCHAR(255),
                    tipologiaEventiId REFERENCES TipologiaEventi(id),
                    utenteId REFERENCES Utente(id)
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_tipologiaeventi_table(self):
        try:
            print("[+] Creating TipologiaEventi table...")

            self.c.execute('''
                CREATE TABLE TipologiaEventi (
                    id INT PRIMARY KEY,
                    descrizione VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    # relazioni n..n
    def __create_stanza_table(self):
        try:
            print("[+] Creating Stanza table...")

            # added 'enabled' field
            self.c.execute('''
                CREATE TABLE Stanza (
                    id INT PRIMARY KEY,
                    vanoId REFERENCES Vano(id),
                    interventoId REFERENCES Intervento(id),
                    enabled BOOL,
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_consuma_table(self):
        try:
            print("[+] Creating Consuma table...")

            # added 'enabled' field
            self.c.execute('''
                CREATE TABLE Consuma (
                    id INT PRIMARY KEY,
                    prodottoId REFERENCES Prodotto(id),
                    interventoId REFERENCES Intervento(id),
                    enabled BOOL,
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def __create_utilizza_table(self):
        try:
            print("[+] Creating Utilizza table...")

            # added 'enabled' field
            self.c.execute('''
                CREATE TABLE Utilizza (
                    id INT PRIMARY KEY,
                    attrezzaturaId REFERENCES Attrezzatura(id),
                    interventoId REFERENCES Intervento(id),
                    enabled BOOL,
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def _create_tables(self):
        # TODO: check return flag

        self.__create_frequenza_table()
        self.__create_sede_table()
        self.__create_plesso_table()
        self.__create_vano_table()
        self.__create_attività_table()
        self.__create_prodotto_table()
        self.__create_attrezzatura_table()
        self.__create_tipologiaeventi_table()
        self.__create_profilo_table()
        self.__create_intervento_table()
        self.__create_watchdog_table()
        self.__create_utente_table()

    def close_connection(self):
        self.conn.close()


def generate_database():
    print("*** Called DatabaseGenerator init ***")
    db_g = DatabaseGenerator()
    db_g.close_connection()
