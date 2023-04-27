s = input()
isMinus = False
result = 0
n = ''

for ch in s:
    if ch.isdigit():
        n += ch
    else:
        if isMinus:
            result -= int(n)
        else:
            result += int(n)

        if ch == '-':
            isMinus = True
        n = ''
else: # 마지막 숫자 연산
    if isMinus:
        result -= int(n)
    else:
        result += int(n)
        
print(result)
