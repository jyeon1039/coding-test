def solution(n, words):    
    for i in range(1, len(words)):
        w = words[i] # 현재 문자
        e = words[i-1][-1] # 이전 차례 사람의 끝 문자
        
        # 끝 문자와 시작하는 문자가 다를 경우
        # 이전에 등장했던 문자인 경우
        if (w[0] != e) or (w in words[:i-1]):
            return [i%n+1, i//n+1]
    
    return [0, 0] # 탈락자가 발생하지 않는 경우