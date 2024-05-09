"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:
    choose_ = input("Deseja [1]inserir, [2]apagar ou [3]listar valores?: ")
    if choose_ == '1':    
        os.system('cls')
        item_lista = input("Digite um item: ")        
        if item_lista not in lista_compras:
            lista_compras.append(item_lista)
            parada = input("Deseja parar? [1]sim, [2]não: ")
            if parada == '1':
                break
        else:
            print("Item já presente ma lista!")
    elif choose_ == '2':
        os.system('cls')
        item = input("Digite o índice que deseja apagar: ")
        if item.isdigit():
            if len(lista_compras) > 0:
                del lista_compras[int(item)]
            else:
                print("Lista vazia!")
        else:
            print("Digite um índice válido!")
        parada = input("Deseja parar? [1]sim, [2]não: ")
        if (parada.isdigit() == True) and (int(parada) == 1):
            break
    elif choose_ == '3':
        os.system('cls')
        if len(lista_compras) > 0:
            for index, item in enumerate(lista_compras):
                print(index, item)
        else:
            print("Lista vazia!")