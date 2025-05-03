""" Filtro de dados em list comprehension (filter) """
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
    
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
]
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]

# lista = [n for n in range(10) if n < 5] --> [0, 1, 2, 3, 4]

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05) > 10
]
p(novos_produtos)