import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
def dfs(graph,v,visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            cnt += 1 
            dfs(graph,i,visited)
dfs(graph,1,visited)
print(cnt)
