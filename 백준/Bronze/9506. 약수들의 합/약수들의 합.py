def myfunction(n):
    submul=[]
    for i in range(1,n+1):
        if(n%i==0): submul.append(i)
    if sum(submul[:-1])==n:
        return submul[:-1]
    else : return False

while True:
    n=int(input())
    if n==-1: break
    list = myfunction(n)
    print(n,end='')
    if list!=False:
        print(' = ',end='')
        for i in range(len(list)):
            print(list[i],end='')
            if i!=len(list)-1: print(' + ',end='')
        print()
    else:
        print(' is NOT perfect.')