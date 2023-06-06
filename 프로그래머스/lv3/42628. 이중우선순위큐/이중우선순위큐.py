import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for o in operations:
        x, d = o.split()
        d = int(d)

        if x == "I":
            heapq.heappush(min_heap, d)
            heapq.heappush(max_heap, d*(-1)) # 최대값이 앞으로 나와야하므로 곱하기 -1
        else:
            if len(max_heap) != 0: # 빈 큐에 데이터를 삭제하라는 연산이 주어질 때, 해당 연산 무시
                if d == 1:
                    m = heapq.heappop(max_heap)
                    min_heap.remove(m*(-1))
                else:
                    m = heapq.heappop(min_heap)
                    max_heap.remove(m*(-1))
        
    if len(max_heap) == 0:
        return [0, 0]
    else:
        return [heapq.heappop(max_heap)*(-1), heapq.heappop(min_heap)]