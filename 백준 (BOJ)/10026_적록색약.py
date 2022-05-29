from collections import deque

n = int(input())
visited = [[False]*n for i in range(n)]
#normalVisited = [[False]*n]*n
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
graph = []
normalCnt = 0
weakCnt = 0

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    
    while queue:
        v = queue.popleft()
        r = v[0]
        c = v[1]
        visited[r][c] = True
        color = graph[r][c]
        for p in range(4):
            nextR = r+y[p]
            nextC = c+x[p]
            
            if 0<= nextR < n and 0 <= nextC < n and (not visited[nextR][nextC]):
                nextColor = graph[nextR][nextC]

                if color == nextColor:
                    visited[nextR][nextC] = True
                    queue.append((nextR, nextC))
                

for i in range(n):
    a = [i for i in input()]
    graph.append(a)

# 정상인 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j)
            normalCnt += 1

visited = [[False]*n for i in range(n)]

# 녹색을 적색으로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
# 색약인 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j)
            weakCnt += 1
            
print(normalCnt, weakCnt)
