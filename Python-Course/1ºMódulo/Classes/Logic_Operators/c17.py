""" Operadores 'in' e 'not in' """
# Strings são iteráveis
#  0  1  2  3  4  5
#  C  a  r  v  ã  o
# -6 -5 -4 -3 -2 -1

nome = 'celular caderno lápis estojo'
print(nome[2], nome[-4])  # l t
print('vio' in nome)      # False
print('zero' not in nome) # True

encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} foi encontrado!')
else:
    print(f'{encontrar} não foi encontrado!')