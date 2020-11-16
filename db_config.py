import os
from flask_pymongo import pymongo

'''
DB_USER = "admin"
DB_PASSWORD = "admin123456789"
DB_HOST = "db-test.z3hzr.mongodb.net"
DB_NAME = "api_teclados"
'''
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(f"mongodb+srv://admin:{DB_PASSWORD}@db-test.z3hzr.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
db = client.test



