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