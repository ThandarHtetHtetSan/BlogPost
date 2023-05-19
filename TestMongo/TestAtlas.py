import pymongo
uri="mongodb+srv://thandarhtethtetsan23:Moeebill2388@cluster0.3s0ipxi.mongodb.net/?retryWrites=true&w=majority"
connection=pymongo.MongoClient(uri)
database=connection["myDB"]
collection=database["myCollection"]
data={"name":"htet","age":23,"gender":"female"}
collection.insert_one(data)