n, k = map(int,input().split())
coins = []
res = 0

for i in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1): #역순으로 출력
    if k//coin > 0:
        res += k // coins[i]
        k %= coins[i]
        
print(res)
