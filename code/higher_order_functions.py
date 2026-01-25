from functools import reduce


def sum_numbers(nums):
    return sum(nums)


# Python Closures
# Python allows a nested function to access the outer scope of the enclosing function.
def add_ten():
    ten = 10
    def add(number):
        return ten + number
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# Python Decorators
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of the function you want to decorate.

# To create a decorator function, we need an outer function within an inner wrapper function
def greeting():
    return 'welcome to python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper()

greeting_call = uppercase_decorator(greeting)
print(greeting_call)


@uppercase_decorator
def greeting_adam():
    return "welcome to python, from adam"

print(greeting_adam)


# adding multiple decorators to a single function
def split_string_decorator(function):
    def wrapper():
        input_function_call = function()
        split_string = input_function_call.split()
        return split_string
    return wrapper



@split_string_decorator
@uppercase_decorator
def greeting_two():
    return 'welcome to python'


print(greeting_two)


# accepting
def introduction_helper(function):
    def wrapper(first_name, last_name, country):
        function(first_name, last_name, country)
        return f'Hello, my name is {first_name} {last_name}. I am from {country}.'
    return wrapper


@introduction_helper
def introduction(first_name, last_name, country):
    return "First Name: {first_name}, Last Name: {last_name}"


my_introduction = print(introduction("Adam", "Worede", "United Kingdom"))


# built in high order functions
# examples of built in high order functions
# map, filter, reduce; these are functions that can be passed into another function
# Lambda functions can be passed into these functions as parameters
# the best usecases for lambda functions is to be passed into these functions

# map function
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


square_numbers = map(square, numbers)
print(list(square_numbers))

lambda_square_numbers = map(lambda x: x * x, numbers)
print(list(lambda_square_numbers))


# filter higher order function
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))


# reduce function is defined in the functools module, this returns a single value and not an iterable
# applie the function passed into the reduce function cumulatively to the items of the iterable. from left to right, returning a single value


def add_two_numbers(num_1, num_2):
    return num_1 + num_2


total = reduce(add_two_numbers, numbers)
print(f"This is the cumulative sum of the array: {total}")



