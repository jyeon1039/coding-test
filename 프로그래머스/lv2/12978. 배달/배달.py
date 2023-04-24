import heapq

# 다익스트라 알고리즘
def dijkstra(dist, map):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        hour, node = heapq.heappop(heap) # 가장 작은 값 추출
        for h, n in map[node]:
            if hour+h < dist[n]:
                dist[n] = hour+h
                heapq.heappush(heap, [hour+h, n])
    
def solution(N, road, K):
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0 # 1번은 자기자신이므로 0
    map = [[] for _ in range(N+1)]
    for (a, b, c) in road:
        map[a].append([c, b])
        map[b].append([c, a])

    dijkstra(dist, map)
    
    return len([i for i in dist if i <= K])