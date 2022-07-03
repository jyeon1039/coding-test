def getAnswer(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == 'P':
                # 거리가 1인 곳에 응시자가 있는 경우
                if 0 <= y+1 < 5 and place[y+1][x] == 'P':
                    return 0
                if 0 <= y-1 < 5 and place[y-1][x] == 'P':
                    return 0
                if 0 <= x+1 < 5 and place[y][x+1] == 'P':
                    return 0
                if 0 <= x-1 < 5 and place[y][x-1] == 'P':
                    return 0

                # 거리가 2인 곳에 응시자가 있는 경우
                if 0 <= y+1 < 5 and place[y+1][x] == 'O':
                    if 0 <= y+2 < 5 and place[y+2][x] == 'P':
                        return 0
                    if 0 <= x+1 < 5 and place[y+1][x+1] == 'P': # 대각선의 경우
                        return 0
                    if 0 <= x-1 < 5 and place[y+1][x-1] == 'P': # 대각선의 경우
                        return 0
                if 0 <= y-1 < 5 and place[y-1][x] == 'O':
                    if 0 <= y-2 < 5 and place[y-2][x] == 'P':
                        return 0
                    if 0 <= x-1 < 5 and place[y-1][x-1] == 'P': # 대각선의 경우
                        return 0
                    if 0 <= x+1 < 5 and place[y-1][x+1] == 'P': # 대각선의 경우
                        return 0
                if 0 <= x+1 < 5 and place[y][x+1] == 'O':
                    if 0 <= x+2 < 5 and place[y][x+2] == 'P':
                        return 0
                    if 0 <= y+1 < 5 and place[y+1][x+1] == 'P': # 대각선의 경우
                        return 0
                    if 0 <= y-1 < 5 and place[y-1][x+1] == 'P': # 대각선의 경우
                        return 0
                if 0 <= x-1 < 5 and place[y][x-1] == 'O':
                    if 0 <= x-2 < 5 and place[y][x-2] == 'P':
                        return 0
                    if 0 <= y-1 < 5 and place[y-1][x-1] == 'P': # 대각선의 경우
                        return 0
                    if 0 <= y+1 < 5 and place[y+1][x-1] == 'P': # 대각선의 경우
                        return 0
    return 1
def solution(places):
    answer = []
    
    for place in places:
        answer.append(getAnswer(place))
        
    return answer