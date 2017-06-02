str1 = "TestString"
print(str1[::-1])
# gnirtStseT
print(str1 * 3)
# TestStringTestStringTestString
str1 = str1[0:4] + "New" + str1[4:]
print(str1)
# TestNewString
str2 = "11121111311141112112"
print(str2.find('2')) # find first enter
# 3
print(str2.rfind('2')) # find last enter
# 19
# print(str2.index('NotExistingString')) # ValueError - not found
print(str2.index('11')) # Find substring in string
# 0
print(str2.rindex('11')) # Find substring in string but last one
# 17
str2.replace('111', '444') # Not changes value
print(str2)
# 11121111311141112112
print(str2.replace('111', '444')) # Creates new output
# 44424441344444442112