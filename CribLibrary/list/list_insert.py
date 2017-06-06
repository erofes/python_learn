from CribLibrary.list.list_package import *

print(first)
# [1, 2, 3, 4, 5]
first.insert(0, 'q')  # insert to pos
print(first)
# ['q', 1, 2, 3, 4, 5]
first.insert(-1, 'q')  # insert to pos
print(first)
# ['q', 1, 2, 3, 4, 'q', 5]
first.insert(111, 'q')  # insert to pos
print(first)
# ['q', 1, 2, 3, 4, 'q', 5, 'q']
