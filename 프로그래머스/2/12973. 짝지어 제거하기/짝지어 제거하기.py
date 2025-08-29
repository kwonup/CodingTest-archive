def solution(s):
    stk = []
    for ch in s:
        if stk and stk[-1]==ch:
            stk.pop()
        else:
            stk.append(ch)
    answer = 1 if not stk else 0
    return answer