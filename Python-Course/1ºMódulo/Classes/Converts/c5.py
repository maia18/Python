''' Conversão de tipos, coerção '''
# Converte um tipo em outro
# Outras nomenclaturas: type convertion, typecasting, coercion

""" Tipos imutáveis e primitivos """
# str, int, float, bool

# print('1' + 1) --> TypeError: can only concatenate str (not "int") to str
print(str(11) + 'b')            # 11b
print(int('1'), type(int('1'))) # 1 <class 'int'>
print(type(float('1') + 1.2))   # <class 'float'>
print(bool(' '), bool(''))      # True False