n, k = map(int,input().split())
coins = []
res = 0

for i in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1): #역순으로 출력
    coin = coins[i]
    if k//coin > 0:
        res += k // coin
        k %= coin
        
print(res)
