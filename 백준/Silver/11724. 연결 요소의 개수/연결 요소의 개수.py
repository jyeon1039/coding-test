import sys

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)

def dfs(v):
    visited[v] = True
    
    for u in range(1, n+1):
        if graph[v][u] == 1:
            if not visited[u]:
                dfs(u)
    
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[y][x] = 1
    graph[x][y] = 1

res = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        res += 1

print(res)
