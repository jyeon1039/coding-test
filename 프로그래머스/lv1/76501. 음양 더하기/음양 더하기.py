def solution(absolutes, signs):
    answer = 0
    
    for (x, sign) in zip(absolutes, signs):
        if sign:
            answer += x
        else:
            answer -= x
        
    return answer