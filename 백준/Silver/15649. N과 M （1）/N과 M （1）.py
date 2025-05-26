import sys
input = sys.stdin.readline
n,m  = map(int,input().split())

def dfs(n,m,path,visited):
    if len(path) == m:
        print(' '.join(map(str,path)))
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            dfs(n,m,path+[i],visited)
            visited[i] = False
visited = [False] * (n+1)
dfs(n,m,[],visited)