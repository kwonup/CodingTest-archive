import sys
input = sys.stdin.readline
s = input().rstrip()
substr = set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substr.add(s[i:j])
print(len(substr))
