from itertools import combinations

def solution(relation):
    answer = []
    rows = len(relation)
    cols = len(relation[0])
    combi = []
    
    # 속성 조합
    for n in range(1, cols+1):
        combi.extend(list(combinations([i for i in range(0, cols)], n)))
    
    for idxs in combi:
        temp = []
        for r in relation:
            tmp = tuple()
            for i in idxs:
                tmp += (r[i],) # 튜플 더하기
            temp.append(tmp)
        
        if len(set(temp)) == rows: # 유일성 만족
            # 최소성 만족
            for unique in answer:
                if set(unique).issubset(set(idxs)):
                    break
            else:
                answer.append(idxs)
    return len(answer)