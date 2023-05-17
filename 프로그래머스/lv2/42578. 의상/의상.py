# (0, yellow_hat, green_turban) (0, blue_sunglasses)
# 일 때 모두 안 입은 (0, 0) 만 빼기 위하여 결과에서 -1

def solution(clothes):
    answer = 1
    hashmap = {}
    
    for (c, t) in clothes:
        if t not in hashmap:
            hashmap[t] = 1
        else:
            hashmap[t] += 1
    
    for x in hashmap.values():
        answer *= (x + 1) # +1 하는 이유: 안 입은 경우도 고려
                 
    return answer - 1 # 모두 안 입은 경우