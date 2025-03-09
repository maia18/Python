""" Precedência entre operadores aritméticos """
# (n + n) -----> ** -----> * / // % -----> + -

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
conta_2 = (3 + ( -9 + 12 )) ** (2 * 1)

print(conta_1) # 1024
print(conta_2) # 36