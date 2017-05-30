import os



print("system, name: ", os.name) #Check filesystem name

print("environments, name: ", os.environ) #Check environments

print("os user: ", os.getlogin()) #Current user

print("PID is: ", os.getpid()) #Current pid id

print("system ", os.uname()) #More info about system

print("F_OK", os.access(os.getcwd(), os.F_OK)) #file exists
print("R_OK", os.access(os.getcwd(), os.R_OK)) #can read
print("W_OK", os.access(os.getcwd(), os.W_OK)) #can write
print("X_OK", os.access(os.getcwd(), os.X_OK)) #can exec

print("List: ", os.listdir(os.getcwd())) #current files in dir