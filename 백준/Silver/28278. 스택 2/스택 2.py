import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        output.append(str(stack.pop()) if stack else '-1')
    elif cmd[0] == 3:
        output.append(str(len(stack)))
    elif cmd[0] == 4:
        output.append('0' if stack else '1')
    elif cmd[0] == 5:
        output.append(str(stack[-1]) if stack else '-1')

print('\n'.join(output))
