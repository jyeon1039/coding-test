n, m = map(int, input().split())
r, c, d = map(int, input().split())

go_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back_dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
arr = []
result = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

while True:
    if arr[r][c] == 0: # 현재 칸이 0인 경우(청소되지 않은 칸인 경우)
        arr[r][c] = 2
        result += 1
    elif arr[r][c] == 1: # 현재 칸이 벽인 경우 작동 멈춤
        break

    # 주변 4칸 중 청소해야 하는 빈칸 있는지 탐색
    visit = [0]*4
    idx = 0
    for (dr, dc) in go_dirs:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            visit[idx] = 1

        idx += 1

    tmp = d
    for i in range(1, 5): # 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
        tmp -= 1

        if tmp < 0:
            tmp = 3
            
        if visit[tmp]:
            d = tmp
            r += go_dirs[d][0]
            c += go_dirs[d][1]
            break
    else: # 청소되지 않은 빈칸이 없는 경우 후진
        r += back_dirs[d][0]
        c += back_dirs[d][1]

print(result)