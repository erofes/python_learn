a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')


print(a.union(b)) #Union of both sets (XXXXXXX) [XXXXXXXXX]
#{'1', 'a', 'd', 'e', 'c', '5', '3', 'f', '2', 'b', '4', '6'}
print(b | a)
#{'1', 'a', 'd', 'e', 'c', '5', 'f', '3', 'b', '2', '4', '6'}