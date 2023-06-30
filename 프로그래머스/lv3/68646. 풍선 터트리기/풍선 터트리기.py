def solution(a):
    answer = [False]*len(a) # 양 쪽은 끝까지 살아남을 수 있음
    lmin = 1000000001
    rmin = 1000000001
    
    # 양쪽의 최소값 중 하나라도 자신보다 크면 됨. 즉 자신이 양쪽 중에서 최소값이면 됨
    for i in range(len(a)):
        if a[i] < lmin:
            answer[i] = True
            lmin = a[i]
        if a[(len(a)-1)-i] < rmin:
            answer[(len(a)-1)-i] = True
            rmin = a[(len(a)-1)-i]
                
    return sum(answer)