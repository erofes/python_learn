c = [c * 3 for c in 'gor']
print(c)
# ['ggg', 'ooo', 'rrr']

c = [c * 3 for c in 'gor' if c != 'o']
print(c)
# ['ggg', 'rrr']

c = [c + d for c in 'gor' if c != 'o' for d in 'ROAD' if d != 'O']
print(c)
# ['gR', 'gA', 'gD', 'rR', 'rA', 'rD']

c = [[c, c*c] for c in range(1, 8)]
print(c)
# [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49]]
