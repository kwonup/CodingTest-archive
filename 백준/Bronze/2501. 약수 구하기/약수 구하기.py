n,k = map(int,input().split())
submul=[]
for i in range(1,n+1):
    if n%i==0: submul.append(i)
if len(submul) < k: print(0) 
else: print(submul[k-1])