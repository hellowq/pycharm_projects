from urllib import request
from urllib import parse
from urllib import error
import json
from bs4 import BeautifulSoup
import re
def get_page_index(offset,keyword):
    data ={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1
    }
    url='http://www.toutiao.com/search_content/?' + parse.urlencode(data)  #urlencode {'a':'b','c':'d'}转换成 a=b&c=d 格式
    try:
        response = request.urlopen(url)
        if response.status == 200:
            html=response.read()
            return html
        return None
    except error:
        print('请求出错')
        return None
def parse_page_index(html):
    data = json.loads(html)    #json.loads   对使用json编码的字符串转换成python格式，这里是字典格式
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
def get_page_detail(url):
    try:
        response = request.urlopen(url)
        if response.status == 200:
            html=response.read()
            return html
        return None
    except error:
        print('请求出错')
        return None
def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?)',re.S)
    result = re.search(images_pattern,html)
    if result:
        print(result.group(1))

def main():
        html=get_page_index(0,'街拍')
        for url in parse_page_index(html):
            html = get_page_detail(url)


if __name__ == '__main__':
    main()
