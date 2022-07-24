def solution(number, k):
    answer = [] # stack
    
    for x in number:
        # k > 0 이고, answer에 원소가 있어야하고, 마지막 원소가 x보다 작을 때 pop
        while k > 0 and answer and answer[-1] < x:
            answer.pop()
            k -= 1
        answer.append(x)
    
    return ''.join(answer[:len(answer) - k])