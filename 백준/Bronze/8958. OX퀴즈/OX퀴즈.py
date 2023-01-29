n=int(input())
s=[]
for i in range(n):
    s=input()
    cnt=0
    score=0
    for j in range(len(s)):
        if s[j]=='O':
            cnt+=1
        else:
            cnt=0
        score+=cnt
    print(score)