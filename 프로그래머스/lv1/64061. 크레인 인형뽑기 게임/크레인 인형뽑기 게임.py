def solution(board, moves):
    answer = 0
    stack = []
    
    for p in moves:
        for y in range(len(board[0])): # 세로의 길이만큼
            x = board[y][p-1]
            if x != 0:
                board[y][p-1] = 0
                if len(stack) != 0 and stack[-1] == x:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(x)
                break
                    
    return answer