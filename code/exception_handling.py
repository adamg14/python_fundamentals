# python uses try except to handle errors gracefully. exceptions are usally external to the program itsetl e.g. incorrect input; wrong file name or unable to find a file.
# try, except, else, finally

try:
    print(10 + '5')
except:
    print('something went wrong')


try:
    name = input('enter your name: ')
    birth_year = input('enter your year of birth: ')
    age = 2026 - birth_year
    print(f'your name is {name}, and you are {age} years old.')
except TypeError:
    print('a type error occurred')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('i usually run with the try block')
finally:
    print('i always run')

# shortening the code above 
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


def sum_of_five(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five(*lst))
