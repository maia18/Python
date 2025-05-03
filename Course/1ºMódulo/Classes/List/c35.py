''' Exemplo 2 '''
#         0    1    2    3    4    5
lista = [100, 200, 300, 400]

lista[2] = 1000
del lista[2] 
print(lista)    # [100, 200, 400]
print(lista[2]) # 400
 
lista.pop()

lista.append(60) 
lista.insert(1, 5)

print(lista)    # [100, 5, 200, 60]

valor_retirado = lista.pop(2)
print(lista, 'Removido,', valor_retirado) # [100, 5, 60] Removido, 200