import requests
from urllib.parse import  urlencode
base_url="http://weixin.sogou.com/weixin?"
keyword='人物'
headers={
    'Cookie':'CXID=61D70AF12CAB5D23097119649B69C2E1; IPLOC=CN3303; SUV=1499307188623037; usid=7CFB83DD2E71980A00000000595D9C2E; SUID=7CFB83DD5C68860A5954AD050004C684; ABTEST=1|1510797396|v1; SNUID=EEF70A7707035808E924B50207AA19B4; JSESSIONID=aaaA-bUstrrWj8pjaLv8v; weixinIndexVisited=1; ppinf=5|1510798007|1512007607|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTclOEUlOEIlRTYlOUQlODN8Y3J0OjEwOjE1MTA3OTgwMDd8cmVmbmljazoxODolRTclOEUlOEIlRTYlOUQlODN8dXNlcmlkOjQ0Om85dDJsdUc0Yk92ZGF0Vm4zel95ZFFsVkhpNWdAd2VpeGluLnNvaHUuY29tfA; pprdig=V84oE5P_-BZADjJ4Huo1-_2558GeCiaoOR5GrSE7BBcLFpi4em6ixW12LYdQNWF_7tHzXW23E5KRRjok_RXuMdAKetKPD8-8LCMZS1oEQ3SsnFSxhjFVqYaelYquVA_z_LdSNgbX8RayDw1Kr4jncG3jnJWIPyFHH3Vp5ISryy0; sgid=07-29875963-AVoM8rcLjglOgda95wSPbJo; ppmdig=1510802340000000a157135ac779627c6e31dfe6d16df8a2; sct=4',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36HH=12Runtime=fobkjmjepodfhggkgoeackdaihhmeliaALICDN/ DOL/HELLO_GWF_'
}
proxy_pool_url="http://127.0.0.1:5000/get"
proxy=None
max_count=5
'''def get_proxy():            #返回代理地址，格式为str  '*.*.*.*:8'
    try:
        response=requests.get(proxy_pool_url,timeout=20)
        if response.status_code==200:
            print('response.text is')
            print(response.text)
            return response.text
        return get_proxy()
    except ConnectionError:
        return get_proxy()'''
def get_proxy():            #返回代理地址，格式为str  '*.*.*.*:8'
    try:
        response=requests.get(proxy_pool_url,timeout=5)
        if response.status_code==200:
            if response.text:
                print('response.text is ',response.text)
                return response.text
            else:
                return get_proxy()
        else:
            return get_proxy()
    except :
        return get_proxy()

def get_html(url):            #
    print('cawlinging ',url)
    #print('tring count',count)
    global proxy
    #if count >=max_count:
     #   print('tried too many time')
      #  return None
    try:
        if proxy:
            proxies={
                'http':'http://'+proxy
            }
            print(proxies)
            response=requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code==200:
            return response.text
        if response.status_code==302:
            #Need Proxy or change a proxy
            print('302')
            proxy=get_proxy()
            if proxy:
                print('use proxy',proxy)
                return get_html(url)
            else:
                print('get proxy failed')
                return get_html(url)

    except ConnectionError as e:
        print('error occurred',e.args)
        proxy=get_proxy()
        return get_html(url)

def get_index(keyword,page):   #根据keyword，page，进行搜索，得到html
    data={
        'query':keyword,
        'type':2,
        'page':page
    }
    queries=urlencode(data)
    url=base_url+queries
    html=get_html(url)
    return html
def main():
    for page in range(1,101):
        html=get_index(keyword,page)
        print(html[0:100])
if __name__=='__main__':
    main()
