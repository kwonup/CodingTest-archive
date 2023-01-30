a=list(range(1,10001))
for i in range(1,10001):
    n=i
    sum=n
    while 1:
        sum+=n%10
        n=n//10 #//는 몫 연산자
        if n<1: break
    if sum in a:
        a.remove(sum)
for i in range(len(a)):
    print(a[i])