import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline()
    word = s.split()
    for x in word:
        print(x[::-1], end = ' ')
    print()
