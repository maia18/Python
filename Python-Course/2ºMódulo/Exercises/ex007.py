""" Ordene os produtos por nome decrescente
    Gere produtos_ordenados_por_nome por deep copy (cópia profunda) """
import copy
import pprint
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'], reverse=True
)
pprint.pprint(produtos)
print()
pprint.pprint(produtos_ordenados_por_nome)