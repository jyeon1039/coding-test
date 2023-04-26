result = 0
n, k = map(int,input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

coin = coin[:len(str(k)) * 2]

for c in coin[::-1]:
    if k // c > 0:
        result += k // c
        k%= c

print(result)
