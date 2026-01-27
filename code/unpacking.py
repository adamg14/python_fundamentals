def five_sum(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(five_sum(*lst))

# this will return the array [2, ..., 6]
numbers = range(2, 7)
print(list(numbers))

args = [2, 7]
numbers = range(*args)
# this will return the same array
print(list(numbers))

# a list or tuple can also be unpacked like this
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
finland, sweden, norway, *rest = countries
print(rest)

numbers = [i for i in range(0, 11)]
print(numbers)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

# unpacking a dictionary 
def personal_info(name, country, city, age):
    print(f"My name is {name}.")
    print(f"I am from {country}.")
    print(f"I live in {city}.")
    print(f"I am {age} years old.")
    return None

person = {
    "name": "Bob",
    "country": "America",
    "city": "London",
    "age": 100
}

print(personal_info(**person))

# packing list g
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all(1, 2, 3, 4, 5))

# packing dictionaries
def packing_personal_info(**kwargs):
    print(f"These are the kwargs: {kwargs}")
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")
    return kwargs

print(packing_personal_info(name="Bob", country="America", city="London", age=100))

# spreading in python
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# enumerate is a built in function to get the index of each item in the list
for index, item in enumerate([10, 20, 30, 40]):
    print(index, item)

# zip
# combine lists when iterating through them 
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veg = []
for f, v in zip(fruits, vegetables):
    fruits_and_veg.append((f, v))

print(fruits_and_veg)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, estonia, russia = names
print(nordic_countries)
print(estonia)
print(russia)