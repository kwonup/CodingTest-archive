import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque() 
for _ in range(n):
    cmd = input().rstrip()
    if cmd.startswith('1'):
        q.appendleft(int(cmd[2:]))
    elif cmd.startswith('2'):
        q.append(int(cmd[2:]))
    elif cmd == '3':
        print(q.popleft() if q else '-1')
    elif cmd == '4':
        print(q.pop() if q else '-1')
    elif cmd == '5':
        print(len(q))
    elif cmd == '6':
        print('0' if q else '1')
    elif cmd == '7':
        print(q[0] if q else '-1')
    elif cmd == '8':
        print(q[-1] if q else '-1')