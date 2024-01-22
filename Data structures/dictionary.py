# Creating a dictionary
person = {"name": "John", "age": 25, "city": "New York"}

# Accessing values
print(person["name"])  # Output: John

# Modifying values
person["age"] = 26
print(person)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Adding new key-value pairs
person["gender"] = "Male"
print(person)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'gender': 'Male'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 26, 'gender': 'Male'}