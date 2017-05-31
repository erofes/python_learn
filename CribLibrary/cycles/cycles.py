i = 0
while i < 3: #while
    print(i)
    i += 1

for i in range(3, 11):
    if i > 5:
        continue
    else:
        print(i)
else:
    print("okay")

while True:
    if i != -1:
        break
    else:
        print('no way!')
else:
    print("not okay")