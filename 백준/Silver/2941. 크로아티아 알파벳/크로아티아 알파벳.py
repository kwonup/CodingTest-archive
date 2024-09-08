word = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
for i in croatia:
    while True:
        idx = word.find(i) 
        if idx == -1: break #더이상 찾을 수 없으면 종료
        word = list(word) #파이썬에서 문자열은 불변이기때문에 리스트로 변환
        for j in range(idx,idx+len(i)):
            word[j]=' ' #크로아티아문자 부분을 공백으로 변환
        word = ''.join(word) #다시 문자열로 변환
        cnt+=1
word = word.replace(' ','') #word의 공백을제거
print(cnt+len(word))
