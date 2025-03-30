''' __init__ e __post_init__ em dataclasses '''
from dataclasses import dataclass

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(p1)
    print(p1.nome_completo)