def solution(places):
    answer = []
    
    for place in places:
        isPass = True
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    # 거리가 1인 곳에 응시자가 있는 경우
                    if 0 <= y+1 < 5 and place[y+1][x] == 'P':
                        isPass = False
                        break
                    if 0 <= y-1 < 5 and place[y-1][x] == 'P':
                        isPass = False
                        break
                    if 0 <= x+1 < 5 and place[y][x+1] == 'P':
                        isPass = False
                        break
                    if 0 <= x-1 < 5 and place[y][x-1] == 'P':
                        isPass = False
                        break
                        
                    # 거리가 2인 곳에 응시자가 있는 경우
                    if 0 <= y+1 < 5 and place[y+1][x] == 'O':
                        if 0 <= y+2 < 5 and place[y+2][x] == 'P':
                            isPass = False
                            break
                        if 0 <= x+1 < 5 and place[y+1][x+1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                        if 0 <= x-1 < 5 and place[y+1][x-1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                    if 0 <= y-1 < 5 and place[y-1][x] == 'O':
                        if 0 <= y-2 < 5 and place[y-2][x] == 'P':
                            isPass = False
                            break
                        if 0 <= x-1 < 5 and place[y-1][x-1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                        if 0 <= x+1 < 5 and place[y-1][x+1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                    if 0 <= x+1 < 5 and place[y][x+1] == 'O':
                        if 0 <= x+2 < 5 and place[y][x+2] == 'P':
                            isPass = False
                        if 0 <= y+1 < 5 and place[y+1][x+1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                        if 0 <= y-1 < 5 and place[y-1][x+1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                    if 0 <= x-1 < 5 and place[y][x-1] == 'O':
                        if 0 <= x-2 < 5 and place[y][x-2] == 'P':
                            isPass = False
                        if 0 <= y-1 < 5 and place[y-1][x-1] == 'P': # 대각선의 경우
                            isPass = False
                            break
                        if 0 <= y+1 < 5 and place[y+1][x-1] == 'P': # 대각선의 경우
                            isPass = False
                            break
            if not isPass:
                break
        if not isPass:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer