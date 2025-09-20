from collections import deque

def solution(maps):
    def bfs(maps):
        n, m = len(maps), len(maps[0])   # 맵의 세로, 가로 크기
        dx = (-1,1,0,0)                   # 상, 하, 좌, 우 이동 방향 (행 변화량)
        dy = (0,0,-1,1)                   # 상, 하, 좌, 우 이동 방향 (열 변화량)

        # 방문 여부와 최단거리 기록용 2차원 배열
        dist = [[0]*m for _ in range(n)]
        dist[0][0] = 1                    # 시작점은 거리 1

        q = deque([(0,0)])                # BFS 시작 큐 (출발 좌표)
        while q:
            x, y = q.popleft()

            # 도착점에 도달하면 해당 칸까지의 최단 거리 반환
            if x == n-1 and y == m-1: 
                return dist[x][y]

            # 4방향 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 맵 범위 내, 벽이 아니고, 아직 방문하지 않았다면
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1  # 이전 거리 + 1
                    q.append((nx, ny))             # 큐에 삽입

        # 끝까지 탐색했는데 도착 불가하면 -1 반환
        return -1

    # BFS 실행 결과가 정답
    answer = bfs(maps)
    return answer
