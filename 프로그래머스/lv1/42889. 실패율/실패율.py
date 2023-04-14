def solution(N, stages):
    answer = []
    
    stages.sort()

    result = dict(zip([i for i in range(1, N+1)], [0 for i in range(N)])) 
    preIdx = 0 # 스테이지에 도달한 사용자의 첫 번째 인덱스
    curIdx = 0 # 스테이지에 도달했고, 클리어까지 한 사용자의 첫 번째 인덱스
    stagesN = len(stages)
    
    while curIdx < stagesN:
        preIdx = curIdx
        x = stages[preIdx]
        while curIdx < stagesN and stages[curIdx] == x:
            curIdx += 1
        if x <= N: # 실패율 계산
            result[x] = (curIdx-preIdx) / (stagesN-preIdx)
            
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    return [x for (x,y) in result]