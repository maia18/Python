""" Atributos de classe """
from datetime import datetime

class Pessoa:
    ano_atual = datetime.now().year # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 56)
p2 = Pessoa('Helena', 21)

print(Pessoa.ano_atual)

# Pessoa.ano_atual = 1
# print(Pessoa.ano_atual) # 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())