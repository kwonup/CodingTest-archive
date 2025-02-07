def isPrime (n):
    cnt=0
    for i in range(1,n):
        if n%i==0: cnt+=1
    if cnt==1: return True
    else : return False

n = int(input())
arr = list(map(int,input().split()))
cnt=0
for i in arr:
    if isPrime(i): cnt+=1
print(cnt)