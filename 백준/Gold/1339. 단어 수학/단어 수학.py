# Greedy
n = int(input())
alpha = {chr(65+n):0 for n in range(26)} # ascii to charater: chr

for _ in range(n):
    word = input()
    
    for idx, char in enumerate(word[::-1]):
        alpha[char] += 10**idx

alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True) # value 값 기준으로 내림차순 정렬
result = 0

for i in range(9):
    result += (9-i) * alpha[i][1] # 해당 알파벳 value 값 * i

print(result)
