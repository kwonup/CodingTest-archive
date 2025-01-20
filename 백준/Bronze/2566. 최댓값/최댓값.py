arr = [0 for _ in range(9)]
tmp = 0
max_row = 1
max_col = 1
for i in range(9):
    arr[i] = list(map(int,input().split()))
    M = max(arr[i])
    if M>tmp : 
        tmp = M
        max_row = i+1
        max_col = arr[i].index(M)+1
print(tmp)
print(max_row,max_col)