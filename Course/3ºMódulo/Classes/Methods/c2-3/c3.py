""" Métodos em instâncias de classes Python """
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome='veiculo') -> None : 
        self.nome = nome

    def acelerar(self) -> None :
        print(f'{self.nome} está acelerando...\f')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()

automóvel = Carro()
print(automóvel.nome)
automóvel.acelerar()