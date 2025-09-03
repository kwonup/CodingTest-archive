def solution(participant, completion):
    answer = ''
    hash={}
    for p in participant:
        if p in hash:
            hash[p]+=1
        else:
            hash[p]=1

    for c in completion:
        if c in hash:
            hash[c] -=1
    for key in hash:
        if hash[key] == 1: return key
 