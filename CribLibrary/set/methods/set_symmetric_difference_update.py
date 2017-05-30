a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Symmetric Difference that changes current "a"   (XXXX[        )XXXXX]
print(a)
#{'1', '2', '6', '4', '3', '5'}
a.symmetric_difference_update(c)
print(a)
#{'b', 'c', '6', 'a', '4', '5'}
a ^= c
print(a)
#{'1', '2', '6', '4', '3', '5'}


