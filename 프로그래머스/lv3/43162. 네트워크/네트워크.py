dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [0] * 200

def dfs(computers, v, n):    
    visited[v] = 1

    for u in range(n):
        if u != v and computers[v][u] and visited[u] == 0:
            dfs(computers, u, n)
    
def solution(n, computers):
    answer = 0
    for v in range(n):
        if visited[v] == 0:
            dfs(computers, v, n)
            answer += 1
                
    return answer