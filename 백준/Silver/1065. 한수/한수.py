n=int(input())
sum=0
for i in range(1,n+1):
    if i<100:
        sum+=1
    else:
        c=i%10
        b=int((i/10)%10)
        a=int(i/100)
        if b-a == c-b:
            sum+=1
print(sum)
