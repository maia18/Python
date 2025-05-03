""" Manipulando chaves e valores em dicionários """
pessoa = {}

chave_1 = 'nome'
pessoa[chave_1] = 'Luiz Otávio'.replace(' ', ', ')
print(pessoa[chave_1]) # Luiz, Otávio
 
pessoa['sobrenome'] = 'Miranda'
# del pessoa['sobrenome']

pessoa[chave_1] = 'Maria'
print(pessoa['nome'], pessoa[chave_1], sep=', ') # Maria, Maria

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])