""" CREATE TABLE para criar tabela com PRIMARY KEY no PyMySQ """

'''
# type: ignore

import os
import dotenv
import pymysql

dotenv.load_dotenv()

connection = pymysql.connect(
    host     = os.environ['MYSQL_HOST'],
    user     = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE'],
)

with connection:
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
'''