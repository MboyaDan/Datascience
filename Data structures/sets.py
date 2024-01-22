# Creating a set
colors = {"red", "green", "blue"}

# Adding elements
colors.add("yellow")
print(colors)  # Output: {'green', 'yellow', 'blue', 'red'}

# Removing elements
colors.remove("green")
print(colors)  # Output: {'yellow', 'blue', 'red'}

# Updating with update() method
my_set = {1, 2, 3}
other_set = {3, 4, 5}
my_set.update(other_set)
print(my_set)
# Output: {1, 2, 3, 4, 5}

# Unpacking with a loop
for element in my_set:
    print(element)

# Unpacking with the * operator
unpacked_set = {*my_set}
print(unpacked_set)