my_list = list("abcdef") # Creatinh list
print(my_list)
#['a', 'b', 'c', 'd', 'e', 'f']

first_list = [] # Empty list
print(type(first_list))
#<class 'list'>

second_list = ["a","b",["c", "d"]] #Another creating
print(second_list)
#['a', 'b', ['c', 'd']]

third_list = [c * 3 for c in 'list'] #Using generator to create list
print(third_list)
#['lll', 'iii', 'sss', 'ttt']

c = [c + d for c in '123' if c != '2' for d in 'abc' if d != 'b'] #example from site
print(c)
#['1a', '1c', '3a', '3c']

fourth_list = [ [x, y, x + y] for x in range(1, 4) for y in range(1, 4)] #self-made
print(fourth_list)
#[[1, 1, 2], [1, 2, 3], [1, 3, 4], [2, 1, 3], [2, 2, 4], [2, 3, 5], [3, 1, 4], [3, 2, 5], [3, 3, 6]]
