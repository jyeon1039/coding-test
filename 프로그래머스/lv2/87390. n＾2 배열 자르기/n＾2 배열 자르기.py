def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        row = i // n
        column = i % n
        
        answer.append(row+1 if (row>=column) else column+1)
        
    return answer