"""
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')
if num.isdigit():
    num_int = int(num)
    if num_int % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é ímpar')
else:
    print('Isso não é um número inteiro')