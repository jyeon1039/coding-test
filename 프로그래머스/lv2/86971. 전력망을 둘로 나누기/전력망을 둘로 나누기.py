from collections import deque
import copy

def bfs(map, x, n):
    map_tmp = copy.deepcopy(map)
    queue = deque([x])
    cnt = 1
    while queue:
        v = queue.popleft()
        for u in range(1, n+1):
            if map_tmp[v][u] == 1:
                map_tmp[v][u] = 0
                map_tmp[u][v] = 0
                queue.append(u)
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = n
    map = [[0]*(n+1) for _ in range(n+1)]
    visited = [[0]*(n+1) for _ in range(n+1)]
    
    for v, u in wires:
        map[v][u] = 1
        map[u][v] = 1
        
    for v in range(1, n+1):
        for u in range(1, n+1):
            if map[v][u] == 1 and not visited[v][u]:
                #전선 제거
                map[v][u] = 0
                map[u][v] = 0
                visited[v][u] = 1
                visited[u][v] = 1
                
                cnt = bfs(map, v, n)
                diff = abs((n - cnt*2)) #(n-cnt)-cnt
                if diff < answer:
                    answer = diff
                    
                #전선 복구
                map[u][v] = 1
                map[v][u] = 1
                
    return answer