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
def get_students(query, limit=None, sort='name', reverse=-1):
    filtered_students = db.students.find(query).limit(limit).sort(sort, reverse)
    return filtered_students

def find_student(input_name):
    student = db.students.find_one({
        "name": input_name
    })
    return student