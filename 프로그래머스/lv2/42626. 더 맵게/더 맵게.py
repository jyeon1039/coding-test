import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap[0] < K:
        answer += 1
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        heapq.heappush(heap, s1 + s2*2)
        
        if len(heap) == 1 and heap[0] < K:
            return -1
        
    return answer