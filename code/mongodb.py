import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

MONGODB_URI = os.environ['CONNECTION_STRING']
client = pymongo.MongoClient(MONGODB_URI)

print(f"This should be the client {client}")

db = client.school

db.students.insert_one({
    "name": "Bob",
    "country": 'United Kingdom',
    "city": "London",
    "class": ["English"]
})

print(client.list_database_names())


def get_students():
    students = db.students.find({})
    return students


example_query = {
    "city": "London"
}

# GET
def get_students(query, limit=None, sort='name', reverse=-1):
    filtered_students = db.students.find(query).limit(limit).sort(sort, reverse)
    return filtered_students

def find_student(input_name):
    student = db.students.find_one({
        "name": input_name
    })
    return student

# ADD
def get_student_details():
    print("********************")
    print("Enter Student Details")
    print("********************")

    name = str(input("Enter your full name: "))
    country = str(input("Enter your country: "))
    city = str(input("Enter your city: "))
    subjects = str(input("Enter your subjects (seperate with ,): "))
    cleaned_subjects = subjects.split(",")
    return name, country, city, cleaned_subjects


def create_student():
    name, country, city, subjects = get_student_details()
    db.students.insert_one({
        "name": name,
        "country": country,
        "city": city,
        "class": subjects
    })
    print("Student created.")


def update_input():
    print("**********UPDATE INPUTS**********")
    original_key = str(input("Original key you are updating: "))
    original_value = str(input("Original value you are updaing: "))
    updated_key = str(input("Key of the new value: "))
    update_value = str(input("Value you are updaing to: "))
    query_update = {original_key: original_value}
    new_value = {'$set': {updated_key: update_value}}
    return [query_update, new_value]


def update_student():
    query, new_value = update_input()
    db.students.update_one(query, new_value)