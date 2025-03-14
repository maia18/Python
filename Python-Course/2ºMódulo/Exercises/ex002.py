""" Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar. """
def par_impar(valor=0):
    if valor % 2 == 0:
        return f'{valor} é par'
    return f'{valor} é ímpar'

teste1 = par_impar(2) ; teste2 = par_impar(11) ; teste3 = par_impar(-39) ; teste4 = par_impar()

print(teste1,               # 2 é par
      teste2,               # 11 é ímpar
      teste3,               # -39 é ímpar
      teste4, sep='\n')     # 0 é par