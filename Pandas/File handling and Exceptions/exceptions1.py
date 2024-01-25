# exceptions - errors 

try:
    f = open("example.txt", "r")
    f.read()
    f.close()
except Exception as e:
    print("There was an error in reading the file ",e)


try:
    print(1/0)
except Exception as e:
    print("A number can not be divided by zero ", e)