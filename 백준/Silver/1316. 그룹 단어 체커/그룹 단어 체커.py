import sys

n = int(sys.stdin.readline())
res = 0

for _ in range(n):
    dic = {}
    s = sys.stdin.readline()
    isGroup = True
    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != (i-1):
                isGroup = False
            else:
                dic[s[i]] = i
        else:
            dic[s[i]] = i
            
    if isGroup:
        res += 1

print(res)
