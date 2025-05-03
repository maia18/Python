""" DELETE no SQLite """
import sqlite3

from c1 import DB_FILE, TABLE_NAME

connection  = sqlite3.connect(DB_FILE)
cursor      = connection.cursor()

''' 
CRUD  - Create  Read  Update Delete
SQL   - INSERT SELECT UPDATE DELETE 
'''

# LOOK OUT: Deleting without where
'''
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()
'''

# DELETE safer
'''
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()
'''

if __name__ == '__main__':
    
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.close()
    connection.close()