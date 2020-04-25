import pymongo 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] #name of database
#To create a database in MongoDB, start by creating a MongoClient object
#then specify a connection URL with the correct ip address 
#and the name of the database you want to create
print(myclient.list_database_names())

#outputs are the list of system database
#['admin', 'config', 'local']
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
#no database are shown, because database does not have a content


#creating collection ~ table in SQL
mycol = mydb["customers"]
#Important: In MongoDB, a collection is not created until it gets content!

print(mydb.list_collection_names())
#Return a list of all collections in your database

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.") 
#specific check for particular collection (there is no yet )

#A document in MongoDB is the same as a record in SQL databases