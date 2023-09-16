def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns+1)] for _ in range(rows+1)]

    # 행렬 생성
    for y in range(1, rows+1):
        for x in range(1, columns+1):
            arr[y][x] = (y-1)*columns + x
    
    for y1, x1, y2, x2 in queries:
        tmp = arr[y1][x1]
        mini = tmp
        
        # 왼쪽 세로
        for y in range(y1, y2):
            test = arr[y+1][x1]
            arr[y][x1] = test
            mini = min(mini, test)

        # 하단 가로
        for x in range(x1, x2):
            test = arr[y2][x+1]
            arr[y2][x] = test
            mini = min(mini, test)

        # 오른쪽 세로
        for y in range(y2, y1, -1):
            test = arr[y-1][x2]
            arr[y][x2] = test
            mini = min(mini, test)

        # 상단 가로
        for x in range(x2, x1, -1):
            test = arr[y1][x-1]
            arr[y1][x] = test
            mini = min(mini, test)

        arr[y1][x1+1] = tmp
        answer.append(mini)
            
    return answer
