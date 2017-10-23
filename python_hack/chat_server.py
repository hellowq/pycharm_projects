import socket
s=socket.socket()
s.bind(('127.0.0.1',442))
print('正在等待连接')
s.listen(5)

sock,addr=s.accept()
print("conect from %s:%s"%addr)
while True:
    data=sock.recv(1024)
    print('client:%s'%(data.decode()))
    data=input('server:')
    sock.send(data.encode())
s.close()