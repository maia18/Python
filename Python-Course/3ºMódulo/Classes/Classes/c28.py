""" __new__ e __init__ em classes Python """
# __new__  -> método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
# __init__ -> método responsável por inicializar a instância. Por isso, init recebe self.
# __new__ wwwwww ❗️DEVE retornar o novo objeto❗️
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # print('Antes de criar a instância...')
        instancia = super().__new__(cls)
        # print('Depois de criar a instância...')
        return instancia

    def __init__(self, x, ) -> None:
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)