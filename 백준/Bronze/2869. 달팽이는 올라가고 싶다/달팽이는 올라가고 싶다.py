import math
a,b,v = map(int,input().split())
dist = 0
cnt = 0

dist = math.ceil((v-b)/(a-b))
print(dist)