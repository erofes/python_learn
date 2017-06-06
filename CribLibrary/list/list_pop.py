from CribLibrary.list.list_package import *

print(first)
# [1, 2, 3, 4, 5]
print(first.pop())  # pop last element
# 5
print(first)
# [2, 3, 4, 5]
# print(first.pop(333)) - !!!out of range!!!
print(first.pop(-1))  # pop last
print(first)
# [1, 2, 3]
