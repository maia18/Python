import datetime

nome = "Nelson"
sobrenome = "Kauê"
idade = 21
ano_nascimento = (datetime.date.today().year) - idade
altura = 1.8

print('Nome: ', nome)                          # Nelson
print('Sobrenome: ', sobrenome)                # Kauê
print('Idade: ', idade)                        # 21
print('Ano de nascimento: ', ano_nascimento)   # 2004
print('Maior de idade? ', idade >= 18)         # True
print(f'Altura em metros: {altura:.2f}')       # 1.80