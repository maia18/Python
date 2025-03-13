"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> Entregue-me o próximo valor
iter -> Entregue-me seu iterador
"""
texto = 'Luiz'  # iterável

iterador = iter(texto)  # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break