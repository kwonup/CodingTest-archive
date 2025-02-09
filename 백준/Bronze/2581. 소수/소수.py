#백준2581 브론즈2 소수
def isPrime (n):
    if n==1: return False
    else:
        for i in range(2,int(n**0.5)+1): #2부터 n의 제곱근까지만 검사
            if n%i==0 : return False
        return True #나누어 떨어지는 수가 없으면 true반환
m=int(input())
n=int(input())
primeArr = []
for i in range(m,n+1):
    if isPrime(i) : primeArr.append(i)
if len(primeArr)==0 : print(-1)
else:
    print(sum(primeArr))
    print(min(primeArr))