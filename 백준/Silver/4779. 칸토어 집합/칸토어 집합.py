import sys
input = sys.stdin.readline

def cantor(s,start,end):
    if end-start<3:
        return
    size = (end-start)//3
    for i in range(start+size,start+2*size):
        s[i]=' ' #가운데부분 빈 공백으로 바꿔줌
    cantor(s,start,start+size) #왼쪽부분 재귀 호출
    cantor(s,start+2*size,end) #오른쪽부분 재귀 호출

    
while True:
    try:
        line = input()
        if not line:
            break  # 더 이상 입력이 없으면 종료
        n = int(line.strip())
        length = 3 ** n
        s = ['-'] * length
        cantor(s, 0, length)
        print(''.join(s))
    except EOFError:
        break
