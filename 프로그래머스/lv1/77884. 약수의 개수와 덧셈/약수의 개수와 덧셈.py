def getDivisorCnt(x):
    cnt = 1 #나 자신은 생략
    for i in range(1, x):
        if x % i == 0:
            cnt += 1
    return cnt
    
def solution(left, right):
    answer = 0
    
    for x in range(left, right+1):
        cnt = getDivisorCnt(x)
        if cnt % 2 == 0:
            answer += x
        else:
            answer -= x
            
    return answer