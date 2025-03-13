"""
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10    9    8    7    6    5    4    3   2
*   7    4    6    8    2    4    8    9   0
   70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301 

Multiplique o resultado por 10 ---> 301 * 10 = 3010
Obtenha o resto da divisão da conta anterior por 11 ---> 3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF MAIS O PRIMEIRO DIGITO multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.:  746.824.890-70 (746824890)
   11   10    9    8    7    6    5    4   3    2
*   7    4    6    8    2    4    8    9   0   *7* <-- PRIMEIRO DIGITO
   77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363 

Multiplique o resultado anterior por 10 ---> 363 * 10 = 3630
Obtenha o resto da divisão da conta anterior por 11 ---> 3630 % 11 = 0

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import random

algarismos_primeiro_digito = algarismos_segundo_digito = ''
soma_primeiro_digito = soma_segundo_digito = 0

quantd_cpfs = 3
while True:
    for _ in range(quantd_cpfs):
        digitos = ''
        for i in range(11):
            digitos += str(random.randint(0, 9))
        for indice, digito in enumerate(digitos[:9]):            
            algarismos_primeiro_digito += str(digito)
            soma_primeiro_digito += int(digito) * (10 - indice)        
            resultado = (soma_primeiro_digito * 10) % 11
            primeiro_digito = 0 if resultado > 9 else resultado
            
            novo_digito = algarismos_primeiro_digito + str(primeiro_digito)
            
        for indice, digito in enumerate(novo_digito):
            algarismos_segundo_digito += str(digito)
            soma_segundo_digito += int(digito) * (11 - indice)
            resultado = (soma_segundo_digito * 10) % 11
            segundo_digito = 0 if resultado > 9 else resultado
            
        print(f"O primeiro dígito do CPF é: {primeiro_digito}\n"
              f"O segundo dígito do CPF é: {segundo_digito}")
    break