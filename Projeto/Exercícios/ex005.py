"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

date_ = input("Digit the hour: ")
if 0 <= int(date_) <= 11:
    print(f"Good morning!, it's {(date_)}h")
elif 12 <= int(date_) <= 17:
    print(f"Good afternoon!, it's {(date_)}h")
elif 18 <= int(date_) <= 23:
    print(f"Good evening!, it's {(date_)}h")
else:
    print("Invalid hour...")