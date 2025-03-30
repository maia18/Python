""" Herança simples - Relações entre classes """
# Associação ---> "Usa" 
# Agregação  ---> "Tem"
# Composição ---> "É dono de"
# Herança    ---> "É um"
#
# Herança vs Composição
#
# 📍Classe principal (Pessoa)
#    --> super class, base class, parent class
# 📍Classes filhas   (Cliente)
#    --> sub class, child class, derived class
# Method resolution order (MRO)
class Pessoa:
    # cpf = 'CPF PESSOA'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print("CLASSE PESSOA :)")
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
        
class Cliente(Pessoa):
    def falar_nome_classe(self):
        print("EITA, NEM SAI DA CLASSE CLIENTE ;-;")
        print(self.nome, self.sobrenome, self.__class__.__name__)
    
    
class Aluno(Pessoa):
    cpf = 'CPF ALUNO'
    ...
    
    
c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()

print(c1.cpf, a1.cpf, sep=', ')