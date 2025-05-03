""" Enum -> Enumerações """
# Enumerações na programação são usadas em ocasiões onde temos um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos;
#   - podem ser iterados para retornar seus membros canônicos na ordem de definição.
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.
# Para obter os dados:
#   • membro = Classe(valor), Classe['chave']
#   • chave = Classe.chave.name
#   • valor = Classe.chave.value
import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direções(enum.Enum):
    ESQUERDA =  enum.auto()
    DIREITA  =  enum.auto()
    ACIMA    =  enum.auto()
    ABAIXO   =  enum.auto()


print(Direções(1), 
      Direções['ESQUERDA'], 
      Direções.ESQUERDA, 
      Direções(1).name, 
      f'({Direções.ESQUERDA.value})',
      sep='\n')

print(Direções(4), 
      Direções['ABAIXO'], 
      Direções.ABAIXO, 
      Direções(4).name,
      f'({Direções.ABAIXO.value})',
      sep='\n')


def mover(direcao: Direções):
    if not isinstance(direcao, Direções):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direções.ESQUERDA)
mover(Direções.DIREITA)
mover(Direções.ACIMA)
mover(Direções.ABAIXO)