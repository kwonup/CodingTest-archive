N,M = map(int,input().split())

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    A[i] = list(map(int,input().split()))
for i in range(N):
    B[i] = list(map(int,input().split()))

answer = []
for i in range(N):
    tmp=[]
    for j in range(M):
        tmp.append(A[i][j]+B[i][j])
    answer.append(tmp)

for i in range(N):
    for j in range(M):
        print(answer[i][j],end = ' ')
    print()
    
