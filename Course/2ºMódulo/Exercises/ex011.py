"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
    
    resultado
    lista_soma  = [2, 4, 6, 8]
"""
from random import sample           # 'sample' Chooses k unique random elements from a population sequence.
from itertools import zip_longest

lista_a = sample(range(10), 7)
lista_b = sample(range(10), 4)
listas_zip = list(zip(lista_a, lista_b))                              # listas_zip: list[tuple[int, int]]
listas_zip_longest = list(zip_longest(lista_a, lista_b, fillvalue=0)) # listas_zip_longest: list[tuple[int, int]]

print(
    lista_a, lista_b,
    listas_zip, listas_zip_longest,
    sep='\n'
)

lista_soma_zip = [x + y for x, y in listas_zip]                 # lista_soma_zip: list[int]
lista_soma_zip_longest = [x + y for x, y in listas_zip_longest] # lista_soma_zip_longest: list[int]

print(
    '',
    lista_soma_zip,
    lista_soma_zip_longest, sep='\n'
)