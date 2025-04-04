""" PyPDF2 para manipular arquivos PDF """
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro, gratuita e de código aberto. 
# Ela é capaz de ler, manipular, escrever e unir dados de arquivos PDF, assim como adicionar anotações, transformar páginas, extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTAS_ORIGINAIS = PASTA_RAIZ / 'pdfs'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTAS_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

'''
print(len(reader.pages))

for page in reader.pages:
    print(page)
    print()

print(page_0.extract_text())
print(page_0.images)
print(len(page_0.images))
'''

page_0  = reader.pages[0]
image_0 = page_0.images[0]
with open(PASTA_NOVA / image_0.name, 'wb') as fp:
    fp.write(image_0.data)
    
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquive:
        writer.add_page(page)
        writer.write(arquive)
        
files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]
merger = PdfMerger()
for file in files:
    merger.append(file)
    
merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()