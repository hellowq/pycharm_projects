import socket,time
s=socket.socket()
s.connect(('127.0.0.1',442))
while True:
    data=input('client:')
    s.send(data.encode())
    data=s.recv(1024)
    print('server:%s'%(data.decode()))
s.close()


