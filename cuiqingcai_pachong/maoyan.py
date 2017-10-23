import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    try:
        res=requests.get(url)
        if res.status_code==200:
            return res.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?<i.*?board-index-.*?>(\d+)</i>.*?title="(.*?)".*?data-src="(.*?)".*?</a>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{                      #yiele 返回可迭代的对象，可以理解return返回一个可迭代对象，当前迭代一次返回的是一个字典
            'paiming':item[0],
            'pianming':item[1],
            'tupian':item[2],
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html= get_one_page(url)
    for item in parse_one_page(html):#由于之前的yield parse_one_page返回时一个可迭代对象
        print(item)
        write_to_file(item)


if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])

