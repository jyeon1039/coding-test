def solution(lottos, win_nums):
    answer = []
    min = 0
    max = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    for lotto in lottos:
        if lotto == 0:
            max += 1
        else:
            if lotto in win_nums:
                min += 1
                max += 1
                
    answer.append(rank[max])
    answer.append(rank[min])
        
    return answer