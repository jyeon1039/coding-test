import sys

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))
sum = sum(arr)
notN1 = 0
notN2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum - (arr[i] + arr[j]) == 100:
            notN1 = arr[i]
            notN2 = arr[j] 
            break
        
arr.remove(notN1)
arr.remove(notN2)
arr.sort()

for x in arr:
    print(x)
