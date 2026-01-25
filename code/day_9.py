# conditionals
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more years to learn how to drive.")

my_age = 24

if my_age == age:
    print("You are the same age as me.")
elif my_age > age:
    print(f"You are {my_age - age} years younger than me.")
else:
    print(f"You are {age - my_age} years older than me.")

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))

if number_one == number_two:
    print(f"{number_one} is equal to {number_two}")
elif number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
else:
    print(f"{number_one} is less than {number_two}")


month = str(input("What month is it")).strip().lower()
if month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif month in ["december", "january", "february"]:
    print("The season is Winter.")
elif month in ["march", "april", "may"]:
    print("The season is Spring.")
else:
    print("The season is Summer.")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = str(input("Enter a fruit: "))
if fruit_input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_input)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person["skills"] is None:
    print("You have no skill")
else:
    print(person['skills'][len(person['skills']) // 2])
    if 'Python' in person['skills']:
        print("You can code in Python.")
    else:
        print("You can't code in Python.")
    if (len(person['skills']) == 2) and ('JavaScript' in person['skills']) and ('JavaScript' in person['skills']):
        print('You are a front end developer.')
    elif (set({'Node', 'Python', 'MongoDB'}).issubset(set(person['skills']))):
            print('You are a fullstack developer.')
    else:
        print("Unknown Title")

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")