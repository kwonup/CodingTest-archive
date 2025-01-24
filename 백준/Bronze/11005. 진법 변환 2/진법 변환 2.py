def decimal_to_base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while N > 0:
        remainder = N % B
        result = digits[remainder] + result
        N //= B

    return result

# 입력
N, B = map(int, input().split())

# 결과 출력
print(decimal_to_base(N, B))