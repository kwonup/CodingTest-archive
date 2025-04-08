import sys
input = sys.stdin.readline
n = int(input())
log=set()  #여기서 list대신 set 사용
for i in range(n):
    name,msg = input().split()
    if msg == 'enter':
        log.add(name)
    elif msg == 'leave':
        log.remove(name)
for i in sorted(log,reverse=1):
    print(i)