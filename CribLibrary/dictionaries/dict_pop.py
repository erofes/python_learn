d = dict(a=1, b=2, c=3, f=4)  # Returns values (default too)
print(d.pop('a'), d.keys())
# 1 dict_keys(['c', 'b', 'f'])
print(d.pop('b'), d.keys())
# 2 dict_keys(['c', 'f'])
print(d.pop('c'), d.keys())
# 3 dict_keys(['f'])
print(d.pop('f'), d.keys())
# 4 dict_keys([])
print(d.pop('f', None), d.keys())  # Default getting value as second argument
# None dict_keys([])