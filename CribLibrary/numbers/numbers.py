import random

a = 10
b = 51

print(a + b)
# 61
print(a - b)
# -41
print(a * b)
# 510
print(a / b)
# 0.19607843137254902
print(b // a)
# 5
print(b % a)
# 1
print(abs(-a))
# 10
print(divmod(b, a))
# (5, 1)
print(b ** a)
# 119042423827613001
print(pow(a, b))
# 1000000000000000000000000000000000000000000000000000
print(pow(b, a, 256)) # via module 256
# 73
c = 4
print(c >> 1)
# 2
print(c << 1)
# 8
print(~0) #inversion of bits
# -1
print(~4) #inversion of bits
# -5
print(random.random())
# 0.9322248857298314
