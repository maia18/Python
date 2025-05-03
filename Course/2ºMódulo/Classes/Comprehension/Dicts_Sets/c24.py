""" Dictionary Comprehension e Set Comprehension """

''' Exemplo 1 '''
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor # (chave, valor)
    in produto.items()
    if chave != 'categoria'
}
print(dc) # {'nome': 'CANETA AZUL', 'preco': 2.5}

''' Exemplo 2 '''
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

print(dc,           # {'a': 'valor a', 'b': 'valor a'}
      dict(lista),  # {'a': 'valor a', 'b': 'valor a'} 
      sep='\n') 

''' Exemplo 3 '''
s1 = {2 ** i for i in range(10)}
print(s1) # {32, 1, 2, 64, 4, 128, 256, 512, 8, 16}