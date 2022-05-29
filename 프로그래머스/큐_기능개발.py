import math

def solution(progresses, speeds):
    answer = []
    queue = []
    # 각 작업마다 소요되는 날
    for i in range(len(progresses)):
        progress = 100 - progresses[i]
        speed = speeds[i]
        day = math.ceil(progress/speed)
        queue.append(day)
        
    cnt = 1
    beforeX = queue[0]
    for i in range(1, len(queue)):
        if beforeX >= queue[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            beforeX = queue[i]
    answer.append(cnt)            
    
    return answer
