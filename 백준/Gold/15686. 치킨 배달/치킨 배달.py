from itertools import combinations

n, m = map(int, input().split())
graph = []
chickens = []
houses = []

for y in range(n):
    graph.append(list(map(int, input().split())))
    for x in range(n):
        if graph[y][x] == 2:
            chickens.append((y, x))
        elif graph[y][x] == 1:
            houses.append((y, x))

combi = list(combinations(chickens, m))

result = []

for chicken in combi:
    dis = []
    for (hy, hx) in houses:
        minD = 101
        for (cy, cx) in chicken:
            d = abs(hy-cy) + abs(hx-cx)
            if d < minD:
                minD = d
        dis.append(minD)
    result.append(sum(dis))

print(min(result))