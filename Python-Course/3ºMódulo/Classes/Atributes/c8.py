""" __dict__ e vars para atributos de instância """
from datetime import datetime

class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA'
# p1.__dict__['nome'] = 'EITA'
# p1.__dict__['outra'] = 'coisa'
# del p1.__dict__['nome']

print(vars(p1))       # {'nome': 'João', 'idade': 35, 'outra': 'coisa'}
# print(p1.__dict__) ->  {'nome': 'João', 'idade': 35, 'outra': 'coisa'}
# print(p1.outra)    ->  coisa
print(p1.nome)        # João