import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

graph = [[0]*m for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    size = 1
    queue = deque([(y, x)])
    graph[y][x] = -1
    while queue:
        y, x = queue.popleft()
        for (dy, dx) in dirs:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = -1 #방문 표시
                    queue.append((ny, nx))
                    size += 1
    return size
    
    
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1

cnt = 0
res = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            res.append(bfs(y, x))
            cnt += 1
res.sort()

print(cnt)
for x in res:
    print(x, end = ' ')
