n = int(input())
arr = list(map(int, input().split()))
res = [0]*n

for i in range(n):
    x = arr[i]
    d = 0
    idx = 0
    
    for j in range(n):
        if d == x and res[idx] == 0:
            res[idx] = i+1
            break
        if res[idx] == 0:
            d += 1
        idx += 1
    
for x in res:
    print(x, end = ' ')
