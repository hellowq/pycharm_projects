import requests
import time
import  re
import json
from urllib.parse import urlencode   # 用于传递参数
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def get_page_index(offset,keyword):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':20,
        'cur_tab':3
    }
    url='https://www.toutiao.com/search_content/?' + urlencode(data) #https://www.toutiao.com/search_content/?offset=0&format=json&keyword=街拍&autoload=true&count=20&cur_tab=1
    try:
        res=requests.get(url,timeout=5)
        if res.status_code==200:
            return res.text
        return None
    except RequestException:
        print("请求索引页失败\n")
        return None
def parse_page_index(html):
    if html:
        data=json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):    #data.get('data')是一个字典的列表，item 是字典
                yield item.get('article_url')  #返回一个可迭代的url
    else:
        print('传入的html参数非法')
def get_page_detail(url):
    try:
        res=requests.get(url)
        if res.status_code==200:
            time.sleep(2)
            return res.text

        return None
    except RequestException:
        print("请求页面失败\n")
        time.sleep(2)
        return None

def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    image_pattern=re.compile('gallery: (.*?)siblingList:',re.S)
    result=re.search(image_pattern,html)
    if result:
        data=json.loads(result.group(1)[0:-6])    #result.group(1)不是json格式，后面有其他字符，[0：-6]去掉其他，符合json格式，json格式的字符串转化为字典
        if data and 'sub_images' in data.keys() :
            sub_images=data.get('sub_images')  #sub_images是字典的列表
            images=[item.get('url') for item in sub_images]  #item是字典，images是url字符串的列表
            return{
                'title':title,
                'url':url,
                'image':images
            }

def main():
    html=get_page_index(0,'街拍')
    i=1
    for url in parse_page_index(html):
        html=get_page_detail(url)
        if html:
            result=parse_page_detail(html,url)
            print('第%d个 '%(i))
            i=i+1
            print(result)

if __name__ == '__main__':
    main()

