import mariadb

conn = None
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="dev",
        password="dev",
        host="localhost",
        port=3306,
        database="gelata"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

if conn:
    cur = conn.cursor()
    print(cur)
