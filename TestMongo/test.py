import pymongo
connection=pymongo.MongoClient("localhost",27017)
database=connection["user_data"]
collection=database["test_data"]
user=[
 {"_id":1,'name':'htethtet','age':23,'gender':'female'},
{"_id":2,'name':'winwin','age':23,'gender':'female'},
{"_id":3,'name':'thwe','age':23,'gender':'female'},
{"_id":4,'name':'yamone','age':23,'gender':'female'},
{"_id":5,'name':'mgmg','age':26,'female':'male'} ]
collection.insert_many(user)
id=collection.find().distinct('_id')
print(id)
for i in collection.find():
    print("Data is:",i)
for i in collection.find({},{"name":0}):
    print("Data without name  ",i)
for i in collection.find({},{"age":1}):
    print("Data with id and age",i)
for i in collection.find({},{"_id":0,"age":1}):
    print("Data age with no id",i)
query={"_id":{"$gt":3}}
da=collection.find(query)
for i in da:
    print("Data id greater than 3 ",i)
query1={"age":{"$lt":26}}
data=collection.find(query1)
for i in data:
    print("Age ",i)
qu={"name":{'$regex':'h'}}
data1=collection.find(qu)
for i in qu:
    print("name with h ",i)
s=collection.find().sort("name")
for i in s:
    print("Ascending Sorted ", i)
s1=collection.find().sort("name",-1)
for i in s1:
    print("Descending order ",i)
