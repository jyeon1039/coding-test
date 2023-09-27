# 진수 변환
def transfer(number, n):
    result = ''
    alpha = {10: 'A', 11: 'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if number == 0:
        result = '0'
    while number > 0:
        x = number % n
        
        if 10 <= x <= 15:
            result = alpha[x] + result
        else:
            result = str(x) + result
        number //= n

    return result
      
# 말해야 하는 숫자 리스트
def getArray(n, t, m):
    result = ''
    number = 0
    while True:
        if len(result) >= t*m:
            break
        result += transfer(number, n)
        number += 1
    return result

def solution(n, t, m, p):
    answer = ''
    result = getArray(n, t, m)
    
    # 튜브가 말해야 하는 숫자를 순서에 맞게 출력
    for i in range(t):
        answer += result[m*i + (p-1)]
        
    return answer