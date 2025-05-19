import sys
from collections import deque

input = sys.stdin.readline

n = int(input())                         # 자료구조 개수
A = list(map(int, input().split()))      # 0=큐, 1=스택
B = list(map(int, input().split()))      # 초기값
m = int(input())                         # 삽입할 수열 길이
C = list(map(int, input().split()))      # 삽입할 수열

# 1) A_i == 0인(큐) 위치의 B_i들만 뽑아서 deque로 초기화
dq = deque(b for a, b in zip(A, B) if a == 0)

# 2) 각 C의 원소 c에 대해
#    - dq가 비어 있지 않으면 pop()한 값을 출력으로, appendleft(c)로 상태 갱신
#    - 비어 있으면 c 자체를 출력
result = []
for c in C:
    if dq:
        x = dq.pop()
        dq.appendleft(c)
    else:
        x = c
    result.append(str(x))

# 3) 공백 구분 출력
print(" ".join(result))
