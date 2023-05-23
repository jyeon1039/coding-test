import math

def solution(progresses, speeds):
    answer = []
    queue = []
    
    # 각 작업마다 소요되는 날
    for x in zip(progresses, speeds):
        day = math.ceil((100-x[0]) / x[1])
        queue.append(day)
        
    day = 1
    beforeDay = queue[0]
    
    for i in range(1, len(queue)):
        if queue[i] <= beforeDay:
            day += 1
        else:
            answer.append(day)
            day = 1
            beforeDay = queue[i]
    
    answer.append(day)
    
    return answer