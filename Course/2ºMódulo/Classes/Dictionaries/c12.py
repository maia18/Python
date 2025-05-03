""" Exemplos """
# len - quantas chaves há
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
pessoa = {
    'nome': 'Otávio',
    'sobrenome': 'Melo',
    # 'idade': 900,
}

''' setdefault '''
pessoa.setdefault('idade', 30)

''' len, keys, values, items '''
print(
    pessoa['idade'],        # 30
    len(pessoa),            # 3
    list(pessoa.keys()),    # ['nome', 'sobrenome', 'idade']
    list(pessoa.values()),  # ['Otávio', 'Melo', 30]
    list(pessoa.items()),   # [('nome', 'Otávio'), ('sobrenome', 'Melo'), ('idade', 30)]
    sep='\n'
)
for chave in pessoa.keys():
    print(chave)         # nome, sobrenome, idade
for valor in pessoa.values():
    print(valor)         # Otávio, Melo, 30
for chave, valor in pessoa.items():
    print(chave, valor)  # nome Otávio, sobrenome Melo, idade 30