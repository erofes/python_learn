d = dict(a=1, b=2, c=3, f=4)
print(d.setdefault('a', 5), d)  # If exists, returns existing value
# 1 {'f': 4, 'a': 1, 'b': 2, 'c': 3}
print(d.setdefault('d', 8), d)  # if not -> adds and returns it's value
# 8 {'f': 4, 'a': 1, 'd': 8, 'b': 2, 'c': 3}
print(d.setdefault('k'), d)  # if default not exists -> it's None
# None {'k': None, 'b': 2, 'a': 1, 'd': 8, 'c': 3, 'f': 4}