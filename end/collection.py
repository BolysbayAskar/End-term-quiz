import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

#creating collection ~ table in SQL
mycol = mydb["customers"]
#Important: In MongoDB, a collection is not created until it gets content!

print(mydb.list_collection_names())
#Return a list of all collections in your database

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.") 
#specific check for particular collection (there is no yet )