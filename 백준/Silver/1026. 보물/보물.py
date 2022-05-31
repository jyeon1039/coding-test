n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
res = 0

for x in a:
    res += x * b.pop(b.index(max(b)))

print(res)
