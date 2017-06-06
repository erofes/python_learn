class A:
    def __init__(self, name):
        self.name = name

class B(A):
    def go(self, name):
        print('Go, {}!'.format(name))

a = A('Vasya')
print(a.name)
# Vasya

b = B('Arg')
print(b.go('Warg'))
# Go, Warg!
# None
