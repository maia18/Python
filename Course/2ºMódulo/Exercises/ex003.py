""" Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro. """
from random import randint
# def duplica(num):
#     return num * 2 
# def triplica(num):
#     return num * 3
# def quadruplica(num):
#     return num * 4

def calculo(mult):
    def produto(num):
        return num * mult
    return produto
    # if mult == 2:
    #     return duplica
    # elif mult == 3:
    #     return triplica
    # elif mult == 4:
    #     return quadruplica

numeros = [randint(0, 100) for _ in range(10)]
print(numeros)

duplica = calculo(2); triplica = calculo(3); quadruplica = calculo(4)
for numero in numeros:
    print(duplica(numero),
          triplica(numero),
          quadruplica(numero), sep=' | ')

def count_pergunta_occurrences(perguntas):
    return sum(1 for pergunta in perguntas if 'Pergunta' in pergunta)

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5? ',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print("Quantidade de ocorrências de 'Pergunta':", count_pergunta_occurrences(perguntas))