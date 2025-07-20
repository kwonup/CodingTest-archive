import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(col,row):
    #범위를 벗어나거나, 이미 방문했거나 배추가 없는 칸이면 종료 
    if col < 0 or col >= m or row < 0 or row >= n or grid[row][col] == 0 or visited[row][col]:
        return
    visited[row][col] = True
    for i in range(4):
        n_col = col + dy[i]
        n_row = row +dx[i]
        dfs(n_col,n_row)
    

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    visited = [[False]*m for _ in range(n)]
    grid = [[0]*m for _ in range(n)] 
    for _ in range(k):
        col,row = map(int,input().split())
        grid[row][col] = 1

    cnt = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1 and visited[row][col] == False:
                dfs(col,row)
                cnt+=1
    print(cnt)