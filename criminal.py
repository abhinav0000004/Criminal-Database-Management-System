import pymongo

myclient = pymongo.MongoClient()
# "mongodb://localhost:27017/"

mydb = myclient["mydatabase"]

mycol = mydb["criminal"]

#print(mydb.list_collection_names())

def insert_rec(dict):
    x = mycol.insert_one(dict)

def ret_dict(nam):
    myquery = { "NAME":nam}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        md=x
    return md

"""
for x in mycol.find():
  print(x)    
   
mycol.drop()

x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
"""
