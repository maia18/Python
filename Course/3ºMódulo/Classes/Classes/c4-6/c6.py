""" Mantendo estados dentro da classe """
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()         # Canon está filmando...
c1.filmar()         # Canon JÁ está filmando...
c1.fotografar()     # Canon não pode fotografar filmando
c1.parar_filmar()   # Canon está parando de filmar...
c1.fotografar()     # Canon está fotografando...

print()

c2.parar_filmar()   # Sony NÃO está filmando...
c2.filmar()         # Sony está filmando...
c2.filmar()         # Sony JÁ está filmando...
c2.fotografar()     # Sony não pode fotografar filmando
c2.parar_filmar()   # Sony está parando de filmar...
c2.fotografar()     # Sony está fotografando...