# https://github.com/Krefails/csd-310
# Justin Kreifels, 1-30-2022
import pymongo
from pymongo import MongoClient
# Was getting an SSL CERT INVALID error. Fixed it by installing and importing Certifi.
import certifi
from mongoURI import URI

client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())
db = client.pytech
print(f"-- PyTech C0llection List --\n{db.list_collection_names()}\n\n End of program, press any key to exit... ")