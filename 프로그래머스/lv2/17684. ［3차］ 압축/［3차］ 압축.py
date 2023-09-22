def solution(msg):
    answer = []
    dictionary = {}
    dicIdx= 27

    # 사전 생성
    for i in range(1, 27):
        ch = chr(i+(ord('A')-1))
        dictionary[ch] = i
    
    idx = 0
    while idx < len(msg):
        tmpIdx = 0
        cnt = 0 # 아래의 for문에서 idx를 그대로 사용하기 위하여 횟수를 세어주는 변수 선언
        for j in range(idx+1, len(msg)+1):
            tmp = msg[idx:j]
            if tmp in dictionary:
                tmpIdx = dictionary[tmp]
                cnt += 1
            else:
                dictionary[tmp] = dicIdx
                dicIdx += 1
                break
        idx += cnt
        answer.append(tmpIdx)
        
    return answer