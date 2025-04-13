import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=set()
for i in a:
    if i  not in b:
        c.add(i)
for i in b:
    if i not in a:
        c.add(i)
print(len(c))