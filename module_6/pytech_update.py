# https://github.com/Krefails/csd-310
# Justin Kreifels, 2-8-2022

import pymongo
from pymongo import MongoClient
import certifi
from mongoURI import URI

client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())

db = client.pytech
students = db.students

student_list = students.find({})

thorin = students.find_one({"student_id": "1007"})

#This if statement changes student 1007's last name to either "Oakenshield II" or "Oakenshield" depeding on what name is currently being used!
if (thorin["last_name"].__eq__("Oakenshield")):
    students.update_one({"student_id" : "1007"}, {"$set" : {"last_name": "Oakenshield II"}})
else:
    students.update_one({"student_id" : "1007"}, {"$set" : {"last_name": "Oakenshield"}})

print('\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in student_list:
    print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')

print('\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
print(f'Student ID: {thorin["student_id"]}\nFirst Name: {thorin["first_name"]}\nLast Name: {thorin["last_name"]}')

input('\n\nEnd of program, press any key to continue... ')