from itertools import permutations
#소수판별 함수
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1): #n의 제곱근까지만 반복
        if n%i==0: return False #나누어 떨어지면 소수아니므로 False
    return True #나누어떨어지는 수 없으므로 소수
#숫자 조합해서 만들수있는 모든 정수 찾는 함수
def all_num(digits):
    result = set() 
    for i in range(1,len(digits)+1):
        #파이썬 내장함수 permutations
        for perm in permutations(digits,i):
            result.add(int(''.join(perm)))
    return result

def solution(nums):
    answer = 0
    nums = all_num(nums)
    for n in nums:
        if is_prime(n): answer+=1
    return answer