from collections import deque
import sys

def bfs(v):
  queue = deque()
  queue.append(v)       
  visited[v] = 1   
  while queue:
    v = queue.popleft()
    print(v, end = " ")
    
    for i in range(1, n + 1):
      if visited[i] == 0 and graph[v][i] == 1:
        queue.append(i)
        visited[i] = 1

def dfs(v):
  visited2[v] = 1        
  print(v, end = " ")
  
  for i in range(1, n + 1):
    if visited2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visited = [0] * (n + 1)
visited2 = [0] * (n + 1)

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x][y] = graph[y][x] = 1

dfs(v)
print()
bfs(v)
