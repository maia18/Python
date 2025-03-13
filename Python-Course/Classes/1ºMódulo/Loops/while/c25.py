""" while (enquanto) """
# Executa uma ação enquanto uma condição for verdadeira
# Loop infinito -> Código não tem fim

''' Exemplo 1 '''
condição = True

while condição:
    nome = input('Seu nome: ')
    print(nome)
    if nome == 'sair':
        break
    
''' Exemplo 2 '''
contador = 0

while contador <= 10:
    contador += 1

    if contador >= 5 and contador <= 7:
        print('Não mostrarei o', contador)
        continue
    if contador == 10:
        break
    print(contador)
print('Acabou')