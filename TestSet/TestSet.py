import re



a = set()
b = set()

my_file1 = open("TestSet.txt", "r")
my_file2 = open("TestSet2.txt", "r")

############################################
#pattern = re.compile('\w+')

#result = pattern.findall(my_file2.readline())
#print(result)

#a.add(result[0])
#a.add(pattern.findall(my_file2.readline())[0])
#a.add(pattern.findall(my_file2.readline())[0])

#print(a)
#
#['car']
#{'g', 'car', 'bbt'}
############################################

#pattern = re.compile('\s\w+:\w+:\w+:\w+:\w+:\w+')

#result = pattern.findall(my_file1.readline())
#result = result[0].strip(' ')
#print(result)

#print(pattern.findall(my_file1.readline())[0].strip(' '))
#
#00:02:d1:1d:cb:36
#00:02:d1:1d:cb:3b
#############################################
#while True:
#    answer = my_file1.readline()
#    print(answer)
#    if (answer == ''):
#        break

#
#   2       00:02:d1:1d:cb:36     g1    dynamic   \n
#   2       00:02:d1:1d:cb:3b     g1    dynamic   \n
#   2       00:02:d1:1d:cb:3c     g1    dynamic   \n
#   2       00:02:d1:1d:cb:3d     g1    dynamic   \n
#   2       00:0b:0e:0f:00:ed     g1    dynamic
#############################################
pattern = re.compile('\w+:\w+:\w+:\w+:\w+:\w+')
pattern = re.compile('.+')
while True:
    data = pattern.findall(my_file1.readline())
    if data == []:
        while True:
            data = pattern.findall(my_file2.readline())
            if data == []:
                break
            else:
                b.add(data[0].strip(' '))
        break
    else:
        a.add(data[0].strip(' '))

print(a)
print(b)
c = a & b
d = a ^ b
f = a - b
g = b - a
#print("Intersecti:", c) #intersecion
#print("Difference:", b - a, "\n") #difference

print("Difference1:\n")
for i in f:
    print(i)

print("Difference2:\n")
for i in g:
    print(i)

#print(a & b)