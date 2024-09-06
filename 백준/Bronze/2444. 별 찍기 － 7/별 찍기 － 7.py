n = int(input())
star ='*'
blank=' '*(n-1)
for i in range(n):
    print(blank,end='')
    print(star)
    star+='**'
    blank = blank[:-1]
blank=' '
star = star[:-4]
for i in range(n-1):
    print(blank,end='')
    print(star)
    star = star[:-2]
    blank+=' '