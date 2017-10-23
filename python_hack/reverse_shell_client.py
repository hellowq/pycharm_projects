import socket,time
s=socket.socket()
s.connect(('127.0.0.1',442))
while True:
    data=input('输入命令:')
    s.send(data.encode())
    stdoutput=s.recv(1024)
    print('命令执行结果:%s'%(stdoutput.decode('gb2312')))
s.close()
