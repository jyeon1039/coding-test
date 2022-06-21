import sys

arr = [1]*10001

def d(n):
    sum = n
    while  n != 0:
        sum += n%10
        n //= 10
    if sum <= 10000:
        arr[sum] = 0
    
for i in range(1, 10000):
    d(i)

for i in range(1, 10001):
    if arr[i]:
        print(i)
