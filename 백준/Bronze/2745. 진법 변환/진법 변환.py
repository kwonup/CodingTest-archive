# 입력 받기
N, B = input().split()
B = int(B)  # B를 정수로 변환

# N을 B진법에서 10진법으로 변환
decimal_value = int(N, B)

# 결과 출력
print(decimal_value)