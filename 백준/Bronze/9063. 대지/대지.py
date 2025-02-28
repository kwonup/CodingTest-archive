n = int(input())
xlist=[]
ylist=[]
for i in range(n):
    x,y=map(int,input().split())
    xlist.append(x)
    ylist.append(y)
if n<=1: print(0)
else: print((max(xlist)-min(xlist)) * (max(ylist)-min(ylist)))