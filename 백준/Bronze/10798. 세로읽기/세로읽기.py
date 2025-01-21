arr = []
for i in range(5):
    word = list(input())
    for j in range(15-len(word)): word.append(None)
    arr.append(word)
for i in range(15):
    for j in range(5):
        if(arr[j][i]!=None):
            print(arr[j][i],end='')