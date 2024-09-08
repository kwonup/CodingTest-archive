n = int(input())
notGroup = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if (word[j] != word[j+1]) and (word[j] in word[j+1:]) :
            notGroup+=1
            break
print(n-notGroup)