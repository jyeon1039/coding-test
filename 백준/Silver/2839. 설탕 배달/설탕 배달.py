n = int(input())

arr = [-1]*(n+1)

if n >= 3:
    arr[3] = 1

if n >= 5:
    arr[5] = 1

for i in range(6, n+1):
    if arr[i-3] > 0 and arr[i-5] > 0:
        arr[i] = min(arr[i-3], arr[i-5]) + 1
    elif arr[i-3] > 0  or arr[i-5] > 0:
        arr[i] = max(arr[i-3], arr[i-5]) + 1
        
print(arr[n])