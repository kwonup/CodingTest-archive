import sys
input = sys.stdin.readline
n = int(input())
meeting = list(list(map(int,input().split())) for _ in range(n))

meeting.sort(key = lambda x:(x[1],x[0])) # key를 기준으로 정렬

cnt = 0
endPoint = 0
for start,end in meeting:
    if endPoint <= start:
        cnt+=1
        endPoint = end
print(cnt)