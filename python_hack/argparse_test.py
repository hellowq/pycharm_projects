import argparse

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-H',action='store',dest='host')  #如果存在dest， 保存在arg.dest中，不会保存在arg.a中
parser.add_argument('-p',action='store',dest='ports')
arg=parser.parse_args()
print(arg.host)
#print(arg.a)
print(arg.ports)
