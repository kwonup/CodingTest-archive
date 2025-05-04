import sys
input = sys.stdin.readline
n = int(input())

#소수(prime number) 판별 함수
def isPrime(x):
    if x<2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True

for _ in range(n): 
    num = int(input())
    i = num
    while isPrime(i)==False: #i가 소수가 아닐동안 반복문 돌다가 소수이면 종료
        i+=1
    print(i)