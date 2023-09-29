from itertools import combinations
from bisect import bisect_left #lower bound -> 원하는 값 이상이 처음 나오는 위치를 반환

def solution(infos, querys):
    answer = []
    candidates = {}
    
    # 모든 경우의 수
    for info in infos:
        tmp = info.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])
        for n in range(5):
            for c in combinations(conditions, n):
                key = ''.join(c)
                if key in candidates:
                    candidates[key].append(score)
                else:
                    candidates[key] = [score]
    
    for key in candidates.keys():
        candidates[key].sort() # 이분탐색을 위한 정렬
        
    for query in querys:
        q = query.replace(' and ', ' ').replace('-', ' ').split()
        key = ''.join(q[:-1])
        score = int(q[-1])
        cnt = 0
        if key in candidates:
            idx = bisect_left(candidates[key], score) # 이분탐색
            cnt = len(candidates[key])-idx
        answer.append(cnt)
        
    return answer