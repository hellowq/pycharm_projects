import os
import re
import bs4
from collections import Counter

def shengsanfang_tousu(path): # 省三方投诉
    os.chdir(r"C:\Users\Administrator")   #切换到桌面目录
    file=open(path,encoding="utf-8")
    content=file.read()
    result = re.findall('<td>省第三方链路</td><td>?([\u4e00-\u9fa5]*)</td>', content, re.S)
    print('省三方投诉',result)
    file.close()


def sidazhuanxiang(path):  #
    os.chdir(r"C:\Users\Administrator")  # 切换到桌面目录
    file = open(path, encoding="utf-8")
    content = file.read()
    result1 = re.findall('<td>网页类</td>', content, re.S)
    result2 = re.findall('<td>游戏类</td>', content, re.S)
    result3 = re.findall('<td>企业专线</td>', content, re.S)
    print('四大专项网页类数量：%d'%(len(result1))+'\n')
    print('四大专项游戏数量：%d'%(len(result2)) + '\n')
    print('四大专项政企类数量：%d'%(len(result3)) + '\n')
    file.close()

def jiaketousu(path):    #获得家客 游戏网页等各项投诉的数量
    os.chdir(r"C:\Users\Administrator")  # 切换到桌面目录
    file = open(path, encoding="utf-8")
    content=file.read()
    soup = bs4.BeautifulSoup(content,"lxml")
    all_list = soup.select('tr[style="vnd.ms-excel.numberformat: @;"]')  #获得所有工单，包括家客和政企业
    tongji_list=[]
    for item in all_list:
        if item.find_all('td')[2]==bs4.BeautifulSoup('<td>个人用户</td>',"lxml").td:  #all_list[1].find_all('td')[2].contents[0]=
            tongji_list.append(item.find_all('td')[14])
    count=Counter(tongji_list)
    print('家客投诉',count)
    print("家客工单数量：%d"%(len(tongji_list)))

def jiake_wangye(path):
    os.chdir(r"C:\Users\Administrator")  # 切换到桌面目录
    file = open(path, encoding="utf-8")
    content = file.read()
    soup = bs4.BeautifulSoup(content, "lxml")
    all_list = soup.select('tr[style="vnd.ms-excel.numberformat: @;"]')
    wangye_list=[]
    for item in all_list:
        if item.find_all('td')[2]==bs4.BeautifulSoup('<td>个人用户</td>',"lxml").td and item.find_all('td')[14]==bs4.BeautifulSoup('<td>网页类</td>',"lxml").td:
            wangye_list.append(item.find_all('td')[23])
    count=Counter(wangye_list)
    print('家客网页',count)

def jiake_youxi(path):
    os.chdir(r"C:\Users\Administrator")  # 切换到桌面目录
    file = open(path, encoding="utf-8")
    content = file.read()
    soup = bs4.BeautifulSoup(content, "lxml")
    all_list = soup.select('tr[style="vnd.ms-excel.numberformat: @;"]')
    youxi_leixing_list=[]
    youxi_tousu_yuanyin_list=[]
    for item in all_list:
        if item.find_all('td')[2]==bs4.BeautifulSoup('<td>个人用户</td>',"lxml").td and item.find_all('td')[14]==bs4.BeautifulSoup('<td>游戏类</td>',"lxml").td:
            youxi_tousu_yuanyin_list.append(item.find_all('td')[23])
            youxi_leixing_list.append(item.find_all('td')[15])
    count1=Counter(youxi_leixing_list)
    count2 = Counter(youxi_tousu_yuanyin_list)
    print('家客游戏类型',count1)
    print('家客游戏投诉原因',count2)

def zhengqi_tousu(path):
    os.chdir(r"C:\Users\Administrator")  # 切换到桌面目录
    file = open(path, encoding="utf-8")
    content = file.read()
    soup = bs4.BeautifulSoup(content, "lxml")
    all_list = soup.select('tr[style="vnd.ms-excel.numberformat: @;"]')
    zhengqi_leixing_list=[]
    zhengqi_yuanyin_list=[]
    for item in all_list:
        if item.find_all('td')[2]!=bs4.BeautifulSoup('<td>个人用户</td>',"lxml").td:
            zhengqi_leixing_list.append(item.find_all('td')[14])
            zhengqi_yuanyin_list.append(item.find_all('td')[23])
    count1=Counter(zhengqi_leixing_list)
    count2=Counter(zhengqi_yuanyin_list)
    print('政企投诉类型',count1)
    print('政企投诉原因',count2)
shengsanfang_tousu('31.txt')
sidazhuanxiang('31.txt')
jiaketousu('31.txt')
jiake_wangye('31.txt')
jiake_youxi('31.txt')
zhengqi_tousu('31.txt')