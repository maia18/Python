""" UPDATE no SQLite """
import sqlite3

from c1 import DB_FILE, TABLE_NAME

connection  = sqlite3.connect(DB_FILE)
cursor      = connection.cursor()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="QUALQUER", weight=67.89 '
    'WHERE id = 2'
)
connection.commit()

cursor.close()
connection.close()