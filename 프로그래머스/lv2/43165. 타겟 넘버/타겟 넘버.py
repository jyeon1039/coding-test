answer = 0

def dfs(numbers, target, sum, idx):
    global answer
    
    if idx == len(numbers):
        if sum == target:
            answer += 1
    else:
        dfs(numbers, target, sum + numbers[idx], idx+1)
        dfs(numbers, target, sum + -numbers[idx], idx+1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    
    return answer