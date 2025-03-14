""" split e join com list e str """
# split - divide a string em uma lista
# join - une uma string
frase = '   Olha só que     , coisa interessante            '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas) # ['   Olha só que     ', ' coisa interessante            ']
print(lista_frases)       # ['Olha só que', 'coisa interessante']

frase_unidas = '-'.join(lista_frases)
print(frase_unidas) # Olha só que-coisa interessante
