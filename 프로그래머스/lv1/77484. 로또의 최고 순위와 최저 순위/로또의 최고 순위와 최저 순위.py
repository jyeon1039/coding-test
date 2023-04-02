def solution(lottos, win_nums):
    answer = []
    min = 0
    max = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
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