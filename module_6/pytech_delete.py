# https://github.com/Krefails/csd-310
# Justin Kreifels, 2-8-2022

from asyncio.windows_events import NULL
import pymongo
from pymongo import MongoClient
import certifi
from mongoURI import URI

client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())

db = client.pytech
students = db.students

student_list = students.find({})

print('\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in student_list:
    print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')

testStudent = {
    "student_id" : "1010",
    "first_name" : "John",
    "last_name" : "Doe"
}

testStudentId = NULL

#This stops the script from inserting a new test student if there one already exists
if(doc["student_id"] != ("1010")):
    testStudentId = students.insert_one(testStudent).inserted_id

#insert statements
print('-- INSERT STATEMENTS --')
print(f'Inserted student record into students collection with document_id ${str(testStudentId)}\n')

#Finds and displays student with id "1010"
student_test_doc = students.find_one({"student_id": "1010"})

print('-- DISPLAYING STUDENT TEST DOC --')
print(f'Student ID: {student_test_doc["student_id"]}\nFirst Name: {student_test_doc["first_name"]}\nLast Name: {student_test_doc["last_name"]}\n')

#deletes student with id of "1010"
students.delete_one({"student_id" : "1010"})

new_student_list = students.find({})

print('\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in new_student_list:
    print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')

input('\nEnd of program, press any key to continue... ')