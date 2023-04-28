n = int(input())
num = [int(input()) for _ in range(n)]
res = 0

while True:
    isChange = False
    for i in range(n-1):
        if num[i] >= num[i+1]:
            num[i] -= 1
            res += 1
            isChange = True
    if not isChange:
        break

print(res)
