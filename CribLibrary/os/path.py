import os


test_path = os.getcwd()
print("Test path: ", test_path)
    #Test path:  /home/se1/PycharmProjects/hull/CribLibrary/os

print("Absolute path: ", os.path.abspath(test_path)) #Returns path absolute
print("Base path: ", os.path.basename(test_path)) #Base name of dir
print("Split path: ", os.path.split(test_path)) #Split head from tail ->>>>
    #Split path:  ('/home/se1/PycharmProjects/hull/CribLibrary', 'os')

my_list = ["Самораспаковывающийся", "Самораспахивающийся", "Саморасх*яривающийся"]
print("Common prefix path: ", os.path.commonprefix(my_list)) #Find same head of list items
    #Common prefix path:  Саморас

print("Dirname: ", os.path.dirname(test_path)) #Show parent directory (sep = '/')
    #Dirname:  /home/se1/PycharmProjects/hull/CribLibrary

print("Path existing: ", os.path.exists(test_path)) #Check path exosting
print("Path existing: ", os.path.exists(test_path+"/"))
    #True
print("Path existing: ", os.path.exists(test_path+"2"))
    #False

print("Change ~ to another: ", os.path.expanduser("~/sekritutka/policer")) #Change ~ to root path
    #Change ~ to another:  /root/sekritutka/policer

print("Last change of others.py: ", os.path.getatime(test_path+"/others.py")) #Get last update time in seconds ERA
    #Last change of others.py:  1495534152.1971834

