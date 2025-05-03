""" SELECT no SQLite """
import sqlite3

from c1 import DB_FILE, TABLE_NAME

connection  = sqlite3.connect(DB_FILE)
cursor      = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connection.close()