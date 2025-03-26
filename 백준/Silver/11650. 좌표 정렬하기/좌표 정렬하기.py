import sys
input = sys.stdin.readline

n = int(input())
coord = [list(map(int,input().split())) for _ in range(n)]
coord.sort()
for i in range(n):
    print(coord[i][0],coord[i][1])