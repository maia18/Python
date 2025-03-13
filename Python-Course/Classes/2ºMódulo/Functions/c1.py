""" Introdução às funções (def) """
# Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
# Por padrão, funções Python retornam None.

''' Exemplo 1 '''

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')
    
saudacao('Helena') # Olá, Helena!
saudacao()         # Olá, Sem nome!

''' Exemplo 2 '''

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3) # 1 2 3

''' Exemplo 3 '''

def multiplo_de(numero, multiplo):
    print(f'{numero} é múltiplo de {multiplo}!' if  numero % multiplo == 0 else f'{numero} não é múltiplo de {multiplo} :(', sep='\n')

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(9, 2)