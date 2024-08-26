s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i]!=' ' and s[i+1]==' ':
        cnt+=1
#s가 비어있지 않으면서 s가 공백이 아니라면 cnt+=1 
if s and s[-1]!=' ':
    cnt+=1
print(cnt)