a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Remove element. No KeyError.
just_element = '7'
print(a)
#{'1', '5', '2', '4', '6', '3'}
a.discard(just_element)
print(a)
#{'1', '5', '2', '4', '6', '3'}
just_element = '6'
a.discard(just_element)
print(a)
#{'1', '5', '2', '4', '3'}

