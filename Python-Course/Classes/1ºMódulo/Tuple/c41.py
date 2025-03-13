""" enumerate """
# Enumera iteráveis (índices)
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(f'{indice}',          #   0       1     2     3
          f'{nome}',            # Maria, Helena, Luiz, João
          f'{lista[indice]}')   # Maria, Helena, Luiz, João
    
for i in range(len(lista)):
    print(f'\n{i}º Tupla:\n')    
    
    for item in enumerate(lista):   # item é uma tupla
        indice, nome = item
        print(indice, nome)         # 0 Maria, 1 Helena, 2 Luiz, 3 João