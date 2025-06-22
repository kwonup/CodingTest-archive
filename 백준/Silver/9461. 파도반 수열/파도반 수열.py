import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

dp = [0]*101 #파도반 수열 값을 미리 계산해둘 리스트
dp[1],dp[2],dp[3] = 1,1,1 #문제에서 주어진 초기값 설정

#점화식을 이용해 P(4)부터 P(100)까지 채워나감
for i in range(4,101):
    dp[i] = dp[i-2] + dp[i-3] #점화식: P(n) = P(n-2)+P(n-3)

for _ in range(T):
    N = int(input())
    print(dp[N])