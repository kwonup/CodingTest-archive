import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

def dfs(x,y):
    global cnt
    # 범위 벗어났으면 0반환
    if x<0 or x>=n or y<0 or y>=n or visited[x][y]==True or graph[x][y]==0:
        return 0
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        dfs(nx,ny)

#모든 칸을 돌면서 새로운 단지 발견시 dfs호출
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

print(len(result))
for i in sorted(result):
    print(i)
