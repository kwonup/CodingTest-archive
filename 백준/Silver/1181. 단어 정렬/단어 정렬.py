import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    words.append(word)
    
# 중복 제거
words = list(set(words))
# 길이 기준 → 사전순 정렬
words.sort(key=lambda x: (len(x), x))
# 한 줄에 하나씩 출력
for word in words:
    print(word)