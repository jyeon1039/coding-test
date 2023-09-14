import math

def transfer(n, k):
    result = ""
    while(n != 0):
        result = str(n%k) + result
        n //= k
        
    return result

def isPrime(n, left, right):
    n = int(n[left: right])
    if n == 0 or n == 1:
        return 0
    for x in range(2, int(math.sqrt(n)+1)):
        if n % x == 0:
            return 0
    else:
        return 1
    
def solution(n, k):
    answer = 0
    n = transfer(n, k)
    left = 0
    right = 1

    while left < len(n) and right < len(n):
        if(n[right] == '0'):
            answer += isPrime(n, left, right)
            left = right
            right += 1
        else:
            right += 1
    else:
        answer += isPrime(n, left, right)
    return answer