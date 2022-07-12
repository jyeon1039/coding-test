import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline()
    sum = 0
    
    for x in s:
        if x == '(':
            sum += 1
        elif x == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break
        
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
