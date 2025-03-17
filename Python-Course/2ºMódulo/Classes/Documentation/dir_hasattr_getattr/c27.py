""" dir, hasattr e getattr em Python"""
string = 'LUCAS'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe {metodo}', 
          getattr(string, metodo)(), sep='\n')
else:
    print('Não existe o método', metodo)