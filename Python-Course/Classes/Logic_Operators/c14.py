""" Operador lógico 'and' """
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy: 0, 0.0, '', False, None (usado para representar um não valor)
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

if entrada == 'E' and senha_digitada == '123456':
     print('Entrar')
else:
     print('Sair')

print(True and False and True) # False
print(True and 0 and True)     # 0