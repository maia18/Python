# Manipulando dados

'''
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

# CURRENT_CURSOR = pymysql.cursors.SSDictCursor
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
)

# Começo a manipular dados a partir daqui

with connection:

""" CREATE TABLE para criar tabela com PRIMARY KEY no PyMySQ """

    with connection.cursor() as cursor:
        cursor.execute(  
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        print(cursor)

""" TRUNCATE e INSERT p/ limpar e criar valores na tabela com um ou mais cursores """

    # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
        
    connection.commit()
    
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25) '
        )
        cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25) '
        )
        result = cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25) '
        )
        print(result)
        
    connection.commit()

""" Inserindo um valor usando placeholder e um iterável """

# Evite SQL Injection ao usar placeholders para enviar valores para consulta SQL
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)  # type: ignore
        
        print(sql, data)
        print(result)
        
    connection.commit()

""" Inserindo valores usando dicionários ao invés de iteráveis """

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)  # type: ignore
        print(sql)
        print(data2)
        print(result)
        
    connection.commit()

""" Inserindo vários valores usando placeholder e uma tupla de dicionários  """

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Juh", "age": 42, },
            {"name": "Ana", "age": 72, },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        print(sql)
        print(data3)
        print(result)
        
    connection.commit()
    
""" Inserindo vários valores usando placeholder e uma tupla de tuplas  """

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Alexa", 16, ),
            ("Luiz", 18, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        print(sql)
        print(data4)
        print(result)
        
    connection.commit()

""" Lendo valores com SELECT e WHERE + Cuidados com SQL Injection """

    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )
        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
        
        data5 = cursor.fetchall()  # type: ignore

        for row in data5:
            print(row)
            
""" Apagando com DELETE, WHERE e placeholders no PyMySQL"""

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        print(cursor.execute(sql, (1,)))  # type: ignore
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore

        for row in cursor.fetchall():  # type: ignore
            print(row)
            
""" Editando com UPDATE, WHERE e placeholders no PyMySQL """

    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Eleonor', 102, 4))
        
        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()
        
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()
        
        for row in data6:
            print(row)

        print('len(data6): '      ,   len(data6))
        print('resultFromSelect: ',   resultFromSelect)
        print('lastrowid na mão: ',   lastIdFromSelect)
        print('rowcount: '        ,   cursor.rowcount)
        print('lastrowid: '       ,   cursor.lastrowid)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)
        
        print()
        print('For 1: ')
        
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 5:
                break

        print()
        print('For 2: ')
        
        # cursor.scroll(-2)   # Go back two lines
        # cursor.scroll(1)    # Advance one line
        # cursor.scroll(100)  # Index out of range
        
        for row in cursor.fetchall_unbuffered():
            print(row)
            
    connection.commit()
'''