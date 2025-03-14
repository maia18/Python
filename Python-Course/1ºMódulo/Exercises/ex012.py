"""
Faça uma lista de compras
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista_de_compras = []
while True:
    print('1 - Adicionar item a lista')
    print('2 - Remover item da lista')
    print('3 - Listar itens da lista')
    print('4 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        item = input("Digite o item que deseja adicionar a lista de compras: ")
        lista_de_compras.append(item)
    elif opcao == '2':
        item = input("Digite o item que deseja remover da lista de compras: ")
        try:
            lista_de_compras.remove(item)
        except ValueError:
            print('Item não encontrado na lista')
    elif opcao == '3':
        for i, item in enumerate(lista_de_compras):
            print(f'{i + 1} - {item}')
    elif opcao == '4':
        break
    else:
        print('Opção inválida')