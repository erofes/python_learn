from re_compile_test import *



result = pattern_mac.match(test3) #match string starts at begin pos (0)
print(result) #None
result = pattern_mac.match(test3, 2) #match string starts at this pos
print(result)
#<_sre.SRE_Match object; span=(2, 19), match='21:bb:c0:78:9d:4d'>
print(result.string)
#a 21:bb:c0:78:9d:4d b 21:bb:c0:78:9d:4d c 22:bb:c0:78:9d:4d
print("Group ", result.group()) #return found substring (after re)
#21:bb:c0:78:9d:4d