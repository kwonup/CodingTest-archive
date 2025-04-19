import sys 
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s.rstrip()=='.': #만약 문자열 오른쪽을 strip한 결과가 '.'이면 입력종료
        break
    stack=[]
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':  
            if stack: #스택이 비어있지않다면
                if stack.pop() == '[': #스택에서 pop한다음 그 원소가 짝이 맞지않으면
                    stack.append(i) #스택에추가(스택이 비어있지 않으면 불균형이므로 일부러 추가함)
                    break
            else:
                stack.append(i) #스택이 비어있다면 스택에 추가
                break
        elif i == ']':
            if stack: #스택이 비어있지않다면
                if stack.pop() == '(':
                    stack.append(i)
                    break
            else:
                stack.append(i) #스택이 비어있다면 스택에 추가
                break
    print('yes' if len(stack)==0 else 'no')