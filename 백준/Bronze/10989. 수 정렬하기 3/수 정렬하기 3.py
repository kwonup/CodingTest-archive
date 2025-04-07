import sys
input = sys.stdin.readline
cnt = [0]* 10001 #1부터 10000까지 수의 빈도를 저장

n = int(input())
for _ in range(n):
    num=int(input())
    cnt[num]+=1

#숫자가 등장한 횟수만큼 출력
for i in range(1,10001):
    if cnt[i]>0:
        for _ in range(cnt[i]): print(i)