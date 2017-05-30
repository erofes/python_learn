a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Intersection that changes current "a"   (     [XXXX)   ]
a |= b
print(a)
#{'d', 'f', 'b', '2', 'c', '1', '4', '5', '6', 'e', '3', 'a'}
a.intersection_update(c)
print(a)
#{'b', '2', 'c', '1', '3', 'a'}
a &= e
print(a)
#{'2', '3', '1'}


