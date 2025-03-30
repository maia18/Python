""" Classes decoradoras (Decorator classes) """
from random import choice
numeros = list(range(1, 10))

class Multiplicar:
    def __init__(self, multiplicador=1):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(choice(numeros))
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
três_mais_cinco  = soma(3, 5)
print(dois_mais_quatro)
print(três_mais_cinco)