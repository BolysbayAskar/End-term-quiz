#Use the sort() method to sort the result in ascending or descending order.
#Sort the result alphabetically by name
import pymongo 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

#sort("name", 1) #ascending
#sort("name", -1) #descending
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)