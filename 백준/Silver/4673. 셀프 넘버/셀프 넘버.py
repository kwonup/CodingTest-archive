a=list(range(1,10001))
b=[]
for i in a:
    sum=i
    for j in str(sum):
        sum+=int(j)
    if sum<=10000:
        b.append(sum)
for i in set(b):
    a.remove(i)
for i in a:
    print(i)