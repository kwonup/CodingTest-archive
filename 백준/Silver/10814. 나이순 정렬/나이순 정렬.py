import sys
input = sys.stdin.readline
n = int(input())
members = []
for i in range(n):
    age,name = input().split()
    members.append((int(age),name)) #여기서 튜플형태로 리스트에 추가

#나이기준 정렬
members.sort(key=lambda x: x[0])

for age,name in members:
    print(age,name)