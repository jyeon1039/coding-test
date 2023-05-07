from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def bfs():
    q = deque([1])
    result = -1 # 1은 제외하기 위해서 -1로 시작
    visited[1] = True
    
    while q:
        v = q.popleft()
        result += 1
        for u in graph[v]:
            if visited[u] == False:
                visited[u] = True
                q.append(u)
    return result

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs())