import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'número': 32},
        {'rua': 'R2', 'número': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None
}

# with open('aula53.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo)
    
    
# with open('aula53.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii = False,
#         indent = 2
#         )
    
    
# with open('aula53.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     print(pessoa, type(pessoa), pessoa['nome'], sep='\n')
