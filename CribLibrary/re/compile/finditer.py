from re_compile_test import *



result = pattern_mac.finditer(test3) #iterator
print(result)
#<callable_iterator object at 0x7f75d3946eb8>
for i in result:
    print(i)
#<_sre.SRE_Match object; span=(2, 19), match='21:bb:c0:78:9d:4d'>
#<_sre.SRE_Match object; span=(22, 39), match='21:bb:c0:78:9d:4d'>
#<_sre.SRE_Match object; span=(42, 59), match='22:bb:c0:78:9d:4d'>

#
#for i in result:
#    print(i)
#=>None (yield)