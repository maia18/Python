""" Aumente os preços dos produtos a seguir em 10%
    Gere novos_produtos por deep copy (cópia profunda) """
import copy
import pprint
produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]
novos_produtos = [
    {**produto, 'preço': round(produto['preço'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]
pprint.pprint(produtos)
print()
pprint.pprint(novos_produtos)