""" Lista de listas e seus índices """
salas = [
      # 0        1
    ['Maria', 'Helena', ],  # 0
      # 0
    ['Elaine', ],  # 1
      # 0       1       2
    ['Luiz', 'João', 'Eduarda'],  # 2
            # 0
    [(3, 9, (15, 21, 25))] # 3
]
print(salas[1][0])       # Elaine
print(salas[0][1])       # Helena
print(salas[2][2])       # Eduarda
print(salas[3][0][1])    # 9
print(salas[3][0][2][0]) # 15
# print(salas[3][1]) -> list index out of range

for sala in salas:
    for aluno in sala:
        print(f'Sala: {sala} \n'    # ['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda'], [(3, 9, (15, 21, 25))]
              f'Aluno(a): {aluno}') #   Maria, Helena        Elaine       Luiz, João, Eduarda        (3, 9, (15, 21, 25))