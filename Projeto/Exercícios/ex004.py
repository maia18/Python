"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input("Digit a number: ")
if num.isdigit():
    if int(num) % 2 == 0:
        print(f"{(num)} is par")
    elif int(num) % 2 != 0:
        print(f"{(num)} is impar")
else:
    print("Is not an integer number...")