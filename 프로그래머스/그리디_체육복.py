def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))

    #여벌 체육복을 빌릴 수 있을 경우
    #lost로 for문 돌면 reserve에서도 삭제해주어야 하므로 reserve로 for문 돌림
    for x in reserve_only:
        if x-1 in lost_only:
            lost_only.remove(x-1)
        elif x+1 in lost_only:
            lost_only.remove(x+1)

    return n - len(lost_only)
