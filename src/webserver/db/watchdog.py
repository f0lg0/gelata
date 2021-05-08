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

        try:
            self.conn = sqlite3.connect(self.DB_PATH)
            self.c = self.conn.cursor()

            print("[*] Watchdog service started [*]")
        except Exception as e:
            print(f"Error while connecting to sqlite database: {e}")
            sys.exit(1)

    def log(self, author, description, query):
        log = LogEvent(author, description, query)
        print(log)


def watchdog_init():
    wd = Watchdog("../database/gelata.db")
    wd.log(-1, "testing", "SHOW TABLES")
