import sys 
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = list(input().rstrip())
    prts = []
    for i in s:
        if i == '(': 
            prts.append(i)
        elif i == ')':
            if prts:
                prts.pop()
            else:
                prts.append(i)
                break
    print('YES' if len(prts)==0 else 'NO')