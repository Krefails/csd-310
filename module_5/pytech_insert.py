# https://github.com/Krefails/csd-310
# Justin Kreifels, 1-31-2022

import pymongo
from pymongo import MongoClient
# Was getting an SSL CERT INVALID error. Fixed it by installing and importing Certifi.
import certifi

URI = "mongodb+srv://admin:admin@cluster0.1qv4w.mongodb.net/pytech?retryWrites=true&w=majority"

client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())

db = client.pytech

# Start of Thorin Data Document
thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "4.0",
            "start_date": "October 19, 2021",
            "end_date": "December 12, 2021",
            "courses": [
                {
                    "course_id": "CSD123",
                    "description": "Database",
                    "instructor": "Professor Cool",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD124",
                    "description": "Java",
                    "instructor": "Professor Cool",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Start of Bilbo Data Document
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.8",
            "start_date": "October 19, 2021",
            "end_date": "December 12, 2021",
            "courses": [
                {
                    "course_id": "CSD123",
                    "description": "Database",
                    "instructor": "Professor Cool",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD124",
                    "description": "Java",
                    "instructor": "Professor Cool",
                    "grade": "B+"
                }
            ]
        }
    ]
}

# Start of Frodo Data Document
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.6",
            "start_date": "October 19, 2021",
            "end_date": "December 12, 2021",
            "courses": [
                {
                    "course_id": "CSD123",
                    "description": "Database",
                    "instructor": "Professor Cool",
                    "grade": "B"
                },
                {
                    "course_id": "CSD124",
                    "description": "Java",
                    "instructor": "Professor Cool",
                    "grade": "B"
                }
            ]
        }
    ]
}

# Gets the students collection for the pytech database
students = db.students

print("\n -- INSERT STATEMENTS --")
thorin_student_id = students.insert_one(thorin).inserted_id
print(f"  Inserted student record Thorin Oakenshield into students collection with document_id {str(thorin_student_id)}")

bilbo_student_id = students.insert_one(bilbo).inserted_id
print(f"  Inserted student record Bilbo Oakenshield into students collection with document_id {str(bilbo_student_id)}")

frodo_student_id = students.insert_one(frodo).inserted_id
print(f"  Inserted student record Frod Oakenshield into students collection with document_id {str(frodo_student_id)}")

input('\n\n  End of program, press any key to exit... ')