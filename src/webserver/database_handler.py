import sqlite3
import sys
import os


class DatabaseHandler:
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

    def __create_user_table(self):
        try:
            print("[+] Creating user table...")

            self.c.execute('''
                CREATE TABLE Utente (
                    id INT PRIMARY KEY,
                    username VARCHAR(255),
                    qualifica VARCHAR(255),
                    enabled BOOL
                )
            ''')

            self.conn.commit()
            print("[+] Done!")
        except Exception as e:
            print(e)
            return False

        return True

    def _create_tables(self):
        self.__create_user_table()


db = DatabaseHandler()
