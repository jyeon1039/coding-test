import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

def bfs(graph):
    res = 0
    queue = deque([1])
    visited[1] = True

    while queue:
        v = queue.popleft()
        for u in range(1, n+1):
            if graph[v][u] == 1 and not visited[u]:
                res += 1
                visited[u] = True
                queue.append(u)

    return res
    
for i in range(k):
    v, u = map(int, sys.stdin.readline().split())
    graph[v][u] = 1
    graph[u][v] = 1

print(bfs(graph))
