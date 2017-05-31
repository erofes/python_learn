def bool_test():
    print(bool(12))
    print(bool(-1))
    print(bool('a'))
    print(bool(12))
    print(bool(True))
    print(bool(False))
    #False
    print(bool(None))
    #False
    print(bool([]))
    #False
    print(bool([[]]))
    #True
    print(bool([[]][0]))
    #False

#bytearray
def bytearray_test():
    b = bytearray(b'abc')
    print(b)
    b[0] = 101
    print(b)

def bytes_test():
    b = bytes(b'asdf')
    print(b)
    b += b'g'
    print(b)
    #b[0] = b'w' #cant change item!

#bool_test()
#bytearray_test()
bytes_test()
