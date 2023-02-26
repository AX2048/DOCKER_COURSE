"""docstring"""
from pprint import pprint
from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("ListDatabases")
pprint(dbs_list)
