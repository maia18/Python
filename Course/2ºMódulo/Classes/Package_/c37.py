from sys import path

''' Exemplo 1 '''
import c37_package.modulo
from c37_package import modulo
from c37_package.modulo import * # (Má prática!)

print(soma_do_modulo(1, 2))                     # 3
print(c37_package.modulo.soma_do_modulo(1, 2))  # 3
print(modulo.soma_do_modulo(1, 2))              # 3 
print(soma_do_modulo(1, 2))                     # 3
print(variavel, nova_variavel)                  # Alguma coisa OK

''' Exemplo 2 '''
from c37_package.modulo import soma_do_modulo, fala_oi

print(__name__)  # __main__
fala_oi()        # Oi!