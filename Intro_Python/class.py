#classes& objects
#A class is a user-defined blueprint or prototype from which objects are created.
#Classes are created by keyword class.
#Attributes are the variables that belong to a class.
#Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute
#objects are instances of a class
class Dog:
    #attributes
    #class variables
    at1 = "mammal"
    at2 = "dog"
    #methodss
    def fun(self):
        print("Iam a", self.at1)
        print("Iam a", self.at2)
    
#object instantiation

bosco = Dog()

#accessing class atrributes and methods through objects

print(bosco.at1)
bosco.fun()

#The __init__() Function

#self parameter
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.


#The method is useful to do any initialization you want to do with your object.
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
class house:
    #constructor
    def __init__(self,floor,window):
        self.floor = floor
        self.window = window

h1 = house("tile", "wodden")
print(h1.floor,h1.window)


#When we call a method of this object as myobject.method(arg1, arg2), this is automatically 
# converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

#class with a method

class GFG:
    #constructor
	def __init__(self, name, company):
     #instance variables
#Instance variables are variables whose value is assigned inside a constructor or method with self   
		self.name = name
		self.company = company
# sample method
	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()


#class with  __str__()method
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
 
    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."
 
 
my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)


#class

# Class for Dog
 
 
class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed):
 
        # Instance Variable
        self.breed = breed
 
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
 
    # Retrieves instance variable
    def getColor(self):
        return self.color
# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())


#Inheritance
#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called  derived class.
# Python program to demonstrate
# single inheritance

# Base class/parent class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()



# Python program to demonstrate
# multiple inheritance
 
# Base class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
