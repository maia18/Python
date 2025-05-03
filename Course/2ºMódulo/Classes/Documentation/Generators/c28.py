""" Generator expression, Iterables e Iterators em Python """
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
print(next(iterator), next(iterator), next(iterator), sep=', ') # Eu, Tenho, __iter__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))     # 8448728
print(sys.getsizeof(generator)) # 192

print(generator) # <generator object <genexpr> at 0x0000019F88A7D0C0>