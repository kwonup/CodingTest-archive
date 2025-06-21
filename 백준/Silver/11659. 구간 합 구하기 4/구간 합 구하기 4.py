import sys
input = sys.stdin.readline

n,m = map(int,input().split())

number = list(map(int,input().split()))

prefix_sum = [0]  #인덱스 0은 0으로 시작 (편의를 위해)

#누적합 리스트 계산
for i in range(n):
    prefix_sum.append(number[i] + prefix_sum[-1])


for _ in range(m):
    i,j = map(int,input().split())
    print(prefix_sum[j]-prefix_sum[i-1]) #구간 [i,j]의 합은 prefix_sum[j]-prefix[i-1]