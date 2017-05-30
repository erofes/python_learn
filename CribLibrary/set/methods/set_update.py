a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Operation that changes current "a" by unioning  (XXXXXX) [XXXXXXX]
print(a)
#{'4', '5', '3', '6', '1', '2'}
a.update(c)
print(a)
#{'4', '5', 'a', 'c', 'b', '3', '6', '1', '2'}
a |= b
print(a)
#{'4', '5', 'a', 'c', 'd', 'e', 'b', '3', 'f', '6', '1', '2'}


