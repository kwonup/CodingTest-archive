import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y)) 
    visited[x][y] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt+=1
    return cnt

result =[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==False:
            cnt = bfs(i,j)
            result.append(cnt)
print(len(result))
for i in sorted(result):
    print(i)