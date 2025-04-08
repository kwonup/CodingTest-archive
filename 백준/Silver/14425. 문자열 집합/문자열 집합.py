import sys
input = sys.stdin.readline
n,m = map(int,input().split())
S = []
for _ in range(n):
    str = input()
    S.append(str)
count = 0
for _ in range(m):
    str = input()
    if str in S:
        count +=1
print(count)