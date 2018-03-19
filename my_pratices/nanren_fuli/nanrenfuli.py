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
    import pymongo
except:
    print('import error')
page_url='http://nanrenfuli.com/page/'
browser=webdriver.Chrome()
#browser=webdriver.PhantomJS()
wait=WebDriverWait(browser, 50)
username='w822927'
password='wq822927'
cookies=[{'domain': '.nanrenfuli.com', 'expiry': 1544007202.53348, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'secure': False, 'value': 'd90d5cddbb63e97892161d0ec43c6a4751512470946'}, {'domain': 'nanrenfuli.com', 'httpOnly': False, 'name': 'wordpress_test_cookie', 'path': '/', 'secure': False, 'value': 'WP+Cookie+check'}, {'domain': 'nanrenfuli.com', 'expiry': 1528196015, 'httpOnly': False, 'name': 'CNZZDATA1253444560', 'path': '/', 'secure': False, 'value': '1400491787-1512465542-http%253A%252F%252Fnanrenfuli.com%252F%7C1512465542'}, {'domain': 'nanrenfuli.com', 'httpOnly': True, 'name': 'wordpress_logged_in_067eaa6f8a768b30d1f7f49acbf39aad', 'path': '/', 'secure': False, 'value': 'w822927%7C1512643749%7CFDW50kh1UMSg9ro6tx4zMoVgshHvFbEdgwnLCtCEpF2%7C735a8c198918a5f19de2f6bd279b3236d3291e2bfad49f6409fee32056977702'}, {'domain': '.nanrenfuli.com', 'expiry': 1528196011, 'httpOnly': False, 'name': 'UM_distinctid', 'path': '/', 'secure': False, 'value': '160264f2ee3879-0e0d65a7e22fe-5c1b3517-100200-160264f2ee424e'}]
MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='nanrenfuli_wangpan'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
stop=1
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
        time.sleep(2)
        submit.click()
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div.web_bod > div.slm_login > div > div.login_in > a.login"))
        )
        print('login success')
        time.sleep(2)
        cookies=browser.get_cookies()
        print(cookies)
        return cookies
    except TimeoutError:
        return login()
def get_index_page(page,cookies):
    try:
        browser.get(page_url+str(page))
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div.web_bod > section > div.main > article"))
            # mainsrp-itemlist class名 items class名 item class名，空格表示 上下级关系  ,下一页存在并且可按
        )
        browser.delete_all_cookies()
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        html=browser.page_source
        #print(browser.get_cookies())
        #file_object = open('nanrenfuli_first', 'w',encoding='utf-8')
        #file_object.write(html)
        #file_object.close()
        return html
    except TimeoutError:
        return first_page()
def parse_index_page(html):#对页码进行parse，返回详细页
    doc=pq(html)
    items = doc(".main .post_box .c-con .disp_a").items()
    for item in items:
        yield {
            'link':item.attr('href'),
            'img_add':'http://nanrenfuli.com'+item.children().attr('src'),
            'describe':item.text()
        }
        #break
def parse_detail_page(detail_page):
    global stop
    try:
        browser.get(detail_page)
        element=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#site-info"))
        )#等页面最下面一个元素加载完毕
    except TimeoutError:
        return parse_detail_page(detail_page)
    html=browser.page_source
    if 'pan.baidu.com'in html:
        stop=1
        doc=pq(html)
        soup = BeautifulSoup(html, 'lxml')

        try:
            try:
                tiquma=soup.select('#pay-content')[0].select('input')[1]['value']
            except:
                tiquma='无'
            info = {
                # 'fanhao':doc
                'wangpan': soup.select('#pay-content')[0].select('a')[0]['href'],
                'tiquma': soup.select('#pay-content')[0].select('input')[0]['value'],
                'jieyamima':tiquma,
                'title': soup.title.text
            }
        except:
            info = {
                # 'fanhao':doc
                'wangpan': soup.select('#vipzhuanshu')[0]['value'],
                #'tiquma': re.findall(r'下载链接: .*? 提取密码: .(*?) 解压密码：', doc('#pay-content').html())[0],
                # 'jieyamima': re.findall(r'value="(.*?)"',doc('#pay-content').html())[1],
                'title': soup.title.text
            }
        #print(info)
        return info
    else:
        print(detail_page+'该页面不存在百度网盘')
        stop=stop+1
def save_to_mongodb(dict):
    if table.find_one({'link':dict['link']})==None:
        table.insert(dict)
        print('存入MongoDB成功')
    else:
        print('已存在不存储')

def main():
    cookies=login_get_cookies()
    for page in range(1,10):#stop inpage77 http://nanrenfuli.com/12768.html
        html=get_index_page(page,cookies)
        detail_page_infos=parse_index_page(html)
        print('当前在page %d页'%page)
        for detail_page_info in detail_page_infos:
            if stop<10:
                try:
                    result=parse_detail_page(detail_page_info['link'])
                    result_dict=dict(detail_page_info,**result)
                    save_to_mongodb(result_dict)
                    print(result_dict,'成功保存到mongodb')
                except:
                    pass
            if stop==10:
                print('当前在page %d页' % page)
                print('连续10个页面不存在网盘，停止')
                break


if __name__=='__main__':
    main()