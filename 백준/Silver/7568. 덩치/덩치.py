import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
    
for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]: # 자신보다 덩치가 큰 사람이 있을 때 rank + 1 한다
            rank += 1
    print(rank, end = ' ')