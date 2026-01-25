from day_12_module import generate_full_name
import os
import sys
from statistics import *
import math
import string
from random import random, randint, choice, shuffle

print(generate_full_name("Adam", "Worede"))


# os.mkdir("day_12")

# changing the current directory
# os.chdir("path")

# get the current working directory
os.getcwd()

# removing directory
# os.rmdir()

# command line arguments
print(f"Firstname: {sys.argv[1]}. Lastname: {sys.argv[2]}")

# largest integer variable it takes
# sys.maxsize

# to know environment path
print(sys.path)

# to know the version of python you are using
print(sys.version)

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(median(ages))


print(math.pi)
print(string.ascii_letters)
print(type(string.ascii_letters))
print(random())
print(randint(5, 10))


def random_user_id():
    chars = list(string.ascii_lowercase + string.digits)
    
    rand_string = ""
    for i in range(0, 6):
        rand_string += choice(chars)
    
    return rand_string

def var_random_user_id(number_of_chars, number_of_ids):
    chars = list(string.ascii_letters + string.digits)
    
    rand_id = ""
    for j in range(0, number_of_ids):
        for i in range(0, number_of_chars):
            rand_id += choice(chars)
        print(rand_id)
        rand_id = ""


print(random_user_id())
var_random_user_id(5, 5)
var_random_user_id(16, 5)


def rgb_colour_gen():
    rgb_value = f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})"
    return rgb_value

print(rgb_colour_gen())

def generate_hex_value():
    hex_chars = list('abcdef0123456789')
    hex_value = f'#{choice(hex_chars)}{choice(hex_chars)}{choice(hex_chars)}{choice(hex_chars)}{choice(hex_chars)}{choice(hex_chars)}'
    return hex_value

def generate_colours(base, values):
    gen_values = []
    if base == "hexa":
        for i in range(0, values):
            gen_values.append(generate_hex_value())
    else:
        for i in range(0, values):
            gen_values.append(rgb_colour_gen())

    return gen_values


print(generate_colours('hexa', 12))
print(generate_colours('rgb', 3))


def shuffle_list(input_list):
    input_list_copy = input_list.copy()
    shuffle(input_list_copy)
    return input_list_copy


def random_numbers():
    return_list = []
    while len(return_list) < 7:
        random_number = randint(0, 9)
        if random_number in return_list:
            continue
        else:
            return_list.append(random_number)
    
    return return_list


print(random_numbers())
print(shuffle_list([1, 2, 3]))