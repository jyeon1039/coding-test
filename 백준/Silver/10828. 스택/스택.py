import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    s = sys.stdin.readline().strip()
    if s[:4] == "push":
        x = int(s[5:])
        stack.append(x)
    elif s == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif s == "size":
        print(len(stack))
    elif s == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s == "top":
        if len(stack) == 0:
            print(-1)
        else:
           print(stack[-1])
