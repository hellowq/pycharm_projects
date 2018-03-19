import pymongo
MONGO_URL='localhost'
MONGO_DB='taobao_meishi'
MONGO_TABLE='product'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
table.find({'deal':'508'})
print(type())
