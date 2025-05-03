"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
from random import choice

palavras = ["casa", "carro", "python", "livro", "java", "paralelepipedo"]
palavra_secreta = choice(palavras)

palavra = "_" * len(palavra_secreta)
tentativas = 0
while True:
    for i in range(len(palavra_secreta)):
        print(palavra)
        letra = input("Digite uma letra: ")
        tentativas += 1
        print(f"Tentativas: {tentativas}x")
        
        if len(letra) > 1:
            print('Digite apenas uma letra!')
            continue
        if (letra in palavra_secreta):
            if (palavra_secreta.count(letra) == 1):    
                index_letras = palavra_secreta.index(letra)
                palavra = palavra[:index_letras] + letra + palavra[index_letras + 1:]      
            elif (palavra_secreta.count(letra) > 1):
                index_letras = [i for i in range(len(palavra_secreta)) if palavra_secreta[i] == letra]
                for i in index_letras:
                    palavra = palavra[:i] + letra + palavra[i + 1:]     
        else:
            print('Errou :(')
            
    if palavra == palavra_secreta:
        print(f"Acertou!\n{palavra}")
        break