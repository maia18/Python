""" reduce """
# Faz a redução de um iterável em um valor.
# Recebe dois argumentos principais:
#   - Uma função que recebe dois argumentos e retorna um único valor;
#   - Um iterável cujos itens serão processados pela função.
# reduce(function, iterable[, initializer]) -> value

''' Exemplo '''
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'], # (function)
    produtos, 0                    # (iterable[, initializer])
)


print('Total (via reduce): ', total)
print('Total (via sum): ', sum([p['preco'] for p in produtos]))