def solution(nums):
    answer = ''
    nums = list(map(str,nums))
    nums.sort(key=lambda x:x*5,reverse=True)
    answer = str(int(''.join(nums)))
    return answer