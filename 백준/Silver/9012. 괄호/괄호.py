import sys 
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = list(input().rstrip())
    prts = []
    isVps = True
    for i in range(len(s)):
        if s[i] == '(': 
            prts.append(s[i])
        elif len(prts)!=0 and s[i] == ')':
            prts.pop()
        else: # prts가 비어있으면서 ')'일때
            isVps=False
            break
    if isVps == True and len(prts)==0:
        print('YES')
    else:
        print('NO')