def solution(d, budget):
    answer = 0
    d.sort()
    
    for x in d:
        if budget < x:
            break
        answer += 1
        budget -= x
        
    return answer