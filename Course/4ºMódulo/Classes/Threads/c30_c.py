# (Parte 3) Threads - Executando processamentos em paralelo

from time import sleep
from threading import Lock, Thread

class Ingressos:
    ''' 
    Classe que vende ingressos
    '''

    def __init__(self, estoque: int):
        ''' Inicializando...

        :param estoque: quantidade de ingressos em estoque
        '''
        self.estoque = estoque
        
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        '''
        Compra determinada quantidade de ingressos

        :param quantidade:  A quantidade de ingressos que deseja comprar
        :type quantidade:   int
        :return:            Nada
        :rtype:             None
        '''
        
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(
            f'Você comprou {quantidade} ingresso(s).'
            f'Ainda temos {self.estoque} em estoque.'
            )

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(
            target  =   ingressos.comprar,
            args    =   (i,)
            )
        t.start()

    print(ingressos.estoque)