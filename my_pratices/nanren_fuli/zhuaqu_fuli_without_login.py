from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from  pyquery import PyQuery as pq
import pymongo
import requests
from zhuaqu_fuli_chrome_config import *
firt_page_url='http://nanrenfuli.com/page/1'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 50)
headers={
    'Cookie':'__cfduid=dd377c5feadfc472d0b94a53dc2fc03ac1510966729; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_067eaa6f8a768b30d1f7f49acbf39aad=w822927%7C1511139532%7Cq2TZRWYIqMZKDYM16URBZdjWsLdPO0xzzCsd4wqaxyC%7Ce97cb20e682ad1c043c1a574f5b50beadd6c77bab9d0145b7667a2f18bfe52fe; UM_distinctid=15fcca681c124a-0ac24da8366fdb-5c1b3517-100200-15fcca681c24bc; CNZZDATA1253444560=1499720006-1510958657-http%253A%252F%252Fnanrenfuli.com%252F%7C1510958657',
    'Host':'nanrenfuli.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}


def firt_page():
    try:
        browser.get(firt_page_url)
        get_link()
    except TimeoutError:
        return firt_page()
    get_link()
def next_page():
    try:
        time.sleep(1)
        xiayiye = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.web_bod > section > div.main > div.page_num > a:nth-child(11)"))
        )
        xiayiye.click()
        get_link()
    except TimeoutError:
        return next_page()
def get_link():
    time.sleep(1)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.web_bod > section > div.main > article:nth-child(4) > div.c-con > a.disp_a"))
        # mainsrp-itemlist class名 items class名 item class名，空格表示 上下级关系
    )
    html = browser.page_source
    #print(html)
    doc = pq(html)
    items = doc(".main .post_box .c-con .disp_a").items()  # items() 返回一个可迭代对象，用于for循环
    for item in items:
        time.sleep(1)
        link = item.attr('href')
        print(link)

'''def search():
    try:
        browser.get("https://www.taobao.com")
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys("美食")
        submit.click()
        total = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        get_products()
        return total[0].text
    except TimeoutError:
        return search()
def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_products()
    except TimeoutError:
        return next_page(page_number)
def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")) #  mainsrp-itemlist class名 items class名 item class名，空格表示 上下级关系
    )
    html=browser.page_source
    doc=pq(html)
    items=doc("#mainsrp-itemlist .items .item").items()   # items() 返回一个可迭代对象，用于for循环
    for item in items:
        product={
            'image':item.find('.pic .pic-link .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        save_to_mongo(product)
def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功',result)
    except Exception:
        print('存储到MONGODB失败',result)
'''
def main():
    firt_page()
    next_page()


if __name__ == '__main__':
    main()

