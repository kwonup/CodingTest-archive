n=int(input())
a=list(map(int,input().split()))
min=1000000;max=-1000000
for i in range(n):
    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
print(min,max)