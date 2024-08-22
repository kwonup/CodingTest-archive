n = int(input())
scores = list(map(int,input().split()))
M = max(scores)
avg = 0
for i in scores:
    avg+=i/M*100
print(avg/n)