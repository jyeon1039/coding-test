import sys
from collections import deque
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
n, m = map(int, sys.stdin.readline().split())
graph = []
queue = deque([])

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dirs[i][0]
            nx = x + dirs[i][1]
            dist = graph[y][x] + 1
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
                graph[ny][nx] = dist
                queue.append((ny, nx))
    
for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

for x in range(n):
    for y in range(m):
        if graph[y][x] == 1:
            queue.append((y, x))

bfs()
    
res = 0
for i in range(m):
    if 0 in graph[i]:
        print(-1)
        exit(0)
    res = max(res, max(graph[i]))

print(res-1) #하루 빼기
