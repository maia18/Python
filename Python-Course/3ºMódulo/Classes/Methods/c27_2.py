''' Exemplo de uso de dunder methods'''
from random import randint
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':  
    p1 = Ponto(randint(0, 10), randint(0, 10))
    p2 = Ponto(randint(0, 10), randint(0, 10))
    p3 = p1 + p2
    
    print(
        f'P1: {p1}', 
        f'P2: {p2}', 
        f'P3: {p3}', 
        sep='\n'
        )
    print('P1 é maior que p2:', p1 > p2)
    print('P2 é maior que p1:', p2 > p1)