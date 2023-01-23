n=int(input())
if n<10:
    n=n*10
x=n
cnt=0
while 1:
    cnt+=1
    a=int(x/10); b=x%10; c=a+b
    x=(b*10)+(c%10)
    if x==n: break
print(cnt)