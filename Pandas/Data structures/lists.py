# List - can contain different data types

# initialize a list
list1 = ["Happy", "Coding", 2024]

# indexing a list
# index start from 0
first_element = list1[0]


# iterating through a list
# use for loop
for element in list1:
    print(element)

# modifying elements
# modify first element
list1[0] = "Hello"

# append element
list1.append("Hello World")

# Appending multiple elements using extend()
list1.extend([5, 6, 7])

# remove an element
list1.remove(2024)

# pop an element - removes an element from any position
list1.pop(1)

# reverse elements of a list
list2 = list1.reverse()

# return position of an element in a list
pos = list1.index("Coding")




