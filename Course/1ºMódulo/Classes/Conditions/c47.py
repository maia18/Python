""" Operação ternária (condicional de uma linha) <valor> if <condicao> else <outro valor> """

''' Exemplo 1 '''
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

''' Exemplo 2 '''
digito = 2  # > 9 = 0
novo_digito = digito if digito <= 9 else 0; 0 if digito > 9 else digito
print(novo_digito)