n = int(input())
constructor = 0 #생성자 0으로 선언
for i in range(1,n):
    s = str(i) #문자열로 변환
    n_sum = i #분해합에 i로 선언
    for j in s: #문자열 돌면서 분해합에 더함
        n_sum += int(j)
    if n_sum == n: #분해합과 n이 일치하면 생성자에 i대입후 반복문 종료
        constructor = i
        break

if constructor == 0: print(0) #생성자가 없을경우
else : print(constructor) #생성자가 있을경우