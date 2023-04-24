def solution(dirs):
    dirMap = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    map = {}
    
    cur = (0, 0)
    
    for dir in dirs:
        x = cur[0]
        y = cur[1]
        nx = x + dirMap[dir][0]
        ny = y + dirMap[dir][1]
        
        if nx >= -5 and nx <= 5 and ny >= -5 and ny <= 5:
            cur = (nx, ny)
            map[(min(x, nx), min(y, ny), max(x, nx), max(y, ny))] = 1
        
    return len(map)