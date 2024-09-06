s=input()
answer=1
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        answer = 0
        break
    answer=1
print(answer)