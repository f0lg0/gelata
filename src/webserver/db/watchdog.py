from os import terminal_size
import sqlite3
import sys
import time

from dataclasses import dataclass


@dataclass
class LogEvent:
    author: int
    description: str
    query: str
    ts: float = time.time()


class Watchdog:
    def __init__(self, path):
        self.DB_PATH = path
        print("[*] Watchdog service initialized [*]")

    def log(self, author, description, query):
        try:
            conn = sqlite3.connect(self.DB_PATH)
            c = conn.cursor()

            log = LogEvent(author, description, query)

            te_query = c.execute(f'''
                SELECT id FROM TipologiaEventi WHERE descrizione = "{log.description}"
            ''')

            te_id = te_query.fetchall()
            print(te_id)
            if len(te_id) == 0:
                c.execute(f'''
                    INSERT INTO TipologiaEventi (descrizione, enabled) 
                    VALUES ("{log.description}", 1)
                ''')

            parsed_query = log.query.rstrip().replace('"', "'")
            c.execute(f'''
                INSERT INTO Watchdog (ts, note, tipologiaEventiId, utenteId)
                VALUES ({log.ts}, "{parsed_query}", {c.lastrowid if len(te_id) == 0 else te_id[0][0]}, {log.author})
            ''')

            conn.commit()

        except Exception as e:
            print("[!] Error while logging: ", e)
            return False

        return True
