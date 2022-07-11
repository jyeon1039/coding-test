import sys
from collections import deque

while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    if n==0 and m==0:
        break

    graph = []
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def bfs(y, x):
        queue = deque([(y, x)])
        while queue:
            y, x = queue.popleft()
            for (dy, dx) in dirs:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < m and 0 <= nx < n:
                    if graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        queue.append((ny, nx))
            
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    res = 0
    
    for x in range(n):
        for y in range(m):
            if graph[y][x] == 1:
                bfs(y, x)
                res += 1

    print(res)
