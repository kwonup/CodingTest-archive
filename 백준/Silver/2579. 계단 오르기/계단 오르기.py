import sys
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n) ]
dp = [0 for _ in range(n)] #i번째 계단까지 왔을때 얻을수있는 최대점수
if n==1:
    dp[0] = stair[0]
elif n==2:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
else:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
    dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])
    for i in range(3,n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
print(dp[-1])
