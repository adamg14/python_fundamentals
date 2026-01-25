language = 'python'

# changing the string to a list
lst = list(language)
print(lst)

lst = [i for i in language]
print(lst)

squares = [(i, i*i) for i in range(0, 11)]
print(squares)

# even_numbers
evens = [i for i in range(0, 10) if i % 2 == 0]
print(evens)

# flattening lists
two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_list = [number for row in two_d_list for number in row]
print(flattened_list)


# lambda functions
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(1, 2, 3))

# self invoking lambda function
print((lambda a, b, c: a + b + c)(1, 2, 3))


# lambda function inside function
def power(x):
    return lambda n: x ** n

print(power(2)(3))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [number for number in numbers if number <= 0]
print(negative_numbers)

tuple_list = [(a, 1, a, a ** 2, a ** 3, a ** 4, a ** 5) for a in range(0, 11)]
print(tuple_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [(country[0].upper(), country[0][:3].upper(), country[1]) for element in countries for country in element]
print(flattened_countries)

dic_list = [
    {
        "country": country[0],
        "city": country[1]
    } for element in countries for country in element
]
print(dic_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [f"{name[0]} {name[1]}" for element in names for name in element]
print(full_name)

calculate_slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 -x1)
calculate_y_intercept = lambda x, y, m: y - m*x

