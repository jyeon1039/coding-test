import sys

s = sys.stdin.readline()
n = len(s)
arr = []

for i in range(0, n-1):
    arr.append(s[i:n-1])

arr.sort()

for x in arr:
    print(x)
