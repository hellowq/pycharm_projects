# -*- coding: utf-8 -*-
import pymongo
import requests
import time
import os
import json
os.chdir(r"C:\Users\Administrator\Desktop\save")

MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='nanrenfuli_wangpan'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
def traverse_mongodb():
    for doc in table.find({}):
        #print(type(doc))
        #print(doc)
        print(doc)
        yield doc

def save_to_file(doc):
    filename ='20171220savedoc111'
    del doc['_id']  #_id项的值被json的dumps执行出现错误不匹配格式
    js_doc = repr(doc)
    #byte_doc=bytes(js_doc,encoding='utf-8')
    if os.path.exists(filename)==False:   #文件不存在的话创建
        try:
            with open(filename, 'wt',encoding='utf8') as f:
                print(js_doc)
                f.write(js_doc)
                f.write('\n')

        except:
            print('新建错误')

    else:
        print(filename,'文件正在添加数据')
        with open(filename, '+a',encoding='utf8') as f:
            f.write(js_doc)
            f.write('\n')

def main():
    docs=traverse_mongodb()
    for doc in docs:
        save_to_file(doc)

if __name__=='__main__':
    main()