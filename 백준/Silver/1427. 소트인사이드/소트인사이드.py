import sys
input = sys.stdin.readline
n = int(input())
digit = []
while n>0:
    single = n%10
    n=n//10
    digit.append(single)

digit.sort(reverse=1)
for i in digit:
    print(i,end='')