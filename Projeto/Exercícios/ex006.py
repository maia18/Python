"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input("Digit your first name: ")
if len(first_name) <= 4:
    print("Your name is short")
elif 5 <= len(first_name) <= 6:
    print("Your name is normal")
elif len(first_name) > 6:
    print("Your name is very big")
else:
    print("Is not an name...")