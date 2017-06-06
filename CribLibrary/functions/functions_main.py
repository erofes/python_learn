# Named functions 'def'
def add(x, y):
    return x + y  # Return value


print(add(1, 4), add('abc', 'def'))
# 5 abcdef
# Function can return ANY object, even another function


def choose_function(choose):
    if choose:
        def added(x, y):
            return x + y

        return added
    else:
        def con(x, y):
            return x - y

        return con


function1 = choose_function(True)
function2 = choose_function(False)
print(function1(1, 5), function2(1, 5))
# 6 -4


def func():
    pass

print(func())
# None
