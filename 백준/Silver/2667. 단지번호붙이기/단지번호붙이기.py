from collections import deque

n = int(input())
graph = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(y, x):
    q = deque([(y, x)])
    cnt = 0
    graph[y][x] = 0 # 방문 처리
    while q:
        y, x = q.popleft()
        cnt += 1
        
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < n and 0 <=ny and ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0 # 방문 처리
                    q.append((ny, nx))

    return cnt
    
for _ in range(n):
    graph.append([int(i) for i in input()])

result = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            result.append(bfs(y, x))

print(len(result))
for x in sorted(result):
    print(x)