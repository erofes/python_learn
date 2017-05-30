a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

if e.issuperset(a): #True if e is NOT subset of a
    print('True')
else:
    print('False')
#False

if e >= a: #True if e is NOT subset of a
    print('True')
else:
    print('False')
#False

if a.issuperset(e):
    print('True')
else:
    print('False')
#True