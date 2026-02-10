# JSON is a stringified JavaScript Object or a Python Dictionary
import json

# JSON
person = '''{
    "name": "Bob",
    "country": "United Kingdom",
    "city": "London",
    "skills": ["JavaScript", "Python"]
}'''

# convert the JSON into a python dictionary
person_dictionary = json.loads(person)

print(person)
print(type(person))
print(person_dictionary)
print(type(person_dictionary))

print(person_dictionary['name'])

# changing the dictionary into JSON
person_json = json.dumps(person_dictionary, indent=4)
print(person_json)
print(type(person_json))

with open('./code/files/person.json', 'w') as json_file:
    json_file.write(person_json)

