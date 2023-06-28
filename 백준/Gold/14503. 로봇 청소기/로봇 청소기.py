n, m = map(int, input().split())
r, c, d = map(int, input().split())

go_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back_dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
arr = []
result = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

while True:
    if arr[r][c] == 0: # 현재 칸이 청소되지 않은 칸인 경우
        arr[r][c] = 2
        result += 1
    elif arr[r][c] == 1: # 현재 칸이 벽인 경우 작동 멈춤
        break

    idx = d
    for i in range(1, 5): # 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
        idx -= 1
        
        if idx < 0:
            idx = 3

        nr = r + go_dirs[idx][0]
        nc = c + go_dirs[idx][1]

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            d = idx
            r  = nr
            c = nc
            break
    else: # 청소되지 않은 빈칸이 없는 경우 후진
        r += back_dirs[d][0]
        c += back_dirs[d][1]

print(result)
