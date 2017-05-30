a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')

if a.isdisjoint(b): #True if no same elements
    print('True')
else:
    print('False')
#True

if a.isdisjoint(c): #True if no same elements
    print('True')
else:
    print('False')
#False