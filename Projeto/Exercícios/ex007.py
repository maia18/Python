"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
new_string = ''
c = 0
while c < len(nome):
    new_string += f"*{nome[c]}"
    c+=1
new_string += "*"
print(new_string)