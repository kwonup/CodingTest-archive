import sys 
input = sys.stdin.readline
n = int(input())
cnt=0
user = set() #채팅하는 인원을 담아두는 집합(중복없애기위해 집합사용)
for i in range(n):
    s = input().rstrip()
    if s == 'ENTER':
        cnt+= len(user)
        user.clear() #집합을 초기화
        continue
    user.add(s)

cnt += len(user) #마지막에 최종적으로 집합의 크기를 cnt변수에 더함
print(cnt)