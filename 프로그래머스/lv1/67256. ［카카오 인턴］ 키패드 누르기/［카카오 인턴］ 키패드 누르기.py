def solution(numbers, hand):
    answer = ''
    
    # 2차원에서의 각 숫자의 위치
    position = {0: (3, 1), 1: (0, 0), 2: (0, 1), 3: (0, 2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2)}
    # 왼손 초기 위치
    lx = 0
    ly = 3
    
    # 오른손 초기 위치
    rx = 2
    ry = 3
    
    for n in numbers:
        (y, x) = position[n] # 숫자의 위치
        
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            ld = abs(lx-x)+abs(ly-y)
            rd = abs(rx-x)+abs(ry-y)
            
            # 거리가 더 가까운 손의 엄지손가락 사용
            if ld < rd:
                answer += 'L'
            elif ld > rd:
                answer += 'R'
            else: # 거리가 가까울 경우 손잡이에 따라 이동
                answer += hand[0].upper()
        
        # 엄지손가락의 위치 이동
        if answer[-1] == 'L':
            lx = x
            ly = y
        else:
            rx = x
            ry = y
            
    return answer