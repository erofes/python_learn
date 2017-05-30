a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')


print(a.difference(c)) #difference a from c (XXXXXX[     )      ]
#{'5', '4', '6'}
print(a - c)
#{'5', '4', '6'}
print(c - a)
#{'b', 'c', 'a'}
