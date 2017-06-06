# Access by key
# Unsorted
# HASH-tables or associative missives

d, g = {}, {'dict': 1, 'dictionary': 2}  # Creating dictionary
print(d, type(d), g, g['dict'])  # Access by key
# {} <class 'dict'> {'dict': 1, 'dictionary': 2} 1

d = dict(short='dict', long='dictionary')  # Creating via dict()
print(d, type(d), d['short'])
# {'short': 'dict', 'long': 'dictionary'} <class 'dict'> dict

d = dict.fromkeys(['a', 'b'], [10, 20])  # Third method via dict.fromkeys
print(d)
# {'a': [10, 20], 'b': [10, 20]}

# Generators of dictionary
d = {a: a ** 2 for a in range(7)}
print(d)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
