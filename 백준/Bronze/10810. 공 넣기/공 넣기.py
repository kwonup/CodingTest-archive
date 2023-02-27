n,m=map(int,input().split())
basket = [0]*n
for x in range(m):
    i,j,k=map(int,input().split())
    for y in range(i-1,j):
        basket[y] = k
for i in range(n):
    print(basket[i],end=' ')