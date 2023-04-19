def solution(n, words):
    humanN = 2 # 몇 번 사람인지 저장하는 인덱스
    idx = 1 # 몇 번째 차례인지 저장하는 인덱스

    for i in range(1, len(words)):
        w = words[i]
        e = words[i-1][-1] # 전 사람의 끝 문자

        if (w[0] != e) or (w in words[:i-1]):
            return [humanN, idx]

        if humanN == n:
            humanN = 1
            idx += 1 # 한 바퀴 돌았으니까 +1
        else:
            humanN += 1
    else:
        return [0, 0]