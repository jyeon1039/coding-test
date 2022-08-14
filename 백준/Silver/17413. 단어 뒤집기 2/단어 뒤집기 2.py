import sys

s = sys.stdin.readline().strip()
arr = []

tmp = ""
isOpen = False
for x in s:
    if x == "<":
        isOpen = True
        if tmp != "":
            arr.append(tmp)
            tmp=""
        
    tmp += x
    
    if x == " ":
        if not isOpen:
            arr.append(tmp.strip())
            tmp = ""
    elif x == ">":
        arr.append(tmp.strip())
        tmp = ""
        isOpen = False

if tmp != "":
    arr.append(tmp.strip())

for i in range(0, len(arr)):
    x = arr[i]
    if x[0] == "<":
        print(x, end='')
    else:
        if i < len(arr)-1 and arr[i+1][0] == "<":
            print(x[::-1], end='')
        else:
            print(x[::-1], end=' ')
