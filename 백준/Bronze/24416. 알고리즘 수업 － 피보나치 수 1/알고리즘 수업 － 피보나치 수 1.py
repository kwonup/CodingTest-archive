import sys 
input = sys.stdin.readline
n = int(input())

# 코드1 횟수 세는 재귀 함수
cnt1 = 0
def fib(x):
    global cnt1
    if x == 1 or x == 2: 
        cnt1 += 1 #코드1 실행 -> 카운트+1
        return 1
    else:
        return fib(x-1) + fib(x-2)

# 코드2 횟수 세기
def fibonacci(x):
    cnt2 = 0
    f = [0] * (x + 1)
    f[1] = f[2] = 1
    for i in range(3, x + 1): 
        f[i] = f[i - 1] + f[i - 2] # 코드2 실행 -> 카운트+1
        cnt2 += 1
    return cnt2

fib(n)
cnt2 = fibonacci(n)
print(cnt1, cnt2)