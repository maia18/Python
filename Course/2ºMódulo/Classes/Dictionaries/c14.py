""" Exemplos """
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

''' get '''
# print(p1.get('nome', 'Não existe'))

''' pop, popitem '''
# nome = p1.pop('nome')
# print(f"'{nome}' apagado",
#       f'Novo dicionário: {p1}', sep='\n')

# ultima_chave = p1.popitem()
# print(f"'{ultima_chave}' apagado",
#       f'Novo dicionário: {p1}', sep='\n')

''' update '''
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# }) # p1.update(nome='novo valor', idade=30)

# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]

# p1.update(tupla)
# p1.update(lista)
# print(p1)