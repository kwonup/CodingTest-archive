import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int,input().split()))

m = int(input())
compare = list(map(int,input().split()))

card_num ={}
for i in range(len(card)):
    if card[i] not in card_num:
        card_num[card[i]]=1
    else:
        card_num[card[i]]+=1
        
result=[]
for i in compare:
    if i in card_num:
        result.append(str(card_num[i]))
    else:
        result.append('0')

print(' '.join(result))