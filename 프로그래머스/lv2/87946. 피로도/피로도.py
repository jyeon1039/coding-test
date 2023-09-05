from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    for p in permutations([i for i in range(n)], n):
        tmp_k = k
        cnt = 0
        for i in p:
            if dungeons[i][0] <= tmp_k: # 최소 필요 피로도 <= 현재 피로도
                tmp_k -= dungeons[i][1] # 현재 피로도 - 소모 피로도
                cnt += 1
        if cnt > answer: # 최대 던전 수 변경
            answer = cnt
    
    return answer