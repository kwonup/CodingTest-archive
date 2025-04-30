import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
balloon =[(i+1,num) for i,num in enumerate(nums)]
bursted = []
idx = 0
while balloon:
    position,step = balloon.pop(idx)
    bursted.append(position)
    if balloon:
        if step>0:
            idx = (idx + step-1) % len(balloon)
        else:
            idx = (idx + step) % len(balloon)  

print(' '.join(map(str,bursted)))