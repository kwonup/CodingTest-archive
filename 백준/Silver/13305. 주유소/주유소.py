import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))
price = list((map(int,input().split())))

total = 0
min_price = price[0]
for i in range(n-1):
    if price[i]< min_price:
        min_price = price[i]
    total += min_price * distance[i]

print(total)
