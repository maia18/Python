""" Problema dos parâmetros mutáveis em funções Python """
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
cliente2.append('Edu')

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)
adiciona_clientes('Fernando', cliente3)
adiciona_clientes('Joyce', cliente3)

print('c1: ', cliente1)
print('c2: ', cliente2)
print('c3: ', cliente3)
