from collections import deque

def popAndAppend(a, b):
    x = a.popleft()
    b.append(x)
    return x
    
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -1
    cnt = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    limit = len(queue1)*3
    
    while True:        
        if sum1 == sum2:
            answer = cnt
            break
        elif cnt == limit:
            break
        
        if sum1 > sum2:
            x = popAndAppend(queue1, queue2)
            sum1 -= x
            sum2 += x
            
        else:
            x = popAndAppend(queue2, queue1)
            sum2 -= x
            sum1 += x
            
        cnt += 1
    
    return answer