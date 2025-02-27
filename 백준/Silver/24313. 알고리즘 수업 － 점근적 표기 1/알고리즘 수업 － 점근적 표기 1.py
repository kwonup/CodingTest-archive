a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# 1. a1 < c인 경우: n = n0에서 조건을 확인하면 충분함.
if a1 < c:
    if a1 * n0 + a0 <= c * n0:
        print(1)
    else:
        print(0)
# 2. a1 == c인 경우: a0가 0 이하여야 모든 n에서 성립함.
elif a1 == c:
    if a0 <= 0:
        print(1)
    else:
        print(0)
# 3. a1 > c인 경우: n이 커질수록 f(n) > c*n이 되므로 조건 미달.
else:
    print(0)