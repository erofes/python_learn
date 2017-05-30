import re



test = "vlan 2     g1 192.168.0.102   20:bb:c0:78:9d:4d   dynamic"
test += "vlan 3     g1 192.168.0.102   33:bb:c0:78:9d:4d   dynamic"
test2 = "Text"
test3 = "a 21:bb:c0:78:9d:4d b 21:bb:c0:78:9d:4d c 22:bb:c0:78:9d:4d"
pattern_mac = re.compile('\w+:\w+:\w+:\w+:\w+:\w+') #take mac from any text