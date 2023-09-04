import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int , sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(parent, u):
    visited[u] = True
    result[u] = parent

    for v in graph[u]:
        if not visited[v]:
            dfs(u, v)

dfs(1, 1)

for i in range(2, n+1):
    print(result[i])
