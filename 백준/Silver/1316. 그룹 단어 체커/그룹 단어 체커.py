n = int(input())
group_cnt = 0
for i in range(n):
    word = input()
    isGroup = 1
    for j in range(0,len(word)-1):
        if word[j] == word[j+1]:
            isGroup = 1
        elif word[j] in word[j+1:]:
            isGroup = 0
            break
    if(isGroup==1): group_cnt += 1

print(group_cnt)