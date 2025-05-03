""" os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes) """

import math
import os
from itertools import count

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """ Formata um tamanho, de bytes para o tamanho apropriado """

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos:     0    1     2     3     4     5
    abreviação_tamanhos     =   "B", "KB", "MB", "GB", "TB", "PB"

    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes com a base (1000 por padrão).
    
    # Isso deve bater com o nosso índice na abreviação dos tamanhos
    indice_abreviação_tamanhos = int(math.log(tamanho_em_bytes, base))
    
    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto.
    potência = base ** indice_abreviação_tamanhos
    
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potência
    
    # A abreviação que queremos
    abreviação_tamanho = abreviação_tamanhos[indice_abreviação_tamanhos]
    
    return f'{tamanho_final:.2f} {abreviação_tamanho}'


caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
counter = count()


for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)