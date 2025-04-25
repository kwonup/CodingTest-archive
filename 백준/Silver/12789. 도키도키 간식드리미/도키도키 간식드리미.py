import sys 
input = sys.stdin.readline
from collections import deque
n = int(input())
subline = []
q = deque(map(int,input().split()))
num = 1 #번호순서 저장하는 변수

while q: #큐(대기열) 순회
    if q[0] == num: #번호순서와 현재 대기열 앞사람의 번호가 같다면
        q.popleft()
        num+=1
    elif subline and subline[-1]==num: #보조열이 차있으면서 보조열의 마지막원소가 번호순서와 같으면
        subline.pop()
        num+=1
    else: #번호순서와 현재 대기열 앞사람의 번호가 다르다면
        subline.append(q.popleft())
while subline: #보조 대기열 순회
    if subline.pop() == num:
        num+=1
    else:
        break             
print("Nice" if len(subline)==0 else "Sad")