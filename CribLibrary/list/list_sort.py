from CribLibrary.list.list_package import *

first.insert(0, 6)
print(first)
#[6, 1, 2, 3, 4, 5]
first.sort()
print(first)
#[1, 2, 3, 4, 5, 6]
first.sort(reverse=True)
print(first)
#[6, 5, 4, 3, 2, 1]
first.sort(key=lambda d: d == 5)
print(first)
#[6, 4, 3, 2, 1, 5]


#first.insert(0, '6')
#first.sort() #ERROR int and str