def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # 우선순위가 더 높은 프로세스 있는지 확인
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    return answer