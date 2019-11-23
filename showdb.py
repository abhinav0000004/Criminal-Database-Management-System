import pymongo

myclient = pymongo.MongoClient()
# "mongodb://localhost:27017/"

mydb = myclient["mydatabase"]

mycol = mydb["criminal"]
"""
myquery = { "NAME": "bdbb" }

mycol.delete_one(myquery)
"""

for x in mycol.find():
  print(x)
