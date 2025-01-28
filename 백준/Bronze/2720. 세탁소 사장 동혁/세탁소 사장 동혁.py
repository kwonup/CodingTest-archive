Q = 25
D = 10
N = 5
P = 1
n = int(input())
for _ in range(n):
    change = int(input())
    # 동전의 개수 계산
    Q_cnt = change // Q
    change %= Q

    D_cnt = change // D
    change %= D

    N_cnt = change // N
    change %= N

    P_cnt = change // P
    change %= P
    print("%d %d %d %d" %(Q_cnt,D_cnt,N_cnt,P_cnt))