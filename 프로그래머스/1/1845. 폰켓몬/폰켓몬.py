def solution(nums):
    answer = 0
    unique_nums = set(nums)
    #answer = len(nums)/2 if len(nums)/2< len(unique_nums) else len(unique_nums)
    answer = min(len(nums)/2,len(unique_nums))
    return answer