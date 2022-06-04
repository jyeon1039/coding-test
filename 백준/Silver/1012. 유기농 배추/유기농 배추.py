from collections import deque
import sys

t = int(sys.stdin.readline())
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(y, x, graph, n, m):
    queue = deque([(y, x)])
    
    while queue:
        y, x = queue.popleft()
        graph[y][x] = 0
        for (dy, dx) in dirs:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx]:
                queue.append((ny, nx))
                graph[ny][nx] = 0

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
        
    res = 0
    for y in range(n):
        for x in range(m):
          if graph[y][x] == 1:
            bfs(y, x, graph, n, m)
            res += 1 
            
    print(res)
