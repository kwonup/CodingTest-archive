n,m=map(int,input().split())
bsk=[i+1 for i in range(n)]
for _ in range(m):
    i,j=map(int,input().split())
    tmp = []
    for k in range(i-1,j):
        tmp.append(bsk[k])
    tmp = tmp[::-1]
    num=0
    for k in range(i-1,j):
        bsk[k] = tmp[num]
        num+=1
for k in range(n):
    print(bsk[k],end=' ')