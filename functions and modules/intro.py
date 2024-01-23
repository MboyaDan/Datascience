# Functions
# built-in, user-defined, and lambda functions

# user-defined function
def display():
    print("Hello World")

# functions with parameters
# a is a parameter aka param
def myage(a):
    print("I am ",a," years old.")

# functions with return values
# a and b are params
# "return" keyword is used
def addition(a,b):
    return a + b

# built-in functions - they come pre-packaged. 
str1="Happy Coding!"
len(str1) # len() is a built-in function
str1.index("H") # index() is a built-in function for Strings

# lambda functions
# syntax - lambda argument : expression
lambda a : a * 2

# using the lambda function above
(lambda a: a * 2) (3) # output: 6
# In this case, value 3 is passed into the function and a is initialized to 3

# using lambda in a list
list1 = [1,2,3,4,5]

# option 1
result = (lambda a:a*2) (list1)
list(result)
print(result)
# result: [2,4,6,8,10]

# option 2 - using map() function
# syntax - map(function, argument)
result = map(lambda a: a * 2, list1)
list(result)
print(result)
# result: [2,4,6,8,10]



