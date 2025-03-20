# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
import os

caminho_arquivo = 'aula53.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula53_1_2.txt')
