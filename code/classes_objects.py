# Python is an object oriented programming.
# everything in python is an object with properties and methods
# e.g. a number or a string is a program with an object of corresponding built-in class
# create a class to create an object, a class is like an object constructor or blueprint for creating objects
# instantiate a class to create an object
# the class defines the behaviour and attributes of the object, the object represents the class

# defining the class
class Person:
    # defining the constructor for the class
    def __init__(self, name):
        self.name = name
    pass

# creating an object
p = Person('Alice')
print(p)
print(p.name)
