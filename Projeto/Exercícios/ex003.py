"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input("Digit your name: ").upper()
age_str = input("Digit your age: ")
if name != "" or age_str != "":
    print(f"Your name is {name}. Your reverse name is: {name[::-1]}. Your name have spaces? {name.__contains__(" ")}. Your name have a len of {len(name)} characters. The first letter of your name is: {name[0]}. The last letter of your name is: {name[-1]}.")
else:
    print("Sorry, your don't answer the ask.")