import sqlite3
from pathlib import Path

ROOT_DIR    = Path(__file__).parent
DB_NAME     = 'db.sqlite3'
DB_FILE     = ROOT_DIR / DB_NAME

TABLE_NAME  = 'customers'

connection  = sqlite3.connect(DB_FILE)
cursor      = connection.cursor()

# LOOK OUT: Deleting without where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# connection.commit()

# Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Register values in the colums table
# LOOK OUT: sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Fulano", 70.4), (NULL, "Helena", 60)'
)
connection.commit()

cursor.close()
connection.close()