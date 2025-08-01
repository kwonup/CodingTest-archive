import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int,input().split()))
price = list((map(int,input().split())))
total = 0
for i in range(n-1):
    m = min(price[:i+1])
    total += m * distance[i]
print(total)