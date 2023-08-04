from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    # 5개를 각 점수에 나누기 위해 중복 조합 사용
    for combi in combinations_with_replacement(range(11),n):
        lion_info = [0]*11 # 라이언 점수
        
        # 10-i 인 이유 : info 의 0번째 index의 점수가 10-i 이기 때문에 통일되게 만들기 위해서
        for i in combi:
            lion_info[10-i] += 1
        
        apeach, lion = 0, 0
        
        for i in range(11):
            if info[i] == lion_info[i] == 0: # 0인 경우 넣어주지 않으면 두 번째 if 문에 걸리기 때문에 넣어주어야 함
                continue
            elif info[i] >= lion_info[i]:
                apeach += 10-i
            elif info[i] < lion_info[i]:
                lion += 10-i
        
        if max_diff < (lion-apeach) :
            max_diff = lion-apeach
            answer = lion_info
            
    return answer