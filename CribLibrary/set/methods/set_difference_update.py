a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Bite operation
#Difference that changes current "a"   (XXXX[        )    ]
a |= b
print(a)
#{'f', 'd', '1', '5', '2', '3', 'a', '4', 'b', 'e', '6', 'c'}
a.difference_update(b)
print(a)
#{'1', '5', '2', '3', '4', '6'}
a -= c
print(a)
#{'4', '5', '6'}


