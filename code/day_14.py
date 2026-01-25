from functools import reduce
from countries import countries_list
from countries_data import country_data
# A higher order function is a function that - takes another function as the argument
# or a high order function returns a function
# This is the backbone of functional programming, pipelines and reusable logic


# Closures
# A closure is a function that remembers variable from its outer scope
# even after the outer function finished executing
# closures are powerful because it has configurable behaviour, has no global state as it is easy for global variables to be manipulated by accident and clean dependency injection
# parameterised transformations, validators, filters

# A decorator is a function that wraps another function to add behaviour to it without changing the function
# decorators are built with high order functions and closures

# call function version of map
numbers = [1, 2, 3, 4, 5]


def map_call_function(func, iter):
    map_list = []
    for i in range(0, len(iter)):
        map_list.append(func(iter[i]))
    return map_list


def filter_call_function(func, iter):
    filter_list = []
    for i in range(0, len(iter)):
        if func(iter[i]) == None:
            continue
        else:
            filter_list.append(func(iter[i]))
    return filter_list


def reduce_call_function(func, iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result = func(result, iter[i])
    return result


def sum(num1,  num2):
    return num1 + num2


def is_even(num):
    if num % 2 == 0:
        return num
    else:
        return None
    

def square(num):
    return num * num


print(map_call_function(square, numbers))
print(filter_call_function(is_even, numbers))
print(reduce_call_function(sum, numbers))


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)


upper_countries = map(lambda x: x.upper(), countries)
print(list(upper_countries))
square_numbers = map(lambda x: x**2, numbers)
print(list(square_numbers))
upper_names = map(lambda x: x.upper(), names)
print(list(upper_names))

def contains_land(country_name):
    if "land" in country_name:
        return False
    else:
        return True
    

filter_countries = filter(lambda country_name: "land" not in country_name, countries)
print(filter_countries)
filter_countries_2 = filter(lambda country_name: len(country_name) != 6, countries)
print(list(filter_countries_2))
filter_countries_3 = filter(lambda country_name: len(country_name) >= 6, countries)
print(list(filter_countries_3))
filter_countries_4 = filter(lambda country_name: country_name[0].lower() != 'e', countries)
print(list(filter_countries_4)) 

result = reduce(sum, filter(is_even, map(square, numbers)), 0)
print(result)


def get_string_list(input_list):
    return list(
            filter(
                lambda x: isinstance(x, str),
                input_list
            )
        )

print(get_string_list([1, "adam", 2, 3, "bob", "alice"]))

reduce_sum = reduce(lambda x, y: x + y, numbers, 0)
print(reduce_sum)

reduce_concat = reduce(
    lambda acc, next_country : acc + ', ' + next_country
                            if next_country != countries[-1] 
                            else acc + " and " + next_country,
    countries[1:],
    countries[0]
    ) + "are northen European countries."
print(reduce_concat)

def categorise_countries(substring, countries):
    filtered_list = filter(lambda x: substring in x, countries)
    return  list(filtered_list)   

print(categorise_countries('land', countries_list))


def add_key(input_dict, key):
    input_dict.update({key: 0}) 
    return input_dict

def increment_key(input_dict, key):
    input_dict[key] += 1
    return input_dict

def filter_list(iterable):
    filtered_list = reduce(
        lambda acc, x: add_key(acc, x[0]) if x[0] not in acc.keys()
        else increment_key(acc, x[0]),
        iterable,
        {}
    )
    return filtered_list

print(filter_list(countries_list))


def get_first_ten_countries():
    return countries_list[:10]


def get_last_ten_countries():
    return countries_list[:len(countries_list) - 11:-1]

print(get_first_ten_countries())
print(get_last_ten_countries())

# def sort_countries_lambda(sort_attribute):
    
def sort_countries(iterable, sort_attribute, reverse=False, return_length=None):
    sorted_countries_list = list(sorted(iterable, key=lambda x: x[sort_attribute], reverse=reverse))
    if return_length is None:
        return sorted_countries_list
    else:
        return sorted_countries_list[:return_length]


print(sorted(country_data, key=lambda x: x["name"]))
print(sort_countries(country_data, "name", False))
print(sort_countries(country_data, "population", True))
print(sort_countries(country_data, "population", False, 10))