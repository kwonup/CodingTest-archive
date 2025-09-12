from collections import deque
def solution(prts, location):
    answer = 0
    q = deque((val,idx)for idx,val in enumerate(prts))
    
    done = 0 #실행완료된 횟수
    while q:
        val,idx = q.popleft()
        if q and val < max(q,key=lambda x:x[0])[0]:# 큐에 꺼낸값보다 큰 값이 존재할경우
            q.append((val,idx))#큐 맨뒤에 추가
        else: # 큐에 꺼낸값보다 큰 값이 존재X
            done+=1
            if location==idx:
                answer=done
                break
    return answer