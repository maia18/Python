""" Funções recursivas e recursividade """
# Funções que podem se chamar de volta
# Úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
#   - Um problema que possa ser dividido em partes menores;
#   - Um caso recursivo que resolve o pequeno problema;
#   - Um caso base que para a recursão.
# Ex: fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

# RecursionError: maximum recursion depth exceeded -> Ocorre quando uma função recursiva não possui caso base e, devido a isso, é levada a um loop infinito.

''' Exemplo 1 '''
def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())