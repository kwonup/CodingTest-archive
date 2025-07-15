import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
# graph.append(list(map(int,input().split())) for _ in range(m))
for _ in range(m):
    a,b = list(map(int,input().split()))
    #간선이 양방향으로 연결된것이므로 양쪽노드에 모두 추가
    graph[a].append(b) #a노드에 b노드 연결
    graph[b].append(a) #b노드에 a노드 연결
for i in graph:
    i.sort()
#print('graph = ',graph)

visited = [False]*(n+1)

#DFS함수
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#BFS함수
from collections import deque

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = True #첫번째 노드 방문처리
    while queue: #큐가 빌때까지
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

dfs(graph,v,visited)
print()
visited = [False]*(n+1)
bfs(graph,v,visited)
