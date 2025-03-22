''' EXEMPLO 2 '''
class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self): 
        super().metodo()          # B ---> super(C, self).metodo()
        super(B, self).metodo()   # A
        # super(A, self).metodo()   # object
        # A.metodo(self)
        # B.metodo(self)
        print('C')


c = C('Atributo', 'Qualquer')

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

print(C.mro()) # [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(B.mro()) # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(A.mro()) # [<class '__main__.A'>, <class 'object'>]

print(c.atributo)       # Atributo
print(c.outra_coisa)    # Qualquer