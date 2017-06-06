# Private function
class A:
    def __private(self):
        print("Private function")


a = A()
# a.__private() -> private method
a._A__private()  # It's still works! If there are class name before.
# Private function


# Inherit
class Mydict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)

a = dict(a=1, b=2)
b = Mydict(a=1, b=2)
print(a.get('v'), b.get('v'))
# None 0