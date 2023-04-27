s = input()

res = 0
tmp = ''
isMinus = False
for x in s:
    if x.isdigit():
        tmp += x
    else:
        if isMinus:
            res -= int(tmp)
        else:
            res += int(tmp)
        tmp = ''

        if x == '-':
            isMinus = True
else:
    if isMinus:
        res -= int(tmp)
    else:
        res += int(tmp)

print(res)
