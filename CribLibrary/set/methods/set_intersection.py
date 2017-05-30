a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')


print(a.intersection(c)) #Intersection (        [XXX)        ]
#{'1', '2', '3'}
print(a & c)
#{'1', '2', '3'}
print(c & a)
#{'2', '3', '1'}
