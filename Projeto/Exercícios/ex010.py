"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = []
while True:
    choose_ = input("Deseja [1]inserir, [2]apagar ou [3]listar valores?: ")
    if choose_.isdigit() == True:
        if int(choose_) != 3:
            item_lista = input("Digite um item: ")
            if int(choose_) == 1:            
                if item_lista not in lista_compras:
                    lista_compras.append(item_lista)
                    parada = input("Parar? [1]sim, [2]não: ")
                    if (parada.isdigit() == True) and (int(parada) == 1):
                        break
            elif int(choose_) == 2:
                if (lista_compras.__contains__(item_lista) == True):
                    lista_compras.pop(lista_compras.index(item_lista))
                    parada = input("Parar? [1]sim, [2]não: ")
                    if (parada.isdigit() == True) and (int(parada) == 1):
                        break
        elif int(choose_) == 3:
            for index, item in enumerate(lista_compras):
                print(index, item)

        parada = input("Parar? [1]sim, [2]não: ")
        if (parada.isdigit() == True) and (int(parada) == 1):
            break