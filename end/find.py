#To select data from a collection in MongoDB, we can use the find_one() method
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()
print(x)
#The find() method returns all occurrences in the selection
for x in mycol.find():
    print(x)
#Return Only Some Fields
#Return only the names and addresses, not the _ids
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)
#You are not allowed to specify both 0 and 1 values in the same object 


#This example will exclude "address" from the result
for x in mycol.find({},{ "address": 0 }):
    print(x)

#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in mycol.find({},{ "name": 1, "address": 0 }):
    print(x)