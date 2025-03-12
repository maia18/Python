""" Listas """
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
    # append - Adiciona um item ao final
    # insert - Adiciona um item no índice escolhido
    # pop - Remove do final ou do índice escolhido
    # del - apaga um índice
    # clear - limpa a lista
    # extend - estende a lista
    # + - concatena listas
# Create, Read, Update, Delete = lista[i] (CRUD)

''' Exemplo 1 '''
#               0     1        2           3    4
#              -5    -4       -3          -2   -1
lista_itens = [123, True, 'Luiz Otávio',  1.2, []]
print(lista_itens) # [123, True, 'Luiz Otávio', 1.2, []]

lista_itens[4] = 'Maria'
print(lista_itens, lista_itens[2], type(lista_itens[2])) # [123, True, 'Luiz Otávio', 1.2, 'Maria'] Luiz Otávio <class 'str'>