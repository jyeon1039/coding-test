import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = []
res = set()

for _ in range(n):
    arr.append(sys.stdin.readline().strip())

for x in permutations(arr, k):
    res.add(''.join(x))

print(len(res))