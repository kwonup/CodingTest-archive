import sys
input = sys.stdin.readline
n,k = map(int,input().split())
A = list(map(int,input().split()))
count = 0
result = -1

#재귀적으로 배열을 반으로 나누고, 각각정렬한 뒤 병합
#의사코드와 동일하게 q는 중간지점
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        count += 1
        if count == k:
            result = tmp[t]

merge_sort(A,0,n-1)

print(result)