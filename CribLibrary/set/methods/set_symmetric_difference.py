a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')


print(a.symmetric_difference(c)) #difference of both a and c (XXXXXX[     )XXXXXX]
#{'c', 'b', '6', '4', 'a', '5'}
print(a ^ c)
#{'c', 'b', '6', '4', 'a', '5'}
print(c ^ a)
#{'c', 'b', '6', '4', 'a', '5'}

