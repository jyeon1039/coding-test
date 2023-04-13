def solution(dartResult):
    idx = 0
    dart = []
    square = {'S': 1, 'D': 2, 'T': 3}

    while idx < len(dartResult):
        x = dartResult[idx]
        dartIdx = len(dart)-1
        if x == '*': # 스타상인 경우
            dart[dartIdx] = dart[dartIdx]*2
            if dartIdx != 0: #첫 번째 기회에서 나오지 않은 경우
                dart[dartIdx-1] *= 2
        elif x == '#': # 아차상인 경우
            dart[dartIdx] = dart[dartIdx]*(-1)
        else: # Single, Double, Triple 인 경우
            idx += 1
            while '0' <= dartResult[idx] <= '9':
                x += dartResult[idx]
                idx += 1
            dart.append(int(x) ** square[dartResult[idx]])
        idx += 1
    
    return sum(dart)