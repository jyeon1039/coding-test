import sys

a = list(i for i in sys.stdin.readline().strip())
a.sort(reverse=True)

for x in a:
    print(x, end='')
