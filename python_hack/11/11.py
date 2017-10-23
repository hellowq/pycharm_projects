import requests,time
#http://204.12.243.210/SIRO-2726/M3U8/playlist1503.ts
# 通过requests库下载文件
for i in range(1,1800):
    url = 'http://204.12.243.210/SIRO-2726/M3U8/playlist'+str(i)+'.ts'
    r = requests.get(url)
    with open('playlist'+str(i)+'.ts', "wb") as code:
        code.write(r.content)
    print(i)

