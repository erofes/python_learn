print('This is {} string'.format('experemental'))  # Change {} to choosen string
# This is experemental string

print("{} {} {} {}".format('This', 'is', 'experemental', 'string'))  # Change {} {} {} {} to strings
# This is experemental string

print("Destroy me {1} {2}".format("boy", "fat", "monster"))  # It starts from 0
# Destroy me fat monster

print("{} {} {} {} {}".format(*"super char"))  # *indicates a literalS
# s u p e r

print("{1} {1} {1}".format("true", 'false'))  # Can be multiplyed
# false false false

print("You are {robot}, and you can {speak}".format(robot='Human', speak='eat'))
# You are Human, and you can eat

t = [1, 2, '3']
print('test {t[2]!s}'.format(t=t), 'test {t[2]!r}'.format(t=t))
# Must declare left args to real args, use lists. !r and !s difference
# test 3 test '3'
