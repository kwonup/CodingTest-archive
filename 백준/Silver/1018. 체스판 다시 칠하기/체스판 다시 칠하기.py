import sys
input = sys.stdin.readline
m,n = map(int,input().split())
board = list(list(input().strip()) for _ in range(m)) #strip을 쓰는 이유는 sys.stdin.readline으로 입력받을때 생기는 맨 뒤의 개행문자를 제거하기 위해

#2가지 완전한 체스판 경우의 수: 왼쪽 위가'W'인 경우와 'B'인 경우
W_BOARD = [['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
B_BOARD = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W','B']]

#먼저 모든 8*8 경우의 수로 쪼개기
for i in range(m-7):
    for j in range(n-7):
        repaint_w = 0  # W로 시작하는 체스판 기준 다시 칠해야 하는 칸 수
        repaint_b = 0  # B로 시작하는 체스판 기준 다시 칠해야 하는 칸 수
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y]!=W_BOARD[x][y]:
                    repaint_w+=1
                elif board[i+x][j+y]!=B_BOARD[x][y]:
                    repaint_b+=1
        if i==0 and j==0: min_repaint = repaint_w
        min_repaint = min(min_repaint, repaint_w, repaint_b)
        
print(min_repaint)