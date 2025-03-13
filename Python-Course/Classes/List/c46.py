""" Desempacotamento em chamadas de métodos e funções """
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista # p = 'Maria', b = 'Helena', _ = [1, 2], ap = 3, u = 'Eduarda'
print(p, u, ap)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda') # Maria Helena 1 2 3 Eduarda
print(*lista)  # Maria Helena 1 2 3 Eduarda
print(*string) # A B C D
print(*tupla)  # Python é legal

print(*salas, sep=', ') # ['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda']