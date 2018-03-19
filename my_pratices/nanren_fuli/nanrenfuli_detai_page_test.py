try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import re
    from pyquery import PyQuery as pq
    import pymongo
    import requests
    from bs4 import BeautifulSoup
except:

    print('import error')
#browser=webdriver.Chrome()
#wait=WebDriverWait(browser, 50)
detail_url='http://nanrenfuli.com/17489.html'
username='w822927'
password='wq822927'
def login_get_cookies():
    try:
        browser.get('http://nanrenfuli.com/wp-login.php')
    except:
        browser.get('http://nanrenfuli.com/wp-login.php')
    time.sleep(2)
    try:
        username_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user_login"))
        )
        password_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user_pass"))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#wp-submit"))
        )
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit.click()
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div.web_bod > div.slm_login > div > div.login_in > a.login"))
        )
        print('login success')
        time.sleep(2)
        cookies=browser.get_cookies()
        return cookies
    except TimeoutError:
        return login_get_cookies()

def get_detail_page_html(detail_url):
    browser.get(detail_url)
    html=browser.page_source
    return html

def main():
    #login_get_cookies()
    #html=get_detail_page_html(detail_url)
    file_object = open('detail_page', encoding='utf-8')
    try:
        detail_html = file_object.read()
    finally:
        file_object.close()
    soup=BeautifulSoup(detail_html,'lxml')
    print(soup.select('#vipzhuanshu')[0])

if __name__=='__main__':
    main()