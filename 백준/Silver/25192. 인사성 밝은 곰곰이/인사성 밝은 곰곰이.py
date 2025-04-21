import sys 
input = sys.stdin.readline
n = int(input())
isNew = False
cnt=0
user = set() #채팅하는 인원을 담아두는 집합(중복없애기위해 집합사용)
for i in range(n):
    s = input().rstrip()
    if s == 'ENTER':
        cnt+= len(user)
        user= set()
        continue
    user.add(s)

cnt+=len(user)
print(cnt)