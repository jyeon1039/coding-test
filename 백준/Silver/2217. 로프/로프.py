import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

max = 0
for i in range(0, n):
    x = arr[i]*(i+1)
    if x > max:
        max = x

print(max)
