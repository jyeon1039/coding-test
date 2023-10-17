# 게임에서 이겼는지 확인
def win(board, t):
    # 가로줄 판단
    for row in board:
        if row == [t, t, t]:
            return True
        
    # 세로줄 판단a
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
        
    # 대각선 판단
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    
    return False
    
def solution(board):    
    board = [list(row) for row in board]
    
    # O 의 개수가 X 의 개수보다 같거나 1 많아야 한다
    o_count, x_count = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                o_count += 1
            if c == 'X':
                x_count += 1
                
    if not (o_count == x_count or o_count == x_count + 1):
        return 0
                
    # O 혹은 X 만 승리조건을 만족해야 한다
    if win(board, 'O') and win(board, 'X'):
        return 0
    
    # O 가 승리했다면 o_ount == x_count+1 이어야 한다
    if win(board, 'O') and o_count != x_count + 1:        
        return 0
    
    # X 가 승리했다면 o_count == x_count 이어야 한다
    if win(board, 'X') and o_count != x_count:
        return 0
    
    return 1