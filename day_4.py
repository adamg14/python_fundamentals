# strings
string_1 = "thirty" + "days" + "of" + "python"
company = "Coding for All"
company2 = "Python for Everyone"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

# capitalize(), title(), swapcase() 
print(company.capitalize())
print(company.title())
print(company.swapcase())

# slice the first string
print(company[0:6])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))
print(company.split(" "))

string_2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_2.split(","))

print(company[0])
# last index
print(len(company) - 1)
print(company[10])

acronym = ''.join(word[0].upper() for word in company.split())
acronym2 = ''.join(word[0].upper() for word in company2.split())
print(acronym)
print(acronym2)

print("Coding For All".index("C"))
print("Python For Everyone".index("F"))
print("Coding For All".rindex("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.rindex("because"))

print(sentence.replace("because because because", ""))

print("Coding For All".startswith("Coding"))
print("Coding For All".endswith("coding"))

setence2  = '   Coding For All      '
print(setence2.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

string_3 = "I am enjoying this challenge.\nI just wonder what is next"
print(string_3)

string_4 = "Name\tAge\tCountry\tCity\nAsabeneh 250\tFinland\tHelsinki"
print(string_4)

a = 8
b = 6
print(f"{a} + {b} = { a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // 6}")
print(f"{a} ** {b} = {a ** b}")