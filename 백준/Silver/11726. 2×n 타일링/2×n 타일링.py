n = int(input())
d = [0]*(n+1)

if n <= 2:
    print(n)
else:
    d[1] = 1
    d[2] = 2

    for x in range(3, n+1):
        d[x] = d[x-1] + d[x-2]

    print(d[x]%10007)