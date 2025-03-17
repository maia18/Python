""" Empacotamento e desempacotamento de dicionários """
''' args e kwargs:
        - args: (já vimos)
        - kwargs: keyword arguments (argumentos nomeados)
'''
a, b = 1, 2
a, b = b, a
# print(f'{a=}, {b=}') --> a = 2, b = 1

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2) --> nome Aline
# print(b1, b2) --> sobrenome Souza

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa) --> {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
        
mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)