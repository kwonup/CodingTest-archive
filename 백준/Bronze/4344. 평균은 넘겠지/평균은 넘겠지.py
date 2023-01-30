n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    avg=sum(s[1:])/s[0]
    cnt=0
    for j in range(1,s[0]+1):
        if s[j]>avg:
            cnt+=1
    print('%.3f%%'%(cnt/s[0]*100))