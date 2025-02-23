a,b,c = map(int,input().split())

tri=[a,b,c]
tri.sort()

if tri[2]<tri[0]+tri[1]:
    print(sum(tri))
else:
    for i in range(tri[2],0,-1):
        if i<tri[0]+tri[1]:
            print(i+tri[0]+tri[1])
            break