""" Iterando strings com while """
#       01234
nome = 'Luiza'  # Iteráveis
#       54321
tamanho_nome = len(nome) # 5

novo_nome = ''

letra = 0
while letra < tamanho_nome:
    novo_nome += f'*{nome[letra]}'
    letra += 1
    
print(novo_nome)