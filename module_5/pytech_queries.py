# https://github.com/Krefails/csd-310
# Justin Kreifels, 1-31-2022

import pymongo
from pymongo import MongoClient
# Was getting an SSL CERT INVALID error. Fixed it by installing and importing Certifi.
import certifi

URI = "mongodb+srv://admin:admin@cluster0.1qv4w.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())

db = client.pytech
students = db.students

student_list = students.find({})

print('\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in student_list:
    print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')

bilbo = students.find_one({"student_id": "1008"})

print('\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
print(f'Student ID: {bilbo["student_id"]}\nFirst Name: {bilbo["first_name"]}\nLast Name: {bilbo["last_name"]}')

input('\n\nEnd of program, press any key to continue... ')