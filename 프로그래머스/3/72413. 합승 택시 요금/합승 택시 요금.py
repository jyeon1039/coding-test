from math import inf
from heapq import heappush, heappop

# 다익스트라 - 최단 거리
def dijkstra(n, graph, start):
    dist = [inf for _ in range(n)] # start 기준으로 거리
    dist[start] = 0
    
    q = []
    heappush(q, (dist[start], start)) # 거리와 노드
    while q:
        cur_dist, u = heappop(q)
        if dist[u] >= cur_dist: # 현재 거리가 저장된 거리보다 작을 때만 진행
            for v in range(n):
                new_dist = cur_dist + graph[u][v]
                if new_dist < dist[v]: # 새로운 거리가 저장된 거리보다 작을 때만 진행
                    dist[v] = new_dist
                    heappush(q, [new_dist, v])
    return dist
        
def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    graph = [[inf]*n for _ in range(n)]
    
    for fare in fares:
        u, v, f = fare
        graph[u-1][v-1] = f
        graph[v-1][u-1] = f
        
    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))
    answer = inf
    
    # k를 거쳐서 a, b까지 가는 최소 비용
    for k in range(n): 
        answer = min(answer,
                    min_graph[s][k] + min_graph[k][a] + min_graph[k][b])
        
    return answer