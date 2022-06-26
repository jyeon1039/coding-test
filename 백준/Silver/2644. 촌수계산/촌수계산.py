import sys
from collections import deque

n = int(sys.stdin.readline())
s, e = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[0]*(n+1) for i in range(n+1)]

for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    graph[y][x] = 1
    graph[x][y] = 1
    
distance = [0]*(n+1)

def bfs(v, e):
    queue = deque([v])
    while queue:
        x = queue.popleft()
        if x==e:
            return distance[x]
        
        for u in range(n+1):
            if graph[x][u] and not distance[u]:
                distance[u] = distance[x] + 1
                queue.append(u)
    return -1

print(bfs(s, e))

