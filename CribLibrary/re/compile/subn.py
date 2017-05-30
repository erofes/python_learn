from re_compile_test import *



result = pattern_mac.subn(test2, test3) #subn to test3 add test2 where test2.re == pattern
print(result)
#('a Text b Text c Text', 3) where is 3 - number of replaces