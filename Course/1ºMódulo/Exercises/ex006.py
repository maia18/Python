"""
Faça um programa que pergunte a hora ao usuário.
Baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia (0h-11h), Boa tarde (12h-17h) e Boa noite (18h-23h).
"""
hora = input('Que horas são? ')

try:
    hora_int = int(hora)
    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    elif 18 <= hora_int <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida.')
except:
    print('Isso não é uma hora válida')