import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque(range(1,n+1))

while len(q)>1:
    q.popleft()
    if len(q)==1: break
    q.append(q.popleft())
print(q[0])