import sys

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

for x in arr:
    print(x, end=' ')
