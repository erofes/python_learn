f = open('text.txt', 'r')

print(f.read(1))
# H
print(f.read())
# ello world!
# Im robot!

f.close()

f = open('text.txt')

for line in f:
    print(line)
# Hello world!
#
# Im robot!
f.close()

l = [str(i)+str(i-1) for i in range(20)]
print(l)
# ['0-1', '10', '21', '32', '43', '54', '65', '76',
# '87', '98', '109', '1110', '1211', '1312', '1413',
# '1514', '1615', '1716', '1817', '1918']

f = open('text.txt', 'w')

for index in l:
    f.write(index + '\n')  # Returns number of writen elements

f.close()

f = open("text.txt")

l = [line.strip() for line in f]
print(l)
# ['0-1', '10', '21', '32', '43', '54', '65', '76',
# '87', '98', '109', '1110', '1211', '1312', '1413',
# '1514', '1615', '1716', '1817', '1918']

f.close()

f = open("text.txt", 'w')

f.write("Hello world!\nIm robot!")

f.close()
