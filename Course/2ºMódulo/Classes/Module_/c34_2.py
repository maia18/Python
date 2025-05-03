''' alias 1 - 'import nome_modulo as apelido' '''
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys, '\n')


''' alias 2 - 'from nome_modulo import objeto as apelido' '''
from sys import exit as ex
from sys import platform as pf

print(pf, '\n')

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem


''' má prática - 'from nome_modulo import *' '''
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import exit, platform
from math import * # from math import sqrt

print(platform, sqrt(4), sep=', ')
exit()