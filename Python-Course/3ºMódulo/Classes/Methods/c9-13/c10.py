""" @staticmethod """
# Métodos estáticos são inúteis em Python; 
# São métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe.
class Classe:
    @staticmethod
    def função_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


def funçao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()                           
c1.função_que_esta_na_classe(1, 2, 3)       # Oi (1, 2, 3) {}
funçao(1, 2, 3)                             # Oi (1, 2, 3) {}

Classe.função_que_esta_na_classe(nomeado=1) # Oi () {'nomeado': 1}
funçao(nomeado=1)                           # Oi () {'nomeado': 1}