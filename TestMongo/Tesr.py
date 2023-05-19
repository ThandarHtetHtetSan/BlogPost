import pymongo
connection=pymongo.MongoClient("localhost",27017)
database=connection["user_data"]
collection=database["T_data"]
# user=[
# {"_id":1,'name':'htethtet','age':23,'gender':'female'},
# {"_id":2,'name':'winwin','age':24,'gender':'female'},
# {"_id":3,'name':'thwe','age':25,'gender':'female'},
# {"_id":4,'name':'yamone','age':26,'gender':'female'},
# {"_id":5,'name':'mgmg','age':26,'female':'male'} ]
# collection.insert_many(user)
# user1={"_id":6,"name":'agag',"age":25, "gender":"male"}
# collection.insert_one(user1)
# user2={"_id":7,"name":'zawzaw',"age":27, "gender":"male"}
# collection.insert_one(user2)
# query = {"name": {"$regex":"h"} }
# data=collection.find(query)
# for i in data:
#     print(i)
# data=collection.find().sort("name")
# for i in data:
#     print("Ascending order is ",i)
# data=collection.find().sort("name",-1)
# for i in data:
#     print("Descending order is ",i)
# collection.delete_many({})
# pretty() method

# for i in range(1,6):
#     user={"_id": i ,"name":"myamya","age":15,"gender":"female"}
#     collection.insert_one(user)
# collection.delete_many({})


# data=collection.find()
# for i in data:
# #     print("Check",i)
# collection.drop()
# print("Collection {} is dropped".format(collection))


# find one and delete
# query={'name':'winwin'}
# # collection.find_one_and_delete(query)
#
# size=query.totalIndexSize()
# print(size)
print(database.collection_names())

