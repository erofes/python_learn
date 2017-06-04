i = 0
while i < 3: #while
    print(i)
    i += 1
# 0
# 1
# 2

for i in range(3, 11):
    if i > 5:
        continue
    else:
        print(i)
else:
    print("okay")
# 3
# 4
# 5
# okay

while True:
    if i != -1:
        break
    else:
        print('no way!')
else: # Exit without using BREAK will lead us here ->
    print("not okay")
print('breaks finally')
# breaks finally
