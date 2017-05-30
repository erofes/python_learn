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