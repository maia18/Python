""" Exemplo """
def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = cria_multiplicador(2)

duplica = executa(
    lambda multiplicador: lambda numero: numero * multiplicador,
    9
)
print(
    duplica(5),
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7, 8, 9
    ), 
    sep='\n'
)