"""
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. 
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. 
Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa
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
import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...
    
    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f"(DEPÓSITO {valor:.2f} R$)")
        return self.saldo
        
    def detalhes(self, msg: str = '') -> None:
        print(f"O saldo é {self.saldo:.2f} R$\n{msg}\n---")
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f} R$)")
            return self.saldo
        
        self.detalhes(
            f"(SAQUE NEGADO {valor:.2f} R$)"
        )
        return self.saldo
        
        
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float=0, limite: float=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        max_limite = -self.limite
        
        if valor_pos_saque >= max_limite:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f} R$)")
            return self.saldo
        
        self.detalhes(
            f"(SAQUE NEGADO {valor:.2f} R$)\nLimite: {max_limite:.2f} R$"
            )
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
      
        
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome:str):
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade:int):
        self._idade = idade
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None  = None


class Banco:
    def __init__(
        self, 
        agencias: list[int] | None = None, 
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None
        ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False 

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        
        print('_checa_conta', False)
        return False 
    
    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_conta_cliente', True)
            return True
        
        print('_checa_conta_cliente', False)
        return False 
    
    def autenticar(
        self, 
        cliente: Pessoa, 
        conta: Conta
        ):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
                self._checa_conta(conta) and \
                    self._checa_conta_cliente(cliente, conta)
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'\
            \nAGÊNCIAS: ({self.agencias!r},\
            \nCLIENTES: {self.clientes!r},\
            \nCONTAS:   {self.contas!r})'
        return f'{class_name}{attrs}'
    

if __name__ == '__main__':
    cc1 = ContaCorrente(444, 555, 0, 100)
    cp1 = ContaPoupanca(111, 222)

    c1 = Cliente('Luiz', 30)
    c2 = Cliente('Pedro', 50)
    
    c1.conta = cc1
    c2.conta = cp1
    
    banco = Banco()
    banco.agencias.extend([cc1.agencia, cp1.agencia])
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    
    print(f"{banco}\n")
    
    if banco.autenticar(c1, cc1):
        print(c1.conta)
        while True:
            comando = input('[1] SAQUE | [2] DEPÓSITO \n')
            if comando == '1':
                cc1.sacar(float(input('Valor para saque -> ')))
            elif comando == '2':        
                cc1.depositar(float(input('Valor para depósito -> ')))