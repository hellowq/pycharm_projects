import pexpect
prompt=['# ','>>> ','> ','\$ ']    #输入命令后 判断正确expect返回的值
def send_comand(child,cmd):
    child.sendline(cmd)
    child.expect(prompt)
    print(child.before)  # 之前输入的命令

def connect(user,host,password):
    ssh_newkey='Are you sure you want to continue connecting'
    constr='ssh '+user+'@'+host
    child=pexpect.spawn(constr)
    expect_result=child.expect([pexpect.EOF,pexpect.TIMEOUT,ssh_newkey,'.*[P|p]assword.*'])
    if expect_result==0:
        print('连接错误')
        return
    if expect_result==1:
        print('连接超时错误')
        return
    if expect_result==2:
        child.sendline('yes')
        expect_result=child.expect([pexpect.EOF,pexpect.TIMEOUT,'.*[P|p]assword.*''])
            if expect_result == 0:
                print('发送yes连接错误')
                return
            elif expect_result == 1:
                print('发送连接超时错误')
                return
    child.sendline(password)
    child.expect(prompt)
    return child
    def main():
        host='127.0.0.1'
        user='root'
        password='pwd_123'
        child=connect(user,host,password)
        send_comand(child,'cat /etc/shadow | grep root')
        print(child.before.decode('utf-8'))    #输出cat结果
    if __name__=='__main__':
        main()


