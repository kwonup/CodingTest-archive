import sys
input = sys.stdin.readline
n = int(input())

##최대공약수(gcd) 구하는 함수(유클리드 호제법 사용)
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

trees = [int(input()) for _ in range(n)] #가로수 입력받기

gaps = [trees[i+1]-trees[i] for i in range(len(trees)-1)]#가로수의 간격들 저장하는 리스트

#간격들의 최대공약수 구하는 로직
gcd_all = gaps[0]
for i in gaps:
    gcd_all = gcd(gcd_all,i)

#간격들 사이에 들어갈 가로수개수
answer = sum((i//gcd_all -1) for i in gaps)
print(answer)