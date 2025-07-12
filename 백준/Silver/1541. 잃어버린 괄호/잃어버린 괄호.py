import sys,re
input = sys.stdin.readline

exp = input().rstrip().split('-')
total = sum(list(map(int,re.findall(r"\d+",exp[0]))))
        
for str in exp[1:]:
    total -= sum(list(map(int,re.findall(r"\d+",str))))
    
print(total)