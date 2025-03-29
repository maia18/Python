"""
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. 
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. 
Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agência=None, num_conta=None, saldo=0):
        self.agência = agência
        self.num_conta = num_conta
        self.saldo = saldo
        
    @property
    def mudar_agência(self):
        return self._agência
    
    @mudar_agência.setter
    def mudar_agência(self, novo_saldo):
        self.saldo = novo_saldo
        
    @property
    def mudar_num_conta(self):
        return self._num_conta
    
    @mudar_num_conta.setter
    def mudar_num_contao(self, novo_num_conta):
        self.num_conta = novo_num_conta
        
    @property
    def mudar_saldo(self):
        return self._saldo
    
    @mudar_saldo.setter
    def mudar_saldo(self, novo_saldo):
        self.saldo = novo_saldo
    
    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def deposito(self, valor):
        self.saldo += valor
        return self.saldo
    
    
class ContaPoupanca(Conta):
    def __init__(self, agência=None, num_conta=None, saldo=0):
        super().__init__(agência, num_conta, saldo)
    
    def deposito(self, valor):
        self.saldo += valor
        return self.saldo 
    
    def sacar(self, valor):
        if 0 <= valor <= self.saldo:
          self.saldo -= valor
          return self.saldo
        else:
            print('Inválido') 


class ContaCorrente(Conta):
    def __init__(self, limite_extra=1000, agência=None, num_conta=None, saldo=0):
        super().__init__(agência, num_conta, saldo)
        self.saldo = limite_extra + saldo

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo 
    
    def sacar(self, valor):
        if 0 <= valor <= self.saldo:
          self.saldo -= valor
          return self.saldo
        else:
            print('Inválido') 


class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @property
    def mudar_nome(self):
        return self._nome
    
    @mudar_nome.setter
    def mudar_nome(self, novo_nome):
        self.nome = novo_nome
        
    @property
    def mudar_idade(self):
        return self._idade
    
    @mudar_idade.setter
    def mudar_idade(self, novo_idade):
        self.idade = novo_idade


class Cliente(Pessoa):
    def __init__(self, conta, nome, idade):
        super().__init__(nome, idade)
        self.conta = conta
        
    @property
    def mudar_conta(self):
        return self._conta
    
    @mudar_conta.setter
    def mudar_conta(self, nova_conta):
        self.conta = nova_conta


class Banco(Cliente, Conta): ...



if __name__ == "__main__":
    ...
    cc = ContaCorrente()
    # cp = ContaPoupanca()
    
    p1 = Cliente(cc, 'kaue', 12)
    print(p1.nome)
    print(p1.idade)
    print(p1.conta)
    
    print(p1.conta.agência)
    print(p1.conta.num_conta)
    print(p1.conta.saldo)
    
    p1.conta.deposito(200)
    print(p1.conta.saldo)
        
    p1.conta.sacar(1300)
    print(p1.conta.saldo)
    
    
    # print(p1.idade)
    # p1.idade = 30
    # p1.nome = 'Cleiton'
    # print(p1.nome)
    # print(p1.idade)
    
    # p2 = Cliente(cp)