import sys
input = sys.stdin.readline
t = int(input())
#재귀함수, l은 시작인덱스 r은 끝인덱스
def recursion(s,l,r):
    global cnt #cnt를 전역변수로 수정할수있도록 함
    cnt+=1
    if l>=r : return 1
    elif s[l]!=s[r]: return 0
    else: return recursion(s,l+1,r-1)
#palindrome판별함수
def isPalindrome(s):
    return recursion(s,0,len(s)-1)

for _ in range(t):
    s = input().strip()
    cnt=0 #전역변수 cnt 리셋
    print(isPalindrome(s),cnt)