from ast import Constant
import pymongo
from pymongo import MongoClient
import certifi

URI = "mongodb+srv://admin:admin@cluster0.1qv4w.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())
db = client.pytech
print(f"-- PyTech C0llection List --\n{db.list_collection_names()}\n\n End of program, press any key to exit... ")