from collections import deque

n = int(input())
graph = []
total = 0
res = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    queue = deque([(y, x)])
    graph[y][x] = 0
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in dirs:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny, nx))
                    cnt += 1

    return cnt
    
for i in range(n):
    graph.append([int(i) for i in input()])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i, j))
            total += 1

res.sort()
print(total)

for i in res:
    print(i)
