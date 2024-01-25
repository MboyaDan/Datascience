# file handling

# file modes
# "w" - write
# "r" - read
# "a" - append
# "w+" - read/write
# "r+" - read/write

# write to a file
f = open("example.txt" "w")
f.write("This is the first line")
f.close()

# read to a file
f = open("example.txt", "r")
f.read() # reads all the lines in the file
f.close()

# append to a file
f = open("example.txt", "a")
f.write("This is the second line")
f.close()