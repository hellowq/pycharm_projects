import pymongo
import requests
import time
import os
import json
os.chdir(r"C:\Users\Administrator\Desktop\save")
print(os.curdir)
MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='nanrenfuli_wangpan'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
def traverse_mongodb():
    for doc in table.find({}):
        print(type(doc))
        print(doc)
        yield doc
def save_to_file(doc):
    filename ='20171220savedoc'
    if os.path.exists(filename)==False:   #文件不存在的话创建
        try:
            f = open(filename, 'w')
            js_doc= json.dumps(doc)
            f.write(js_doc)
            f.write(str + '\n')
            f.close()
            print(doc['title'], '已保存')
        except:
            print('新建错误')


    else:
        print('文件已经存在，添加数据')
        f = open(filename, 'a+')
        js_doc = json.dumps(doc)
        f.write(js_doc)
        f.write(str + '\n')
        f.close()
        print(doc['title'], '已保存')
def main():
    docs=traverse_mongodb()
    '''for doc in docs:
        save_to_file(doc)'''
if __name__=='__main__':
    main()