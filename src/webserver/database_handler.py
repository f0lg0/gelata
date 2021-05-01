import mariadb
import sys

conn = None
cur = None


class DatabaseHandler:
    def __init__(self):
        # Connect to MariaDB Platform
        try:
            self.__conn = mariadb.connect(
                user="dev",
                password="dev",
                host="localhost",
                port=3306,
                database="gelata"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self.__cur = self.__conn.cursor()

        tables = self.get_tables()
        print(tables)
        if "Utente" not in tables[0]:
            self.__create_user_table()

    def get_tables(self):
        self.__cur.execute("SHOW TABLES;")
        return self.__cur.fetchall()

    def __create_user_table(self):
        try:
            self.__cur.execute('''
                CREATE TABLE Utente (
                    id INT PRIMARY KEY,
                    username VARCHAR(255),
                    qualifica VARCHAR(255),
                    enabled BOOL
                )
            ''')

        except Exception as e:
            print(e)
            return False

        return True


db = DatabaseHandler()
