""" Exercício com classes
    1 - Crie uma classe Carro (Nome)
    2 - Crie uma classe Motor (Nome)
    3 - Crie uma classe Fabricante (Nome)
    4 - Faça a ligação entre Carro tem um Motor
    Obs.: Um motor pode ser de vários carros
    
    5 - Faça a ligação entre Carro e um Fabricante
    Obs.: Um fabricante pode fabricar vários carros
    
    Exiba o nome do carro, motor e fabricante na tela
"""
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
        
class Motor:
    def __init__(self, nome):
        self.nome = nome

    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    

fusca = Carro('Fusca')
fiat_uno = Carro('Fiat Uno')
gol = Carro('Gol')

volkswagen = Fabricante('Volkswagen')
fiat = Fabricante('Fiat')

motor_1_0 = Motor('Motor 1.0')

fusca.fabricante = volkswagen
fiat_uno.fabricante = fiat
gol.fabricante = volkswagen

fusca.motor = motor_1_0
fiat_uno.motor = motor_1_0
gol.motor = motor_1_0

print(
    fusca.nome,
    fusca.fabricante.nome,
    fusca.motor.nome, sep='\n'
)

print()

print(
    fiat_uno.nome,
    fiat_uno.fabricante.nome,
    fiat_uno.motor.nome, sep='\n'
)

print()

print(
    gol.nome,
    gol.fabricante.nome,
    gol.motor.nome, sep='\n'
)