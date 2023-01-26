a=[]
max=0
for i in range(9):
    a.append(int(input()))
    if a[i]>max:
        max=a[i]
        idx=i
print(max)
print(idx+1)