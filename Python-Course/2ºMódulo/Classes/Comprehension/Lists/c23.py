""" List comprehension com mais de um for """
lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
lista_1 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista_2 = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista_1,
      lista_2, sep='\n')