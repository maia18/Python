""" Polimorfismo em Python Orientado a Objetos """
# 📍 Polimorfismo - princípio em que classes derivadas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
# 📚 Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura).

# Opinião + princípios que contam:
#   • Assinatura do método: nome, parâmetros e retorno iguais
#   • SO"L"ID
#   • Princípio da substituição de liskov

# Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.
#  Sobrecarga  de métodos (overload) 🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificação(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class Email_Notificação(Notificação):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class SMS_Notificação(Notificação):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificação):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('NOTIFICAÇÃO ENVIADA!')
    else:
        print('NOTIFICAÇÃO NÃO ENVIADA!')


notificacao_email = Email_Notificação('testando e-mail')
notificar(notificacao_email) # E-mail: enviando -  testando e-mail
                             # NOTIFICAÇÃO ENVIADA!
                             
notificacao_sms = SMS_Notificação('testando SMS')
notificar(notificacao_sms)  # SMS: enviando -  testando SMS
                            # NOTIFICAÇÃO NÃO ENVIADA!