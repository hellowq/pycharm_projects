from  pyquery import PyQuery as pq
import requests
import time
import pymongo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='info'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
page=1
headers={
    'Cookie':'__cfduid=dd377c5feadfc472d0b94a53dc2fc03ac1510966729; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_067eaa6f8a768b30d1f7f49acbf39aad=w822927%7C1511139532%7Cq2TZRWYIqMZKDYM16URBZdjWsLdPO0xzzCsd4wqaxyC%7Ce97cb20e682ad1c043c1a574f5b50beadd6c77bab9d0145b7667a2f18bfe52fe; UM_distinctid=15fcca681c124a-0ac24da8366fdb-5c1b3517-100200-15fcca681c24bc; CNZZDATA1253444560=1499720006-1510958657-http%253A%252F%252Fnanrenfuli.com%252F%7C1510958657',
    'Host':'nanrenfuli.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
url='http://nanrenfuli.com/page/'
stop=0
def get_info(page):
    global stop
    try:
        print('正在请求第%d页'%(page))
        response=requests.get(url+str(page))
        html=response.text
        doc=pq(html)
        items = doc(".main .post_box .c-con .disp_a").items()
        for item in items:
            link = item.attr('href')
            print(link)
            if stop==1:  #如果stop=1,跳出此次的for循环,不再对page进行
                break
            else:
                parse_detail(link)
    except:
        print('请求page %d失败，休息5秒继续请求该页面'%(page))
        time.sleep(5)
        get_info(page)

def parse_detail(url):
    global stop
    try:
        response=requests.get(url,headers=headers,timeout=3)
        if response.status_code==200:
            doc=pq(response.text)
            if doc('#pay-content > p:nth-child(1)').html==None:   #如果某个具体页面不存在网盘的，把stop=1,表示接下来的页面可能也没有网盘了，内容可能是其他类型
                stop=1
                pass
            else:
                info={
                    #'fanhao':doc
                    'wangpan':doc('#pay-content > p:nth-child(1) > a').attr('href'),
                    'tiquma':doc('#pay-content > p:nth-child(1) > input[type="text"]:nth-child(2)').attr('value'),
                    'jieyamima':doc('#pay-content > p:nth-child(1) > input[type="text"]:nth-child(3)').attr('value')
                }
                print(info)
    except:
        print('请求详细页 %s失败，休息5秒继续请求该页面' )
        time.sleep(5)
        parse_detail(url)
def save_to_mongodb(result):
    if table.find_one({'fanhao':result['fanhao']})==None:
        table.insert(result)
        print('存入MongoDB成功')
    else:
        print('已存在不存储')


def main():
    global page
    while True:
        get_info(page)
        page+=1
        if stop==1:
            break

if __name__ == '__main__':
    main()

