def bool_test():
    print(bool(12))
    print(bool(-1))
    print(bool('a'))
    print(bool(12))
    print(bool(True))
    print(bool(False))
    # False
    print(bool(None))
    # False
    print(bool([]))
    # False
    print(bool([[]]))
    # True
    print(bool([[]][0]))
    # False


# bytearray
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
    # b[0] = b'w' #cant change item!


def complex_test():
    print(complex(1, 3))
    # (1+3j)


def range_test():
    for i in range(1, 10, 2):
        print(i)
        # 1,3,5,7,9


def slice_test():
    line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # square = (i for i in range(1000)) #cant go to [1:20:2]
    print(line[1:20:2])
    # [2, 4, 6, 8, 10, 12, 14]


def all_test():
    sequence = [1, 2, 3, 4, 5, 0]
    print(all(sequence))  # if any is "0" or False -> False
    # False
    sequence = [1, 2, 3, 4, 5]
    print(all(sequence))
    # True


def any_test():
    sequence = [1, 2, 3, 4, 5, 0]  # If any not "0" or False
    print(any(sequence))  # If any is "1" or True -> True
    # True
    sequence = [0, 0]
    print(any(sequence))
    # False


def max_min_test():
    sequence = [1, 2, 3, 4]
    print(min(sequence))
    # 1
    print(max(sequence))
    # 4


def sorted_test():
    sequence = [1, 2, 1, 3, 4]
    print(sorted(sequence))
    # [1, 1, 2, 3, 4]


def others_test():
    x = 10
    print('\n', bin(111)) # 2
    print('\n', oct(111)) # 8
    # 0b1101111
    print(callable(any_test))
    # True
    print(callable(x))
    # False
    x = 1.666666
    print(round(x, 1))  # rount to x symbols after ,
    # 1.7
    print(hex(56))
    # 0x38


def sum_test():
    sequence = [x for x in range(10)] # Sum elements
    print(sequence)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum(sequence))
    # 45

# bool_test()
# bytearray_test()
# bytes_test()
# complex_test()
# range_test()
# slice_test()
# all_test()
# any_test()
# max_min_test()
# sorted_test()
# sum_test()
others_test()

