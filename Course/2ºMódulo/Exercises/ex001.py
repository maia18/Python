""" Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o total para uma variável e mostre o seu valor. """
def multiplica(*args):
    total = 1
    for numero in args:
        if numero != 0:
            total *= numero
        else:
            return ValueError('O número deve ser não nulo!')
    return total

multiplicação = multiplica(10, 2, 3, 4, 5)
print(multiplicação)