a = set('123456')
b = set('abcdef')
c = set('123abc')
d = set('111aaa')
e = set('123')

if e.issubset(a): #True if e is subset of a
    print('True')
else:
    print('False')
#True

if e <= a: #True if e is subset of a
    print('True')
else:
    print('False')
#True

if a.issubset(e):
    print('True')
else:
    print('False')
#False