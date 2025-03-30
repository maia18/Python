""" Valores padrão e field em dataclasses """
from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', 
        repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    endereços: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(
        p1, 
        p1.nome,
        p1.sobrenome,
        p1.endereços, 
        sep='\n'
        )