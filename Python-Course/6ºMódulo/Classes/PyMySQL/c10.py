""" Inserindo valores usando dicionários ao invés de iteráveis """

'''
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
'''