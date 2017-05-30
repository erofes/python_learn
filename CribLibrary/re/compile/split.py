from re_compile_test import *



result = pattern_mac.split(test) #split by pattern (remove all mac's, make semicolons)
print(result)
#test =
#"vlan 2     g1 192.168.0.102   20:bb:c0:78:9d:4d   dynamic"
#=>
#['vlan 2     g1 192.168.0.102   ', '   dynamicvlan 3     g1 192.168.0.102   ', '   dynamic']