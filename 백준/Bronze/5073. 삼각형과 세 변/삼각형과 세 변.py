while True:
    a,b,c = map(int,input().split())
    if a == b==c==0 : break
    tri = [a,b,c]
    tri.sort()
    if tri[2] < tri[0]+tri[1]:
        if a==b==c:
            print("Equilateral")
        elif a==b or b==c or a==c:
            print("Isosceles")
        else:
            print("Scalene")
    else : 
        print("Invalid")