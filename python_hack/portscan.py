import argparse
import threading
lock=threading.Lock()
from socket import *
def connect_scan(host_ip,port):
    try:
        connect_socket=socket()
        connect_socket.connect((host_ip,int(port)))
        #connect_socket.send(b'hello')    #不注释掉，会卡住
        #result=connect_socket.recv(1024)

        lock.acquire()
        print('host %s port %s is open'%(host_ip,port))
        #print('result:%s'%result)
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
        print('scan port %s'%port)
        t=threading.Thread(target=connect_scan,args=(host_ip,port))
        t.start()
def main():
    parser = argparse.ArgumentParser(description='usage -H <host_ip> -p <port,ports>')
    parser.add_argument('-H',dest='host_ip')
    parser.add_argument('-p',dest='ports')
    arg = parser.parse_args()
    host_ip=arg.host_ip
    ports=arg.ports.split(',')
    if host_ip==None or ports==None:
        print('you must specify a host and port[s]')
        exit(0)  #无错误离开程序
    port_scan(host_ip,ports)
if __name__=='__main__':
    main()



