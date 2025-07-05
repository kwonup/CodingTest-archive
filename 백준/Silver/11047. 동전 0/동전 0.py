import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coins = list(int(input()) for _ in range(n))

coins.sort(reverse=1)
answer = 0
for i in coins:
    if i<=k:
        answer += k//i
        k = k%i
    if k==0: 
        break
print(answer)