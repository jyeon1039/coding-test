def isCorrect(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] != 'P':
                continue
                
            # 거리가 1인 곳에 응시자가 있는 경우
            if 0 < y < 4 and (place[y+1][x] == 'P' or place[y-1][x] == 'P'):
                return 0
            if 0 < x < 4 and (place[y][x+1] == 'P' or place[y][x-1] == 'P'):
                return 0
            
            # 거리가 2인 곳에 응시자가 있는 경우 - 직선
            if x < 3:
                if place[y][x+1] == 'O' and place[y][x+2] == 'P':
                    return 0
            if y < 3:
                if place[y+1][x] == 'O' and place[y+2][x] == 'P':
                    return 0
            
            # 거리가 2인 곳에 응시자가 있는 경우 - 대각선
            if 0 < x and y < 4:
                if place[y+1][x-1] == 'P' and (place[y+1][x] == 'O' or place[y][x-1] == 'O'):
                    return 0
            if x < 4 and 0 < y:
                if place[y-1][x+1] == 'P' and (place[y-1][x] == 'O' or place[y][x+1] == 'O'):
                    return 0
            if 0 < x and 0 < y:
                if place[y-1][x-1] == 'P' and (place[y-1][x] == 'O' or place[y][x-1] == 'O'):
                    return 0
            if x < 4 and y < 4:
                if place[y+1][x+1] == 'P' and (place[y+1][x] == 'O' or place[y][x+1] == 'O'):
                    return 0  
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(isCorrect(place))
        
    return answer