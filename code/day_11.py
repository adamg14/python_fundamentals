from math import pi
from math import sqrt
from countries_data import country_data
from collections import Counter


def add_two_numbers(number_1, number_2):
    return number_1 + number_2


def area_of_circle(radius):
    return pi * (radius ** 2)


def add_all_nums(*numbers):
    sum = 0
    for num in numbers:
        try:
            sum += float(num)
        except TypeError:
            return f"unable to parse this {num} a number."
    
    return sum


def convert_celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * (9/5) + 32)


def check_season(month):
    clean_month = month.strip().lower()
    if clean_month == "january" or clean_month == "february" or clean_month == "december":
        return "Winter"
    elif clean_month == "september" or clean_month == "october" or clean_month == "november":
        return "Autumn"
    elif clean_month == "march" or clean_month == "april" or clean_month == "may":
        return "Spring"
    elif clean_month == "june" or clean_month == "july" or clean_month == "august":
        return "Summer"
    else:
        return "invalid input"


def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    return (
        (-b + sqrt(b ** 2 - 4*a*c)) / 2 * a
        ,
        (-b + sqrt(b ** 2 - 4*a*c)) / 2 * a
    )


def print_list(input_list):
    for item in input_list:
        print(item)

    
def reverse_list(input_list):
    return input_list[::-1]
    
def capitalise_list_items(words):
    return list(map(lambda word: word.capitalize(), words))


def add_item(input_list, input_item):
    input_list.append(input_item)
    return input_list


def item(input_list, input_item):
    input_list.remove(input_item)
    return input_list


def sum_of_numbers(number_range):
    return sum(range(0, number_range + 1))


def sum_of_odds(number_range):
    sum = 0
    for i in range(0, number_range + 1):
        if i % 2 ==  0:
            continue
        else:
            sum += i
    return sum

def evens_and_odds(number):
    odd_count = 0
    even_count = 0
    for i in range(0, number + 1):
        if i % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
    
    return f"""The number of odds are {odd_count}.\nThe number of evens are {even_count}"""


def factorial(number):
    factorial = number
    for i in range(number - 1, 0, -1):
        factorial *= i
    return factorial


def calculate_mean(input_list):
    return sum(input_list) / len(input_list)


def calculate_median(input_list):
    return input_list[len(input_list) / 2]


def calculate_mode(input_list):
    return max(set(input_list), key=input_list.count)


def calculate_range(input_list):
    return input_list.sort()[-1] - input_list.sort()[0]


def calculate_variance(input_list ):
    calculated_mean = calculate_mean(input_list)
    
    sum = 0
    for i in range(0, len(input_list)):
        sum += ((input_list[i]) ** 2)

    return sum / (len(input_list) - 1)


def calculate_std(input_list):
    return sqrt(calculate_variance(input_list))


def is_prime(input_number):
    for i in range(input_number - 1, 1, -1):
        if input_number % i == 0:
            return False
    return True


def is_unique_values(input_list):
    return len(set(input_list)) == len(input_list)


def same_type(input_list):
    first_item_type = type(input_list[0])

    for item in input_list:
        if type(item) == type(first_item_type):
            continue
        else:
            return False
    
    return True


def valid_variable_name(name):
    if not isinstance(name, str):
        return False
    if not name.isidentifier():
        return False
    return True


def most_spoken_language(countries_list):
    language_counter = Counter()

    for country in countries_list:
        language_counter.update(country['languages'])

    def output_string(input_tuple):
        return f"The {input_tuple[0]} language is spoken in {input_tuple[1]} different countries"
    
    return language_counter.most_common(10)


def most_populated_countries(countries_list):
    top_20 = sorted(countries_list, key=lambda x:x['population'], reverse=True)[:20]

    keys_to_keep = ["name", "capital", "currency", "population"]

    filtered_countries = [
    {key: country[key] for key in keys_to_keep if key in country}
    for country in top_20
]
    return filtered_countries

print(most_populated_countries(countries_list=country_data))