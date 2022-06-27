import sys

n,m =map(int, sys.stdin.readline().split())
dic = {}
cnt = 0

for _ in range(n):
    name = sys.stdin.readline().strip()
    dic[name] = 1

for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in dic:
        dic[name] += 1
        cnt += 1

res = []
for k, v in dic.items():
    if v == 2:
        res.append(k)

res.sort()

print(cnt)
for x in res:
    print(x)
