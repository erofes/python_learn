# Finally will be executed in any case, is there any exception or not.
# Else will be executed if there are no exception
try:
    f = open('1.txt')
except FileNotFoundError:
    print("There are no such file!")

inst = []
try:
    for line in f:
        inst.append(int(line))
except ValueError:
    print("It's not a digit!")
except Exception:
    print("Unnamed exception")
else:
    print("All fine")
finally:
    try:
        f.close()
    except NameError:
        print("File was not created!")
    else:
        print("I closed file")
