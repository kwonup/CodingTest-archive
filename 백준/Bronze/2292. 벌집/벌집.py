n = int(input())
room = 1

i=1 #6의배수로 증가하기 때문에 6에 곱해줄 변수
while n>1:
    room+=1 #방의 개수1씩증가
    n-=6*i #6의배수로 n에서 빼줌
    i+=1
print(room)