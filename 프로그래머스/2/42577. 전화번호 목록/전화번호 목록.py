def solution(phone_book):
    answer = True
    numbers = set(phone_book)
    for num in phone_book:
        for i in range(len(num)):
            if num[:i] in numbers:
                return False
    return answer