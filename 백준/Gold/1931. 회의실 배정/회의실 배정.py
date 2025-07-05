import sys
input = sys.stdin.readline
n = int(input())
meeting = list(list(map(int,input().split())) for _ in range(n))

meeting.sort(key = lambda x:(x[1],x[0])) # key를 기준으로 정렬
cnt = 0
available = []
available.append(meeting[0])
j=0
for i in range(1,n):
    if available[j][1]<=meeting[i][0]:
        available.append(meeting[i])
        j+=1
print(len(available))