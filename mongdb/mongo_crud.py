from pymongo import MongoClient

client = MongoClient("mongodb://192.168.206.130:27017")
print(client)
database = client["test"]
collection = database["user"]
# collection.insert_many([{"name": "daxiong", "age": 30, "address": "宁夏"},
#                        {"name": "pizai", "age": "1", "address": "四川"},
#                        {"name": "huge", "age": "35", "address": "hubei"}])

# collection.insert_one({"name": "xiaoliu", "age": 25, "address:": "吉林"})

collection.update_one({"name": "huge"},
                      {"$set": {"age": 35, "address": "湖北"}})

rows = collection.find({"age": {"$lt": 40, "$gt": 20}})
for row in rows:
    print(row)
