from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque([])
    result = 0

    for i in range(n):
        queue.append((i, arr[i]))
        
    priority = sorted(arr)

    while priority:
        (idx, x) = queue.popleft()

        if x == priority[-1]: # 중요도가 최대값이랑 같은 경우
            result += 1
            
            if idx == m:
                break 
            
            priority.pop()
        else: # 현재 문서보다 중요도가 높은 문서가 있는 경
            queue.append((idx, x))


    print(result)