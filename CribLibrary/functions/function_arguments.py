def func(a, b, c = 2):  # a, b is necessary! c is not necessary
    return a + b + c

print(func(1, 2, 3), func(1, 2), func(a=2, b=3))  # There are ways to use arguments
# 6 5 7


def many(*args):  # Must take any number of elements, unnamed tuple
    '''Custom description: Return input arguments'''
    return args  # it's tuple type

print(many(1, 2, 3, 'abc', func), many(1))
# (1, 2, 3, 'abc', <function func at 0x0025B228>) (1,) -> It's tuple!


def other_many(**args):  # It takes only NAMED arguments
    return args

print(other_many(a=1, b=2, c=3))
# {'a': 1, 'c': 3, 'b': 2} -> It's dictionary!
