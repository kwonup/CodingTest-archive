import sys
input = sys.stdin.readline
n = int(input())

cost = [list(map(int,input().split())) for _ in range(n)]
#dp[i][j] 는 i번째 집을 j번 색으로 칠했을때 최소비용
dp = [[0]*3 for _ in range(n)]

#dp[0][0],dp[0][1],dp[0][2] = cost[0][0],cost[0][1],cost[0][2]
dp[0] = cost[0]
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+cost[i][2]

print(min(dp[n-1]))