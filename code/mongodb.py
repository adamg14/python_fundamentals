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