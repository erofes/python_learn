# Manager of context
# Like try, except, finally

# "with" expression ["as" target] ("," expression ["as" target])* ":"
#    suite

with open('text.txt', 'w') as g:
    d = 2
    print('1 / {} = {}'.format(d, 1/d), file=g)
    # 1 / 2 = 0.5 -> in text.txt
