x = int(input())
#step1: x가 몇번째 대각선에 속하는지 찾음
n=1
while (n*(n+1))//2 < x:
    n+=1
start = (n * (n - 1)) // 2 + 1  # 해당 대각선의 시작 번호
position = x - start + 1  # 해당 대각선에서 몇 번째인지

if n%2==1: #대각선번호가 홀수일때
    print('{}/{}'.format(n+1-position, position))
else: #대각선 번호가 짝수일때
    print('{}/{}'.format(position,n+1-position))
