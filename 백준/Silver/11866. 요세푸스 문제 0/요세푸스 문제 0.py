import sys
input = sys.stdin.readline

n,k = map(int,input().split())
circle = list(range(1,n+1))
josephus = []
idx = k-1
while circle:
    josephus.append(circle.pop(idx))
    if not circle: break #마지막 순회때 len(circle)==0 이면 반복문 탈출
    idx = (idx + k-1) % len(circle) #나머지 연산 사용 (원순열)

print(f"<{', '.join(map(str,josephus))}>")