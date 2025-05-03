import sqlite3

from c1 import DB_FILE, TABLE_NAME

connection  = sqlite3.connect(DB_FILE)
cursor      = connection.cursor()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))
connection.commit()

if __name__ == '__main__':
    print(sql)
    
    cursor.close()
    connection.close()