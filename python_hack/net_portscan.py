import IPy,time

import argparse
import threading

from socket import *
def connect_scan(host_ip,port):   # host port 均为str
    try:
        connect_socket=socket()
        connect_socket.connect((host_ip,int(port)))
        #connect_socket.send(b'hello')    #不注释掉，会卡住
        #result=connect_socket.recv(1024)

        lock.acquire()
        print('host %s port %s is open' % (host_ip, port))
        openlist.append(host_ip+'\t'+port)
        #print('result:%s'%result)
        #return {
         #   "ip":host_ip,
          #  "open_port":port
        #}

    except:
        lock.acquire()
        print('host %s port %s is close'%(host_ip,port))
    finally:
        lock.release()
        connect_socket.close()


def port_scan(host_ip,ports):     #ports 是一个str 或者由str组成的list
    '''try:
        host_ip=gethostbyname(hostname)
    except:
        print("hostname %s cann't resolve"%hostname)
        return'''
    setdefaulttimeout(2)
    for port in ports:
        #print('scan port %s'%port)
        t=threading.Thread(target=connect_scan,args=(host_ip,port))
        t.start() #启动线程
        t.join()  #如果不加join语句，那么主线程不会等到当前线程结束才结束。加了后，等子线程结束，主线程才结束。
def get_ip_fromfile(filename):     #filename str格式
    f=open(filename,'r')
    for line in f.readlines():
        for ip in  IPy.IP(line.split('\t')[2]):
            yield str(ip)             #ip返回的是 IPy.ip类型，一定要加str转
    f.close()
def save_openlist(filename,openlist):    #filename str,ipen_list list[str,str]
    with open(filename,'a',encoding='utf-8') as f:
        for ip_port in openlist:
            f.write(ip_port+'\n')
        f.close()
def main():
    #parser = argparse.ArgumentParser(description='usage -H <host_ip> -p <port,ports>')
    #parser.add_argument('-H',dest='host_ip')
    #parser.add_argument('-p',dest='ports')
    #arg = parser.parse_args()
    filename='wuganda.txt'
    ports=['21']

    #host_ip=arg.host_ip
    #ports=arg.ports.split(',')
    #if host_ip==None or ports==None:
     #   print('you must specify a host and port[s]')
      #  exit(0)  #无错误离开程序
    for ip in get_ip_fromfile(filename):
        port_scan(ip,ports)
    save_openlist('wuganda_ftp21_result.txt',openlist)

if __name__=='__main__':
    lock = threading.Lock()
    openlist = []
    main()
    #time.sleep(2)
    print(openlist)