def solution(s):
    stk = []
    for i in s:
        if i == '(':
            stk.append(i)
        else:
            if stk and stk[-1]=='(':
                stk.pop()
            else: return False
    if stk: return False
    return True