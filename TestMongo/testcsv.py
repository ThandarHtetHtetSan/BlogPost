import pymongo
connection=pymongo.MongoClient("localhost",27017)
database=connection["user_data"]
collection=database["business_info"]
query={"Series reference ": 2019.12}
new={"$set":{"Series reference ": 2020.20}}
try:
    collection.update_one(query , new)
    for i in collection.find():
        print(i)

    print('success')
except Exception as err:
    print(err)


