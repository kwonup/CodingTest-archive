a,b=map(int,input().split())
c=int(input())
t=(a*60)+b+c

if(t>=24*60):
    t=t-24*60
print(int(t/60),t%60)


