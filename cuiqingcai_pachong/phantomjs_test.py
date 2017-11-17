from selenium import webdriver
from taobaomeishi_phantomjs_config import *

driver = webdriver.PhantomJS(service_args=['--disk-cache=true'])
driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
data = driver.find_element_by_id("jd_comments").text
print(data)
driver.quit()