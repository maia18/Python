""" Argumentos nomeados e não nomeados em funções Python """
# Argumento nomeado tem nome com sinal de igual
# Argumento não nomeado recebe apenas o argumento (valor)
def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)     # x=1 y=2 z=3 | x + y + z =  6
soma(1, y=2, z=5) # x=1 y=2 z=5 | x + y + z =  8