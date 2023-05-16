import sys

sys.setrecursionlimit(10000)

def dfs(v):
    for u in graph[v]:
        if visited[u] == False:
            visited[u] = True
            dfs(u)
                
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = 0

for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for v in range(1, n+1):
    if visited[v] == False:
        dfs(v)
        res += 1

print(res)