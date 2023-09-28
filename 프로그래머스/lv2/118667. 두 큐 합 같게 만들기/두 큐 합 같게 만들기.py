from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    while sum1 != sum2:
        if answer > len(queue1)*4:       
            answer = -1
            break
            
        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
        answer += 1
    
    return answer