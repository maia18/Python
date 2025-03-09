""" Operador lógico 'or' """
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy: 0, 0.0, '', False, None (usado para representar um não valor)
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

if (entrada == 'E' or entrada == 'e') and (senha_digitada == '123456'):
    print('Entrar')
else:
    print('Sair')

outra_senha = input('Senha: ') or 'Sem senha'
print(outra_senha)