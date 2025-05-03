"""
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias da classe com os dados salvos
Faça em arquivos separados. 
"""
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
CAMINHO_ARQUIVO = 'ex001.json'

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 10)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)