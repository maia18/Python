"""
Introdução ao empacotamento e desempacotamento
"""
# nome_1, nome_2, nome_3 = ['Maria', 'Helena', 'Luiz']
# nome_1, nome_2 = ['Maria', 'Helena', 'Luiz'] # too many values to unpack (expected 2)
# nome_1, nome_2, nome_3, nome_4 = ['Maria', 'Helena', 'Luiz'] # not enough values to unpack (expected 4, got 3)

# nome_1, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome_1) # ---> Maria
# print(nome_1, *resto) # ---> Maria Helena Luiz

# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(_) # Helena
# print(_) # Helena
# print(nome) # Luiz
# print(*resto) # 

#######################################################

"""
Tipo tupla - Uma lista imutável
enumerate - enumera iteráveis (índices)
"""
nomes = 'Maria', 'Helena', 'Luiz'
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1]) # ---> Luiz
print(nomes) # ---> ('Maria', 'Helena', 'Luiz')

#######################################################

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')