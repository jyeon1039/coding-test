import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

arr.sort(key=lambda x:(x[1], x[0]))

end = 0
res = 0

for (i, (s, e)) in enumerate(arr):
    if s >= end:
        end = e
        res += 1

print(res)