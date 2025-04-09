import sys
input = sys.stdin.readline
n,m = map(int,input().split())
book1 = {}
book2 = {}
for i in range(1,n+1):
    name = input().rstrip()
    book1[i] = name
    book2[name] = i
    
for i in range(m):
    answer = input().rstrip()
    if answer.isdigit():
        print(book1[int(answer)])
    else:
        print(book2[answer])