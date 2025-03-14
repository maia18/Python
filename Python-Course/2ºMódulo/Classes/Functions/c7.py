"""
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes:

● Higher Order Functions: Funções que podem receber e/ou retornar outras funções
● First-Class Functions:  Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""
def saudação(msg, nome):
    return f'{msg}, {nome}!'

def executa(função, *args):
    return função(*args)

print(
    executa(saudação, 'Bom dia', 'Luiz'),
    executa(saudação, 'Bom tarde', 'Fernanda'),
    executa(saudação, 'Boa noite', 'Maria'),
    sep='\n'
)