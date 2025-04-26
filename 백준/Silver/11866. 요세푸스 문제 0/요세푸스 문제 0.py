import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
circle = list(range(1,n+1))
josephus = []
idx = k-1
for i in range(n):
    #print('idx = ',idx)
    josephus.append(circle.pop(idx))
    #print('josephus : ',josephus)

    idx -= 1
    for j in range(k):
        idx += 1
        if idx >= len(circle): 
            idx = 0

    #print(circle)
    #print()
print(f"<{', '.join(map(str, josephus))}>")