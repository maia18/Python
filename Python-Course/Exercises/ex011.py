""" Exiba os índices da lista """
lista = ['Maria', 'Helena', 'Luiz']

indices = range(len(lista))
print(indices) # range(0, 3)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))