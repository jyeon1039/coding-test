import sys

s = int(sys.stdin.readline())
res = 0
for i in range(s):
    if s-i <= i:
        break
    else:
        s = s-i
        res += 1

print(res)
