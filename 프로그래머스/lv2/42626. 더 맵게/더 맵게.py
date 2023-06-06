import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for x in scoville:
        heapq.heappush(heap, x)
    
    while heap[0] < K:
        answer += 1
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        heapq.heappush(heap, x + 2*y)
        
        if len(heap) == 1 and heap[0] < K: # 모든 음식의 스코빌 지수가 K 이상이 아닐 때
            answer = -1
            break
        
    return answer