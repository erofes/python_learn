# Anonymous function lambda
# Contains just one expression
# Faster than simple 'def function'

func = lambda x, y: x + y  # Create anonymous fast function of summary
print(func(1, 4))
# 5
print((lambda x, y: x - y)(4, 3))  # It can be just lambded
# 1
func = lambda *args: args
print(func(1, 2, 3, func))
# (1, 2, 3, <function <lambda> at 0x02503348>)
