import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
lp, rp = 0, 1
sum = arr[lp]

while True:
        if sum == m:
                res += 1
                sum -= arr[lp]
                lp += 1
            
        if rp >= n and sum < m:
            break

        if sum > m:
            sum -= arr[lp]
            lp += 1
        elif sum < m:
            sum += arr[rp]
            rp += 1

print(res)
