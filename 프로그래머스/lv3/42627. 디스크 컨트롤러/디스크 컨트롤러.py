import heapq

def solution(jobs):
    heap = []
    jobs.sort()
    answer, time, i = 0, 0, 0
    start = -1

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            job = heapq.heappop(heap)
            start = time
            time += job[0]
            answer += time - job[1]                
            i += 1
        else:
            time +=  1

    return answer // len(jobs)