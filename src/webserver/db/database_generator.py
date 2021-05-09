import sqlite3
import sys
import os

from db_setup_queries import setup_queries


class DatabaseGenerator:
    def __init__(self, db_path):
        self.DB_PATH = db_path

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

    def execute_query(self, payload: dict):
        '''
        payload {
            author: string
            description: string
            query: string
        }
        '''

        try:
            print(f"[+] execute_query: {payload['description']}")

            self.c.execute(payload["query"])
            self.conn.commit()
        except Exception as e:
            print(f"[!] execute_query: {e}")
            return False

        print("[+] Done!")
        return True

    def _create_tables(self):
        for q in setup_queries:
            success = self.execute_query(q)

            if not success:
                print("[!] Error while executing critical query [!]")
                sys.exit(1)

    def close_connection(self):
        self.conn.close()


def generate_database():
    print("*** Called DatabaseGenerator init ***")
    db_g = DatabaseGenerator("../database/gelata.db")
    db_g.close_connection()
