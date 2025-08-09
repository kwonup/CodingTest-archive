import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

# 알파벳 26개에 대한 누적 등장 횟수를 저장할 리스트
# acc[i][j]: S의 0 ~ j-1까지에서 알파벳 chr(i + ord('a'))가 몇 번 등장했는지
acc = [[0] * (len(S) + 1) for _ in range(26)]

# 누적합 배열 채우기
for i in range(len(S)):
    ch_idx = ord(S[i]) - ord('a') # 현재 문자의 알파벳 인덱스
    for j in range(26):
        # 이전까지 누적합을 복사
        acc[j][i + 1] = acc[j][i]
    # 현재 문자의 등장 횟수 1 증가
    acc[ch_idx][i + 1] += 1
# 질의 처리
for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    ch_idx = ord(alpha) - ord('a')
    # 누적합을 이용해 구간 [l, r]에서 alpha가 몇 번 등장했는지 계산
    # acc[ch_idx][r+1]은 S[0]~S[r]까지의 누적 개수
    # acc[ch_idx][l]은 S[0]~S[l-1]까지의 누적 개수
    # 따라서 둘의 차이는 S[l]~S[r]까지 등장한 횟수
    result = acc[ch_idx][r + 1] - acc[ch_idx][l]
    print(result) #결과 출력
