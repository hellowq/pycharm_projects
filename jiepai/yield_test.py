def count(n): 
  while n > 0: 
    yield n  #生成值：n 
    n -= 1
    return n
c=count(5)
for b in c:
    print(b)
