""" csv.writer e csv.DictWriter para escrever em CSV """
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'c17_b.csv'

lista_clientes = [
    {'Nome': 'Luiz Otavio', 'Endereco': 'Av 1, 22'},
    {'Nome': 'Joao Silva',  'Endereco': 'R. 2, "1"'},
    {'Nome': 'Maria Sol',   'Endereco': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Luiz Otavio', 'Av 1, 22'],
#     ['Joao Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereco']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)