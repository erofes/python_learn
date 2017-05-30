a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

#Remove element. Care of KeyError.
#just_element = '7' => exception KeyError
just_element = '6'
print(a)
#{'6', '3', '1', '2', '5', '4'}
a.remove(just_element)
print(a)
#{'3', '1', '2', '5', '4'}

