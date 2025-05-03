import sys
input = sys.stdin.readline
n = int(input())
def gcd(a,b): #유클리드 호제법으로 최소공배수 구하는 함수
    while b:
        a,b = b,a%b
    return a

gaps=[]
nums=[]
tmp = 0
for _ in range(n):
    num = int(input())
    nums.append(num)
    gaps.append(num-tmp)
    tmp = num
gaps = gaps[1:]

gcd_all = gaps[0]
for i in gaps[1:]:
    gcd_all = gcd(gcd_all,i)
        
answer = sum((i//gcd_all -1) for i in gaps)
print(answer)
