from collections import deque

def bfs(maps):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q = deque([(0, 0)])
    n = len(maps)
    m = len(maps[0])
    
    while q:
        y, x = q.popleft()
        for (dy, dx) in dirs:
            ny = y + dy
            nx = x + dx
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append((ny, nx))
        
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
    
def solution(maps):
    return bfs(maps)