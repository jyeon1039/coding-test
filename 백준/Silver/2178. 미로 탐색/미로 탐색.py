from collections import deque

n, m = map(int, input().split())
graph = []
#상하좌우
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [[False]*m for i in range(n)]

def bfs(graph, n, m):
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        v = queue.popleft()
        x = v[1]
        y = v[0]
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and (not visited[ny][nx]):
                    visited[ny][nx] = True
                    distance = graph[y][x]
                    graph[ny][nx] = distance+1
                    queue.append((ny, nx))
        
for i in range(n):
    a = [int(i) for i in input()]
    graph.append(a)

bfs(graph, n, m)
print(graph[n-1][m-1])