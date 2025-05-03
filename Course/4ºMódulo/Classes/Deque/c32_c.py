''' FIFO (First In First Out) '''
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final:  O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante
from c32_a import deque

# ✅ Legal (FIFO com deque)
fila_correta: deque[int] = deque() # Cria uma fila vazia

fila_correta.append(3)      # Adiciona no final
fila_correta.append(4)      # Adiciona no final
fila_correta.append(5)      # Adiciona no final
fila_correta.appendleft(2)  # Adiciona no começo
fila_correta.appendleft(1)  # Adiciona no começo
fila_correta.appendleft(0)  # Adiciona no começo

print(fila_correta)         # deque([0, 1, 2, 3, 4, 5])

fila_correta.pop()          # 5
fila_correta.popleft()      # 0

print(fila_correta)         # deque([1, 2, 3, 4])
print()


# 🚫 Ruim (FIFO com lista) 
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 10)
#   0  1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 11)
#  0   1   2  3  4  5  6  7  8  9, 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista.pop(0)  # 11
#  0   1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro: ', primeiro_removido)  # 11
print('Lista:', lista)                  # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()