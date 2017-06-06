# Exceptions is one of types of data
# Is used for reporting about code errors
# Simplest exception division by zero
# 100 / 0
# ZeroDivisionError: division by zero
try:
    k = 1 / 0
except ZeroDivisionError:  # Exception of zero division
    k = 0

print(k)
# 0
# We can catch this exception by parent exception
try:
    k = 1 / 0
except ArithmeticError:
    k = 0

print(k)
# 0
# There are a global cather except:, but if you want to look for real problems in your code
# it's better to choose certain Exception codes
