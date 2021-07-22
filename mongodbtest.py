from pymongo import MongoClient
from pprint import pprint

MONGODB_URL = "mongodb+srv://fav-videos-admin:ansonyya0117@cluster0.6fu7m.mongodb.net/fav-videos?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URL)
db = client.admin

serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)