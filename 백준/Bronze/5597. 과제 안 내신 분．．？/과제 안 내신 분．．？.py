a=[]
num=list(range(1,31))
for i in range(28):
    a.append(int(input()))
    num[a[i]-1]=0
for i in range(len(num)):
    if num[i]!=0:
        print(num[i])