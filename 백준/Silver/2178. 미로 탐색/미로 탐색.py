from collections import deque

n, m = map(int, input().split())
graph = []
#상하좌우
x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
visited = [[False]*m for i in range(n)]

def bfs(graph, n, m):
    queue = deque([(0, 0)])
    visited[0][0] = True
    distance = 1

    while queue:
        v = queue.popleft()
        curX = v[1]
        curY = v[0]
        for i in range(4):
            nextX = curX + x[i]
            nextY = curY + y[i]
            distance = graph[curY][curX]
            if 0 <= nextY < n and 0 <= nextX < m:
                if (not visited[nextY][nextX]) and graph[nextY][nextX] == 1:
                    visited[nextY][nextX] = True
                    graph[nextY][nextX] = distance+1
                    queue.append((nextY, nextX))
    
        
for i in range(n):
    a = [int(i) for i in input()]
    graph.append(a)

bfs(graph, n, m)
print(graph[n-1][m-1])
