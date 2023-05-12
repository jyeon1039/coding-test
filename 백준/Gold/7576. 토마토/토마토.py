from collections import deque

m, n = map(int, input().split())
graph = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque([])

def bfs():
    while q:
        y, x = q.popleft()
        for (dy, dx) in dirs:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))
        
for y in range(n):
    graph.append(list(map(int, input().split())))
    for x in range(m):
        if graph[y][x] == 1:
            q.append((y, x))

bfs()
result = 0
    
for x in graph:
    if 0 in x:
        print(-1)
        break
    result = max(result, max(x))
else:
    print(result-1)
