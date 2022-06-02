import sys

n = int(sys.stdin.readline())
p = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    p.append((x, y))

p.sort(key=lambda x:(x[0], x[1]))

for (x, y) in p:
    print(x, y)
