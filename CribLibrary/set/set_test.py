a = set('123456')
b = set('abcdef')
c = set('123abc')

print(a, '\n', b, '\n', c)  # in random order no repeats
# {'5', '3', '6', '2', '1', '4'}
# {'e', 'd', 'b', 'a', 'f', 'c'}
# {'3', '2', 'b', '1', 'a', 'c'}

print({'a', 'a', 'b'})  # set could be inited via {}
# {'a', 'b'}
param = {'a', 'b'}
print(type(param))
# <class 'set'>
param = {}  # but..
print(type(param))  # must be not empty
# <class 'dict'>
