a=[]
a_cnt=[]
for i in range(10):
    n=int(input())
    a.append(n)
    a[i]=n%42
    if a[i] not in a_cnt:
        a_cnt.append(a[i])
print(len(a_cnt))