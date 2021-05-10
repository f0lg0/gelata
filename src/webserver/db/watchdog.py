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

            # TODO: controlla se l'attività che stiamo loggando esiste già nella tabella, se si allora non inserire
            c.execute(f'''
                INSERT INTO TipologiaEventi (descrizione, enabled) 
                VALUES ("{log.description}", 1)
            ''')

            parsed_query = log.query.rstrip().replace('"', "'")
            c.execute(f'''
                INSERT INTO Watchdog (ts, note, tipologiaEventiId, utenteId)
                VALUES ({log.ts}, "{parsed_query}", {c.lastrowid}, {log.author})
            ''')

            conn.commit()

        except Exception as e:
            print("[!] Error while logging: ", e)
            return False

        return True
