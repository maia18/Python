""" Exemplos """
# copy - retorna uma cópia rasa (shallow copy)
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

""" shallow copy (cópia rasa) """
# d2 = d1.copy() # d2 = copy(copy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1) # {'c1': 1, 'c2': 2, 'l1': [0, 999999, 2]}
# print(d2) # {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}

""" deep copy (cópia profunda) """
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
# print(d2) # {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}