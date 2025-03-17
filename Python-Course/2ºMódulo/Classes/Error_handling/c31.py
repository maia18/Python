""" try e except para tratar exceções """
try:
    a = 18
    b = 0
    
    # print(b[0]) --> 'int' object is not subscriptable
    # print('Linha 1'[1000]) --> string index out of range
    # print('Linha 1'[111])
    
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nomes indefinidos!')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO!!')
    
print('CONTINUAR')