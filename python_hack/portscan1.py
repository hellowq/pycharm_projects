import argparse
import socket
def port_scan(host_ip,port):#string
    try:
        s = socket.socket()
        s.connect(('127.0.0.1',135))
    except:
        print("host %s port %s is close"%(host_ip,port))
def main():
    parser = argparse.ArgumentParser(description='usage -H <host_ip> -p <port,ports>')
    parser.add_argument('-H', dest='host_ip')
    parser.add_argument('-p', dest='port')
    arg = parser.parse_args()
    host_ip = arg.host_ip
    port = arg.port
    print(host_ip)
    print(port)
    '''if host_ip == None | port == None:
        print('you must specify a host and port[s]')
        exit(0)  # 无错误离开程序'''
    port_scan(host_ip, port)
if __name__=='__main__':
    main()