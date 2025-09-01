import heapq
def solution(scv, K):
    cnt = 0
    heapq.heapify(scv)
    while len(scv)>=2:
        min_1 = heapq.heappop(scv)
        if min_1 >= K:
            return cnt
        else:
            min_2 = heapq.heappop(scv)
            heapq.heappush(scv, min_1 + (min_2*2))
            cnt += 1
    #만약 모든음식 스코빌지수를 K이상으로 만들수없을경우
    if scv[0]<K: return -1
    return cnt