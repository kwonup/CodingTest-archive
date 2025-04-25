import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque()
for _ in range(n):
    cmd = input().rstrip()
    if cmd[:4] == 'push':
        q.append(int(cmd[5:]))
    elif cmd == 'pop':
        print(q.popleft() if q else '-1')
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print('1' if len(q)==0 else '0')
    elif cmd == 'front':
        print(q[0] if q else '-1')
    elif cmd == 'back':
        print(q[-1] if q else '-1')
