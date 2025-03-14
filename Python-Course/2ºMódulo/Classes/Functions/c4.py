""" Escopo de funções em Python """
# Escopo significa o local onde aquele código pode atingir.
# Existe o escopo global e local.
# O escopo global é o escopo onde todo o código é alcançavel.
# O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
# Não temos acesso a nomes de escopos internos nos escopos externos
# A palavra 'global' faz uma variável do escopo externo ser a mesma no escopo interno ( MÁ PRÁTICA )
x = 1

def escopo():
    global x
    x = 10
    print(f'{x=}')

    def outra_função():
        global x
        x = 11
        y = 2
        print(f'{x=} {y=}')
    outra_função()

print(x) # 1
escopo() # x=10, x=11 y=2
print(x) # 11