""" Usando python-dotenv e .env com pymysql.connect """

'''
import pymysql
import dotenv
import os

dotenv.load_dotenv()

connection = pymysql.connect(
    host     = os.environ['MYSQL_HOST'],
    user     = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE'],
)

print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)
        
'''