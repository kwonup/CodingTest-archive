import sys
input = sys.stdin.readline
n,m = map(int,input().split())
cnt = 0
list1 = set()
for _ in range(n):
    list1.add(input().rstrip())
answer = []
for _ in range(m):
    name = input().rstrip()
    if name in list1:
        answer.append(name)
answer.sort()
print(len(answer))
for i in answer: 
    print(i)