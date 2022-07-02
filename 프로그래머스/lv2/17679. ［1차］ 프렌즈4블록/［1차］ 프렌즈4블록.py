def removeBoard(m, n, arr, board):
    for x in range(n):
        while True:
            sy = 0
            ey = -1
            for y in range(m-1, -1, -1):
                if arr[y][x] == 1:
                    arr[y][x] = 0
                    if sy == 0:
                        sy = y
                elif arr[y][x] == 0 and sy > 0:
                    ey = y
                    break
            if sy != 0: # 지우는 경우 (1이 있는 경우)
                # 땡긴다
                diff = sy - ey
                for y in range(ey, -1, -1):
                    board[y+diff][x] = board[y][x]
                    arr[y+diff][x] = arr[y][x]
                # 삭제한다
                for y in range(sy-ey-1, -1, -1):
                    arr[y][x] = 0
                    board[y][x] = ' '

            else: #지울 게 없는 경우
                break

    return board

def solution(m, n, board):
    answer = 0

    tmp = []
    for x in board:
        tmp.append(list(x))
    board = tmp

    dirs = [(0, 1), (1, 0), (1, 1)]
    while True:
        isRemove = False
        arr = [[0]*n for _ in range(m)] # 지워지는 블록 나타내는 배열

        for y in range(m):
            for x in range(n):
                data = board[y][x]
                if data == ' ': # 지워진 칸의 경우 고려 X
                    continue

                sameCnt = 0
                for (dx, dy) in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[ny][nx] == data:
                            sameCnt += 1
                if sameCnt == 3:
                    arr[y][x] = 1
                    for (dx, dy) in dirs:
                        isRemove = True
                        nx = x + dx
                        ny = y + dy
                        arr[ny][nx] = 1

        if not isRemove: #not isRemove
            break
        else:
            board = removeBoard(m, n, arr, board)

    for y in range(m):
        for x in range(n):
            if board[y][x] == ' ':
                answer += 1

    return answer