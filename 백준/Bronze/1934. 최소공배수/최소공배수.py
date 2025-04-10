import sys
input = sys.stdin.readline
n = int(input())
#최소공배수 구하는 함수
def LCM(a,b):
    for i in range(1,max(a,b)+1):
        if (a*i)%b==0:
            return a*i

for _ in range(n):
    a,b = map(int,input().split())
    print(LCM(a,b))