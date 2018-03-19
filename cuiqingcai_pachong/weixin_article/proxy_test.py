import requests
proxy_pool_url='http://127.0.0.1:5000/get'
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
def main():
    proxy=get_proxy()
if __name__=='__main__':
    main()