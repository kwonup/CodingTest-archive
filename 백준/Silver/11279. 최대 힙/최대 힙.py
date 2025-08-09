import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []  # 최소힙을 최대힙처럼 쓰기 위해 음수로 넣음

for _ in range(n):
    x = int(input())
    if x > 0:
        # 최대힙 효과를 위해 음수로 저장
        heapq.heappush(h, -x)
    else:
        # x == 0 : 최댓값 출력(없으면 0)
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)