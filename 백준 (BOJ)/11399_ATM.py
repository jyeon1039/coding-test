n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
result = 0

for x in a:
    sum= sum + x
    result += sum

print(result)
