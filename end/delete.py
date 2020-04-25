#The first parameter of the delete_one() method is a query object defining which document to delete
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)
#Delete all documents were the address starts with the letter S
myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")
#To delete all documents in a collection, pass an empty query object to the delete_many() method
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")