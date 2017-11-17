from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from  pyquery import PyQuery as pq
import pymongo
import requests
from zhuaqu_fuli_chrome_config import *
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 50)

'''def get_cookies():
    data = {'log': 'w822927', 'pwd': 'wq822927', 'wp-submit': '登录',
            'redirect_to': 'http://nanrenfuli.com/wp-admin/',
            'testcookie': '1'}
    try:
        r = requests.post('http://nanrenfuli.com/wp-login.php', data=data)
        if r.status_code == 200:
            return r.cookies
    except RequestException:
        print('get cookies error')
        return get_cookies()
'''
def login():
    try:
        browser.get("http://nanrenfuli.com/wp-login.php")
        input_username=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user_login"))
        )
        input_password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user_pass"))
        )

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#wp-submit"))
        )
        input_username.send_keys("w822927")
        input_password.send_keys("wq822927")
        submit.click()
        link_shouye= wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#menu-item-3199 > a"))
        )
        link_shouye.click()
        get_link()
    except TimeoutError:
        return login()
def next_page():
    try:
        xiayiye = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.web_bod > section > div.main > div.page_num > a:nth-child(11)"))
        )
        xiayiye.click()
        get_link()
    except TimeoutError:
        return next_page()
def get_link():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.web_bod > section > div.main > article:nth-child(4) > div.c-con > a.disp_a"))
        # mainsrp-itemlist class名 items class名 item class名，空格表示 上下级关系
    )
    html = browser.page_source
    print(html)
    doc = pq(html)
    items = doc("#main .post_box .c-con").items()  # items() 返回一个可迭代对象，用于for循环
    print(items)
    for item in items:
        print(item)
        '''product = {
            'image': item.find('.pic .pic-link .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }'''
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
    login()
    '''total=search()
    total=int(re.search('(\d+)',total).group(1))
    print(total)
    for i in range(2,total+1):
        print(i)
        next_page(i)
    browser.close()'''
if __name__ == '__main__':
    main()

