""" Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.

"""
variavel_1 = 1

class Foo:
    def soma(
        x: (int | float), 
        y: (int | float)
    ) -> int | float:
        """ 
        Soma x e y

        :param x:  Número 1
        :param y:  Número 2
        :type  x:  int or float
        :type  y:  int or float

        :return:  A soma entre x e y
        :rtype :  int or float
        
        """
        return  x + y


    def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None
    ) -> int | float:
        """ 
        Multiplica x, y e/ou z

        Multiplica x e y. Se z for enviado, multiplica x, y, z.
        
        """
        if z is None:
            return x * y
        return x * y * z
    
    def bar(self):
        """
        
        O que ele faz
        
        :raises NotImplementedError: Se o método não for definido
        :raises ValueError: Se o método não for definido
        """

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4