"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

for in com listas
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
print(lista)
print(lista[3], type(lista[3]))
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

#############################################

#        0   1   2   3      4       5
lista = [10, 20, 30, 40, 'marcos', 4.3]
lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(5)
print(lista, 'Removido,', ultimo_valor)

#############################################

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
# lista_d = lista_a.extend(lista_b)
# print(lista_d) ----> None
lista_a.extend(lista_b)
print(lista_a) # -----> [1, 2, 3, 4, 5, 6]

#############################################

lista_a_ = ['Luiz', 'Maria', 1, True, 1.2]
lista_b_ = lista_a_.copy() # ---> ['Luiz', 'Maria', 1, True, 1.2]
lista_a_[0] = 'Qualquer coisa'
# lista_b_ = lista_a_.copy() ----> ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_a_) 
print(lista_b_)

#############################################

lista_for = ['Maria', 'Helena', 'Luiz']

for nome in lista_for:
    print(nome, type(nome)) # --> Maria <class 'str'>
                            # --> Helena <class 'str'>
                            # --> Luiz <class 'str'>

"""
Exercício Solucionado
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ["Maria", "Helena", "Jorge"]
lista.append("Gilberto")
print(lista)
for nome in lista:
    print(lista.index(nome), nome) # ---> 0 Maria
                                   # ---> 1 Helena
                                   # ---> 2 Jorge
                                   # ---> 3 Gilberto