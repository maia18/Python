""" Introdução à List comprehension em Python """
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.
lista = [
    numero * 2
    for numero in range(10)
]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)           # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]