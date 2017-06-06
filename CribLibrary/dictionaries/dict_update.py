d = dict(a=1, b=2, c=3, f=4)  # Update dict by elements from another dict
c = dict(a=4, b=9, d=6, e=7)
d.update(c)
print(d)
# {'d': 6, 'f': 4, 'a': 4, 'c': 3, 'b': 9, 'e': 7}

d = dict(a=1, b=2, c=3, f=4)
c = dict(a=4, b=9, d=6, e=7)
c.update(d)
print(c)
# {'d': 6, 'f': 4, 'a': 1, 'c': 3, 'b': 2, 'e': 7}
