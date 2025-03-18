import importlib # A pure Python implementation of import
import c35

# print(c35.platform)

for i in range(10):
    importlib.reload(c35)
    print(i)

print('Fim')