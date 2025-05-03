""" 
Operadores de atribuição 
= += -= *= /= //= **= %=
"""
contador = 2    # Valor inicial

contador += 5   # contador = contador + 5
print(contador) # 7

contador -= 5   # contador = contador - 5
print(contador) # 2

contador *= 5   # contador = contador * 5
print(contador) # 10

contador **= 5  # contador = contador ** 5
print(contador) # 100000

contador /= 5   # contador = contador / 5
print(contador) # 20000.0

contador //= 5  # contador = contador // 5
print(contador) # 4000.0

contador %= 5   # contador = contador % 5
print(contador) # 0.0