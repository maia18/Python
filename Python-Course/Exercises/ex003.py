primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(
        f"{primeiro_valor} é maior do que"
        f"{segundo_valor}"
        )
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor} é maior do que {primeiro_valor}")
elif primeiro_valor == segundo_valor:
    print("Os valores são iguais")
else:
    print("Nada a comparar")