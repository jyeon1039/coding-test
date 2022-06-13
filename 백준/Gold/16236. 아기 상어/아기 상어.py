import sys
from collections import deque

n = int(sys.stdin.readline())
INF = 1e9
graph = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
size = 2
eat = 0
time = 0

for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_y,shark_x = i,j
            graph[shark_y][shark_x] = 0

# 최단거리 계산
def bfs(shark_y, shark_x):
    dist = [[-1]*n for _ in range(n)]
    queue = deque([(shark_y,shark_x)])
    dist[shark_y][shark_x] = 0
    while queue:
        y, x = queue.popleft()
        for (dy, dx) in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny <n:
                if graph[ny][nx] <= size and dist[ny][nx] == -1:
                    queue.append((ny, nx))
                    dist[ny][nx] = dist[y][x]+1
    return dist

# 먹을 물고기 찾기
def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < size:
                if dist[i][j] < min_dist:
                    y, x = i,j
                    min_dist = dist[i][j]
    if min_dist == INF: #먹을 물고기가 없는 경우
        return None
    else:
        return y, x, min_dist

while True:
    value = find(bfs(shark_y, shark_x))
    if value == None:
        print(time)
        break
    else:
        shark_y,shark_x = value[0],value[1]
        time += value[2]
        graph[shark_y][shark_x] = 0
        eat += 1
        
    if eat >= size:
        size+=1
        eat = 0
