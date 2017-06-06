a = (1, 2, 3, 4, 5, 6)  # tuple
b = [1, 2, 3, 4, 5, 6]  # list
print(a)  # tuple
print(b)  # list
print(a.__sizeof__())
# 36
print(b.__sizeof__())
# 44

d = {(1, 2, 3): 4}  # Dictionary via key of tuple
print(d, type(d), d[(1, 2, 3)])
# {(1, 2, 3): 4} <class 'dict'> 4
# d = {[1, 1, 1] : 1} -> cant be used key of type list
print(type([1, 1, 1]))
# <class 'list'>

s, j, k, l = tuple(), (), 's', ('s',)  # Creating tuple
print(type(a), type(j), type(k), type(l))
# <class 'tuple'> <class 'tuple'> <class 'str'> <class 'tuple'>

