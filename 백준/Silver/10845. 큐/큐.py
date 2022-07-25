import sys

t = int(sys.stdin.readline())

queue = []

for _ in range(t):
    s = sys.stdin.readline().strip()
    
    if s[:4] == "push":
        queue.append(int(s[5:]))
    elif s == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif s == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif s == "size":
        print(len(queue))
    elif s == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif s == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
        
