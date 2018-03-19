import pymongo
import requests
import time
import os
headers={
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
headers1={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'__cfduid=dca5f40a9a6ade6b404d9ccb1b8bed58f1509782486; UM_distinctid=1605847908ff7-0873fe7edf8f82-6b1b1279-100200-160584790904e4; CNZZDATA1253444560=907055103-1513302692-%7C1513302692',
    'Host':'nanrenfuli.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
os.chdir(r"C:\Users\Administrator\Desktop\save")
print(os.path)
MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='nanrenfuli_wangpan'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
def traverse_mongodb():
    for  doc in table.find({}):
        yield {
            'img_add':doc['img_add'],
            'title':doc['title']
        }
def down_load_img(info):
    filename = info['title'].replace(r'/', '').replace(r'\\', '').replace(r'|', '').replace(r'*', '').replace(r':','').replace( r'?', '').replace(r'?', '')
    if os.path.exists(filename+r'.jpg')==False:
        try:
            print(info['img_add'])
            r=requests.get(info['img_add'],headers=headers1,timeout=5)
            print(r.status_code)
        except requests.ConnectionError as e:
            print('requests 失败',info['img_add'],e)
            time.sleep(0.5)
            return
        time.sleep(0.3)

        f=open(filename+r'.jpg', 'wb')
        f.write(r.content)
        f.close()
        print(info['img_add'],'已保存')
    else:
        print('文件已经存在，无需')

def main():
    infos=traverse_mongodb()
    for info in infos:
        print(info)
        down_load_img(info)
if __name__=='__main__':
    main()