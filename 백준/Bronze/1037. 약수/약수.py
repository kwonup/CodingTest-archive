import sys
input = sys.stdin.readline
n = int(input())
submul = list(map(int,input().split()))
print(max(submul)*min(submul))